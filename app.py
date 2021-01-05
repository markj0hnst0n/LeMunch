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

"""
Environment variables for accessing database and mail server for contact emails
sent form flask app below.
"""

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
    """
    Displays main splash page for app.  Shows some recipe examples by
    calling top 3 most liked recipes from the database.
    If the user has logged in it takes them straight to
    their profile page.
    """
    if 'user' in session:
        db_user = user_collection.find_one(
            {"username": session['user']}
            )
        if db_user:
            return redirect(url_for('profile', user=db_user['username']))
    all_recipes = list(recipe_collection.find().sort("likes", -1).limit(3))
    return render_template("index.html", all_recipes=all_recipes)


@app.route('/signin', methods=['GET'])
def signin():
    """
    Displays login page unless user already logged in.  In which case
    it will display the profile.
    """
    if 'user' in session:
        db_user = user_collection.find_one(
            {"username": session['user']}
            )
        if db_user:
            return redirect(url_for('profile', user=db_user['username']))
    else:
        return render_template("signin.html")


@app.route('/login', methods=['POST'])
def login():
    """
    Uses data entered in login form to check against database to see if
    username and password match user database.  If successful it puts a
    user in the browsing session and takes the user to their profile.
    If unsuccessful it lets the user know through a flash message.
    Uses werkzeug password hashing and salting for security.
    Uses the .lower() method to normalise any user entered data so that
    it can be checked against normalised database information.
    """
    form = request.form.to_dict()
    db_user = user_collection.find_one({"username": form['username'].lower()})
    if db_user:
        if check_password_hash(db_user['password'], form['password']):
            session['user'] = form['username'].lower()
            flash('Login successful')
            return redirect(url_for('profile', user=db_user['username']))
        else:
            flash('Username or password incorrect')
            return render_template("signin.html")
    flash("Username or password incorrect")
    return render_template("signin.html")


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    """
    Displays user registration page.  If the request method is POST
    it will add user data from the form to the database.
    Uses werkzeug password hashing and salting for security.
    If the user already exists their profile will be displayed.
    Uses the .lower() method to normalize and user entered data so
    that it is all held in the saem format in the database.
    """
    if 'user' in session:
        flash("You are already logged in")
        return redirect(url_for('profile', user=session["user"]))
    if request.method == 'POST':
        form = request.form.to_dict()
        if form['password'] == form['password1']:
            user = user_collection.find_one(
                {"username": form['username'].lower()}
                )
            if user:
                flash(f"{form['username']} already exists")
                return redirect(url_for('add_user'))
            else:
                user_collection.insert_one(
                    {
                        'username': form['username'].lower(),
                        'email': form['email'],
                        'password': generate_password_hash(form['password'])
                    }
                )
                db_user = user_collection.find_one(
                    {"username": form['username'].lower()})
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
    """
    Displays users profile page and any recipes that they have added
    sorted with the newest at the top.  If the user has not logged in
    the login page will be displayed.
    """
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
    """
    Displays information about the user which can be edited which is called
    from the database.  If the request method is post the data is updated
    adn the user receives a flash message to confirm their action.
    """
    if request.method == "POST":
        if request.form.get("password") == request.form.get("password1"):
            edit = {"$set": {
                    "username": request.form.get("username").lower(),
                    "email": request.form.get("email")
                    }}
        user_collection.update({"_id": ObjectId(user_id)}, edit)
        flash("User info updated")
        user = user_collection.find_one({"username": session["user"]})
        my_recipes = list(recipe_collection.find({"user": user})
                          .sort("datetime", -1))
        return redirect(url_for('profile', user=session["user"],
                        my_recipes=my_recipes))
    user = user_collection.find_one({"username": session["user"].lower()})
    return render_template('edit_user.html', user=user)


@app.route('/change_password/<user_id>', methods=["GET", "POST"])
def change_password(user_id):
    """
    Displays change of password form.  For security no data is filled in
    initially.  User must enter correct existing password on the database
    and the write new password twice.
    If password is successfully changed the user is notified via a flash
    message and if they have supllied any incorrect information a flash
    messsage will also notify them.
    Uses werkzeug password hashing and salting for security.
    """
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
    """
    Logs user out of browsing session and takes them back to the main splash
    page.
    """
    session.pop('user')
    flash('User Logged Out')
    return redirect(url_for('index'))


@app.route('/add_recipe', methods=["GET", "POST"])
def add_recipe():
    """
    Displays add recipe form.  If request method is POST it takes information
    from the form and adds it to the database.
    It sets the ingredients and method steps as arrays.
    Uses the .lower() method to normalize and user entered data so
    that it is all held in the same format in the database.
    A flash message lets the user know that their action has been successful.
    """
    if 'user' in session:
        if request.method == "POST":
            method_steps = request.form.getlist("method")
            method_lower = [item.lower() for item in method_steps]
            ingredients = request.form.getlist("ingredients")
            ingredients_lower = [item.lower() for item in ingredients]
            recipe = {
                "recipe_type": request.form.get("recipe_type").lower(),
                "name": request.form.get("recipe_name").lower(),
                "description": request.form.get("description").lower(),
                "picture": request.form.get("recipe_image"),
                "ingredients": ingredients_lower,
                "method": method_lower,
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
    return redirect(url_for('signin'))


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """
    Displays edit recipe form pre filled with the recipe information to
    edit. If request method is POST it takes information from the form
    and adds it to the database.
    Uses the .lower() method to normalize and user entered data so
    that it is all held in the same format in the database.
    A flash message lets the user know that their action has been successful.
    """
    if 'user' in session:
        user = user_collection.find_one({"username": session["user"]})
        if request.method == "POST":
            method_steps = request.form.getlist("method")
            method_lower = [item.lower() for item in method_steps]
            ingredients = request.form.getlist("ingredients")
            ingredients_lower = [item.lower() for item in ingredients]
            edit = {"$set": {
                "recipe_type": request.form.get("recipe_type").lower(),
                "name": request.form.get("recipe_name").lower(),
                "description": request.form.get("description").lower(),
                "picture": request.form.get("recipe_image").lower(),
                "ingredients": ingredients_lower,
                "method": method_lower,
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
                               recipe_types=recipe_types,
                               user=user,
                               ingredients=ingredients,
                               method_steps=method_steps)
    return redirect(url_for('signin'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    """
    Deletes the currently displayed recipe.  This can only be accessed
    A flash message lets the user know that their action has been successful.
    """
    if 'user' in session:
        recipe_collection.remove({"_id": ObjectId(recipe_id)})
        flash("Recipe deleted")
        return redirect(url_for('profile', user=session["user"]))
    return redirect(url_for('signin'))


@app.route('/browse_date')
def browse_date():
    """
    Displays all the recipes in the recipe data for the user to browse sorted
    with newest at the top of the page.  Custom information is dislayed if it
    is a user generated recipe.
    """
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
    """
    Displays all the recipes in the recipe data for the user to browse sorted
    with those with the most likes at the top of the page.  Custom information
    is dislayed if it is a user generated recipe.
    """
    browse = 1
    browse_like = 1
    user = user_collection.find_one({"username": session["user"]})
    all_recipes = list(recipe_collection.find().sort("likes", -1))
    return render_template('browse.html', all_recipes=all_recipes,
                           user=user,
                           browse=browse,
                           browse_like=browse_like)


@app.route('/search', methods=["GET", "POST"])
def search():
    """
    Displays all the recipes in the recipe data for the user to browse sorted
    with those with the most likes at the top of the page.
    """
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
    """
    Displays a specific recipe from the recipe collection and also calls
    the likes collection to see if the user has liked that recipe.
    """
    recipe = recipe_collection.find_one({"_id": ObjectId(recipe_id)})
    ingredients = range(0, len(recipe['ingredients']))
    method_steps = range(0, len(recipe['method']))
    if 'user' in session:
        user_like = likes_collection.find_one(
            {
                "username": session["user"],
                "recipe_id": recipe["_id"]
            }
        )
        user = user_collection.find_one({"username": session["user"]})
        return render_template('view_recipe.html', recipe=recipe,
                               ingredients=ingredients,
                               method_steps=method_steps,
                               user=user,
                               user_like=user_like,
                               recipe_user=recipe['user'])
    return render_template('view_recipe.html', recipe=recipe,
                           ingredients=ingredients,
                           method_steps=method_steps)


@app.route('/like_recipe/<recipe_id>')
def like_recipe(recipe_id):
    """
    Adds the users name and recipe id to the likes collection creating a unique
    record which can be called to check if user has liked a certain recipe.
    Also increases the number of likes a recipe has by 1.
    If the user has already liked the recipe calling this function again will
    remove the like from the likes collection and decrease the number of likes
    the recipe has by 1.
    """
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
    """
    Displays a contact form so that users can contact the site administrators.
    If the request method is post it will send an email to the administrators
    on behalf of the user with their query as defined in the form.
    """
    if request.method == 'POST':
        recipient = os.environ.get('RECIPIENT')
        sender = os.environ.get('SENDER')
        email = request.form['email']
        query = request.form['query']
        name = request.form['name']
        msg1 = Message(subject="User Query",
                       sender=(sender),
                       recipients=[recipient])
        msg1.body = f'Name: {name}.  Query: {query}.  Email: {email}.'
        mail.send(msg1)
        flash("Contact form received")
        return redirect('index')
    if 'user' in session:
        db_user = user_collection.find_one({"username": session['user']})
        if db_user:
            return render_template('contact.html', user=db_user['username'])
    return render_template('contact.html')


"""
The functions below handle and HTTP errors that may be incurred so that the user does not
leave the app if this happens.
"""


@app.errorhandler(403)
def page_not_found(error):
    if 'user' in session:
        return render_template('errors/403.html', user=session["user"]), 403
    return render_template('errors/403.html'), 403


@app.errorhandler(404)
def forbidden(error):
    if 'user' in session:
        return render_template('errors/404.html', user=session["user"]), 404
    return render_template('errors/404.html'), 404


@app.errorhandler(405)
def not_allowed(error):
    if 'user' in session:
        return render_template('errors/405.html', user=session["user"]), 405
    return render_template('errors/405.html'), 405


@app.errorhandler(500)
def internal_server(error):
    if 'user' in session:
        return render_template('errors/500.html', user=session["user"]), 500
    return render_template('errors/500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
