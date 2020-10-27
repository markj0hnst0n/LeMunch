import os
from os import path
from flask import Flask, flash, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)

@app.route('/')

@app.route('/signin', methods=['GET'])
def signin():
    if 'user' in session:
        db_user = mongo.db.users.find_one({"username": session['user']})
        if db_user:
            flash("You are already logged in")
            return redirect(url_for('profile.html', user=db_user['username']))
    else:
        return render_template("signin.html")

@app.route('/login', methods=['POST'])
def login():
    form = request.form.to_dict()
    db_user = mongo.db.users.find_one({"username": form['username']})
    if db_user:
        if check_password_hash(db_user['password'], form['password']):
            session['user'] = form['username']
            flash("Login successful")
            return redirect(url_for('profile', user = db_user['username']))
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
            user = mongo.db.users.find_one({"username": form['username']})
            if user:
                flash(f"{form['username']} already exists")
                return redirect(url_for('add_user'))
            else:
                mongo.db.users.insert_one(
                    {
                        'username': form['username'],
                        'picture': form['picture'],
                        'bio': form['bio'],
                        'email': form['email'],
                        'password': generate_password_hash(form['password'])
                    }
                )
                db_user = mongo.db.users.find_one({"username": form['username']})
                if db_user:
                    session['user'] = db_user['username']
                    return redirect(url_for('profile', user=db_user['username']))
                else:
                    flash('Issues saving profile')
                    return redirect(url_for('add_user'))
        else:
            flash('Passwords do not match')
            return redirect(url_for('add_user'))
    return render_template('signup.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)