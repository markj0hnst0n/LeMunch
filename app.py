import os
from os import path
from flask import Flask, flash, g, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo

if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.secret_key = 'SECRET_KEY'

mongo = PyMongo(app)

@app.route('/')
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        database_user = mongo.db.user_info.find_one({"username": request.form.get("username")})
        password = request.form.get('password')
        if database_user:
            if database_user["password"] == password:
                session["user"] = request.form.get("username")
                return redirect(url_for('profile'))
        else:
            flash("User does not exist!  Please Sign Up")
    return render_template('signupsignin.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)