import os
import datetime
from os import path
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)

# Collections

user_collection = mongo.db.users
recipe_collection = mongo.db.recipes
type_collection = mongo.db.recipe_types


@app.route('/')
@app.route('/signin', methods=['GET'])
def signin():
    if 'user' in session:
        db_user = user_collection.find_one({"username": session['user']})
        if db_user:
            flash("You are already logged in")
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
            return redirect(url_for('profile', user=db_user['username']))
        else:
            flash('Username or password incorrect')
            return redirect(url_for('signin'))


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if 'user' in session:
        flash("You are already logged in")
        return redirect(url_for('profile'))
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
    my_recipes = list(recipe_collection.find({"user": user})
                      .sort("datetime", -1))
    recipe_count = len(my_recipes)
    if 'user' in session:
        return render_template('profile.html',
                               user=username, my_recipes=my_recipes,
                               recipe_count=recipe_count)
    return redirect(url_for('signin'))


@app.route('/logout', )
def logout():
    session.pop('user')
    flash('User Logged Out')
    return redirect(url_for('signin'))


@app.route('/add_recipe', methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_type": request.form.get("recipe_type"),
            "name": request.form.get("recipe_name"),
            "description": request.form.get("description"),
            "picture": request.form.get("recipe_image"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "user": session["user"],
            "datetime": datetime.datetime.now().timestamp()
        }
        recipe_collection.insert_one(recipe)
        flash("Recipe Added to Your Cookbook!")
        return redirect(url_for('profile', user=session["user"]))
    recipe_types = type_collection.find().sort("type_name", 1)
    return render_template('add_recipe.html', recipe_types=recipe_types)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        edit = {
            "recipe_type": request.form.get("recipe_type"),
            "name": request.form.get("recipe_name"),
            "description": request.form.get("description"),
            "picture": request.form.get("recipe_image"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "user": session["user"],
            "datetime": datetime.datetime.now().timestamp()
        }
        recipe_collection.update({"_id": ObjectId(recipe_id)}, edit)
        flash("Recipe Edited")
        return redirect(url_for('profile', user=session["user"]))

    recipe = recipe_collection.find_one({"_id": ObjectId(recipe_id)})
    recipe_types = type_collection.find().sort("type_name", 1)
    return render_template('edit_recipe.html', recipe=recipe, recipe_types=recipe_types)


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    recipe_collection.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe deleted")
    return redirect(url_for('profile', user=session["user"]))


@app.route('/browse')
def browse():    
    all_recipes = list(recipe_collection.find().sort("datetime", -1))
    return render_template('browse.html', all_recipes=all_recipes)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
