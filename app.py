import os
import datetime
from os import path
from flask import (
    Flask,
    flash,
    render_template,
    redirect,
    request,
    session,
    url_for)
from flask_mail import Mail,  Message
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USE_TLS'] = True
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)
mail = Mail(app)

# Collections

user_collection = mongo.db.users
recipe_collection = mongo.db.recipes
type_collection = mongo.db.recipe_types
likes_collection = mongo.db.likes


@app.route('/')
@app.route('/index')
def index():
    if 'user' in session:
        db_user = user_collection.find_one({"username": session['user']})
        if db_user:
            return redirect(url_for('profile', user=db_user['username']))
    all_recipes = list(recipe_collection.find().sort("likes", -1).limit(3))
    return render_template("index.html", all_recipes=all_recipes)


@app.route('/signin', methods=['GET'])
def signin():
    if 'user' in session:
        db_user = user_collection.find_one({"username": session['user']})
        if db_user:
            return redirect(url_for('profile', user=db_user['username']))
    else:
        return render_template("signin.html")


@app.route('/login', methods=['POST'])
def login():
    form = request.form.to_dict()
    db_user = user_collection.find_one({"username": form['username']})
    if db_user:
        if check_password_hash(db_user['password'], form['password']):
            session['user'] = form['username']
            flash('Login successful')
            return redirect(url_for('profile', user=db_user['username']))
        else:
            flash('Username or password incorrect')
            return render_template("signin.html")
    flash("Username or password incorrect")
    return render_template("signin.html")


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if 'user' in session:
        flash("You are already logged in")
        return redirect(url_for('profile', user=session["user"]))
    if request.method == 'POST':
        form = request.form.to_dict()
        if form['password'] == form['password1']:
            user = user_collection.find_one({"username": form['username']})
            if user:
                flash(f"{form['username']} already exists")
                return redirect(url_for('add_user'))
            else:
                user_collection.insert_one(
                    {
                        'username': form['username'],
                        'picture': form['picture'],
                        'bio': form['bio'],
                        'email': form['email'],
                        'password': generate_password_hash(form['password'])
                    }
                )
                db_user = user_collection.find_one(
                    {"username": form['username']})
                if db_user:
                    session['user'] = db_user['username']
                    return redirect(url_for('profile',
                                            user=db_user['username']))
                else:
                    flash('Issues saving profile')
                    return redirect(url_for('add_user'))
        else:
            flash('Passwords do not match')
            return redirect(url_for('add_user'))
    return render_template('signup.html')


@app.route('/profile/<user>', methods=["GET", "POST"])
def profile(user):
    username = user_collection.find_one({"username": user})
    profile = 1
    my_recipes = list(recipe_collection.find({"user": user})
                      .sort("datetime", -1))
    recipe_count = len(my_recipes)
    if 'user' in session:
        return render_template('profile.html',
                               user=username,
                               my_recipes=my_recipes,
                               recipe_count=recipe_count,
                               profile=profile)
    return redirect(url_for('signin'))


@app.route('/edit_user/<user_id>', methods=["GET", "POST"])
def edit_user(user_id):
    if request.method == "POST":
        if request.form.get("password") == request.form.get("password1"):
            edit = {"$set": {
                    "username": request.form.get("username"),
                    "picture": request.form.get("picture"),
                    "bio": request.form.get("bio"),
                    "email": request.form.get("email")
                    }}
        user_collection.update({"_id": ObjectId(user_id)}, edit)
        flash("User info updated")
        user = user_collection.find_one({"username": session["user"]})
        my_recipes = list(recipe_collection.find({"user": user})
                          .sort("datetime", -1))
        return redirect(url_for('profile', user=session["user"],
                        my_recipes=my_recipes))
    user = user_collection.find_one({"username": session["user"]})
    return render_template('edit_user.html', user=user)


@app.route('/change_password/<user_id>', methods=["GET", "POST"])
def change_password(user_id):
    user = user_collection.find_one({"_id": ObjectId(user_id)})
    new_password = request.form.get("new_password")
    confirm_password = request.form.get("new_password1")
    if request.method == "POST":
        if check_password_hash(user['password'], request.form.get("password")):
            if new_password == confirm_password:
                user_collection.update({"_id": ObjectId(user_id)},
                                       {"$set": {"password":
                                        generate_password_hash
                                        (request.form.get("new_password"))}})
                my_recipes = list(recipe_collection.find({"user": user})
                                  .sort("datetime", -1))
                flash("Password Changed")
                return redirect(url_for('profile', user=session["user"],
                                my_recipes=my_recipes))
            flash("new passwords do not match")
            return render_template('change_password.html', user=user)
        flash("Old Password Incorrect")
        return render_template('change_password.html', user=user)
    return render_template('change_password.html', user=user)


@app.route('/logout', )
def logout():
    session.pop('user')
    flash('User Logged Out')
    return redirect(url_for('index'))


@app.route('/add_recipe', methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_type": request.form.get("recipe_type"),
            "name": request.form.get("recipe_name"),
            "description": request.form.get("description"),
            "picture": request.form.get("recipe_image"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
            "user": session["user"],
            "datetime": datetime.datetime.now().timestamp(),
            "likes": 0
        }
        recipe_collection.insert_one(recipe)
        flash("Recipe Added to Your Cookbook!")
        return redirect(url_for('profile', user=session["user"]))
    recipe_types = type_collection.find().sort("type_name", 1)
    user = user_collection.find_one({"username": session["user"]})
    return render_template('add_recipe.html',
                           recipe_types=recipe_types,
                           user=user)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    user = user_collection.find_one({"username": session["user"]})
    if request.method == "POST":
        edit = {"$set": {
            "recipe_type": request.form.get("recipe_type"),
            "name": request.form.get("recipe_name"),
            "description": request.form.get("description"),
            "picture": request.form.get("recipe_image"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
            "user": session["user"],
        }}
        recipe_collection.update({"_id": ObjectId(recipe_id)}, edit)
        flash("Recipe Edited")
        return redirect(url_for('profile', user=session["user"]))
    recipe = recipe_collection.find_one({"_id": ObjectId(recipe_id)})
    recipe_types = type_collection.find().sort("type_name", 1)
    ingredients = range(0, len(recipe['ingredients']))
    method_steps = range(0, len(recipe['method']))
    return render_template('edit_recipe.html', recipe=recipe,
                           recipe_types=recipe_types, user=user,
                           ingredients=ingredients, method_steps=method_steps)


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    recipe_collection.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe deleted")
    return redirect(url_for('profile', user=session["user"]))


@app.route('/browse_date')
def browse_date():
    browse = 1
    browse_date = 1
    user = user_collection.find_one({"username": session["user"]})
    all_recipes = list(recipe_collection.find().sort("datetime", -1))
    return render_template('browse.html', all_recipes=all_recipes,
                           user=user,
                           browse=browse,
                           browse_date=browse_date)

@app.route('/browse_like')
def browse_like():
    browse = 1    
    browse_like = 1
    user = user_collection.find_one({"username": session["user"]})
    all_recipes = list(recipe_collection.find().sort("likes", -1))
    return render_template('browse.html', all_recipes=all_recipes,
                           user=user,
                           browse=browse,
                           browse_date=browse_like)


@app.route('/search', methods=["GET", "POST"])
def search():
    search_page = 1
    user = user_collection.find_one({"username": session["user"]})
    if request.method == "POST":
        query = request.form.get("query")
        all_recipes = list(recipe_collection.find({"$text":
                           {"$search": query}}).sort("datetime", -1))
        if len(all_recipes) == 0:
            flash("No recipes found, please search again")
            return render_template('search.html',
                                   user=user,
                                   search_page=search_page)
        flash("Search successful!")
        return render_template('search.html', all_recipes=all_recipes,
                               user=user,
                               search_page=search_page)
    return render_template('search.html', user=user, search_page=search_page)


"""
@app.route('/search', methods=["GET"])
def search():
    user = user_collection.find_one({"username": session["user"]})
    query = request.form.get("query")
    search_page = 1
    if request.method == "GET":
        if query:
            all_recipes = list(recipe_collection.find({"$text":
                            {"$search": query}}).sort("datetime", -1))
            if len(all_recipes) == 0:
                flash("No recipes found, please search again")
                return render_template('search.html',
                                        user=user,
                                        all_recipes=all_recipes,
                                        search_page=search_page)
            return render_template('search.html',
                                    user=user,
                                    all_recipes=all_recipes,
                                    search_page=search_page)
        else:
            all_recipes = []
            return render_template("search.html",
                                user=user,
                                all_recipes=all_recipes,
                                search_page=search_page)
"""

@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id): 
    if 'user' in session:
            user = user_collection.find_one({"username": session["user"]})
            recipe = recipe_collection.find_one({"_id": ObjectId(recipe_id)})
            ingredients = range(0, len(recipe['ingredients']))
            method_steps = range(0, len(recipe['method']))
            return render_template('view_recipe.html', recipe=recipe,
                                ingredients=ingredients, method_steps=method_steps, user=user,
                                recipe_user=recipe['user'])
    else:
        recipe = recipe_collection.find_one({"_id": ObjectId(recipe_id)})
        ingredients = range(0, len(recipe['ingredients']))
        method_steps = range(0, len(recipe['method']))
        return render_template('view_recipe.html', recipe=recipe,
                                ingredients=ingredients, method_steps=method_steps)


@app.route('/like_recipe/<recipe_id>')
def like_recipe(recipe_id):
    recipe = recipe_collection.find_one({"_id": ObjectId(recipe_id)})
    ingredients = range(0, len(recipe['ingredients']))
    method_steps = range(0, len(recipe['method']))
    like_count = recipe['likes']
    user_like = likes_collection.find_one(
        {
            "username": session["user"],
            "recipe_id": recipe["_id"]
        }
    )
    if user_like:
        recipe_collection.update(
            {"_id": ObjectId(recipe_id)},
            {"$set":
                {"likes": like_count - 1}})
        likes_collection.remove(user_like)
        return redirect(url_for('view_recipe', recipe_id=recipe['_id'],
                        recipe=recipe,
                        ingredients=ingredients,
                        method_steps=method_steps,
                        user_like=user_like,
                        user=session["user"], recipe_user=recipe['user']))
    else:
        recipe_collection.update({"_id": ObjectId(recipe_id)},
                                 {"$set":
                                 {"likes": like_count + 1}})
        likes_collection.insert_one(
            {
                'username': session["user"],
                'recipe_id': recipe['_id']
            }
        )
        return redirect(url_for('view_recipe',
                        recipe_id=recipe['_id'],
                        recipe=recipe,
                        ingredients=ingredients,
                        method_steps=method_steps,
                        user_like=user_like,
                        user=session["user"],
                        recipe_user=recipe['user']))


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        recipient = os.environ.get('MAIL_USERNAME')
        msg1 = Message(sender=request.form['email'],
                      recipients=[recipient])
        msg1.body = request.form['query']
        mail.send(msg1)
        flash("Contact form received")
        return redirect ('index')

    if 'user' in session:
        db_user = user_collection.find_one({"username": session['user']})
        if db_user:
            return render_template('contact.html', user=db_user['username'])
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
