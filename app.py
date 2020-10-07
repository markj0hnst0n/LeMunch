import os
from os import path
from flask import Flask, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo

if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['secret_key'] = os.environ.get('secret_key')
app.secret_key = 'secret_key'

mongo = PyMongo(app)

@app.route('/')
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.pop('user_id', None)
        database_user = mongo.db.user_info.find_one(
            {"username": request.form.get("username")}
        )
        user = request.form.get('username')
        database_password = mongo.db.user_info.find_one(
            {"password": request.form.get("password")}
        )
        password = request.form.get('password')

        if user == database_user:
            if password == database_password:
                session["user_id"] = mongo.db.user_info.find_one('username')
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