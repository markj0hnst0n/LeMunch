import os
from os import path
from flask import Flask, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)

@app.route('/')

@app.route('/get_user')
def get_user():
    users = mongo.db.users.find()
    return render_template("profile.html", users=users)

@app.route('/add_user')
def add_user():
    return render_template("signup.html", users=mongo.db.users.find())

@app.route('/new_user', methods=['POST'])
def new_user():
    users = mongo.db.users
    users.insert_one(request.form.to_dict())
    return redirect(url_for('get_user'))

@app.route('/new_recipe')
def add_recipe():
    return render_template("add_recipe.html")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)