from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   #means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
import pyrebase
authenticate= Blueprint('authenticate', __name__)

firebaseConfig={
  "apiKey": "AIzaSyA7GweUH8Z8Dy_eWJVz2ohpfMaKK-XNTs8",
  "authDomain": "qrbasedordering.firebaseapp.com",
  "databaseURL": "https://qrbasedordering-default-rtdb.firebaseio.com",
  "projectId": "qrbasedordering",
  "storageBucket": "qrbasedordering.appspot.com",
  "messagingSenderId": "364448122744",
  "appId": "1:364448122744:web:476bff4d8e32a9ecc26a8d",
  "measurementId": "G-3HVXNBTYDH"
}
def signup(e,passw):
   
    firebase=pyrebase.initialize_app(firebaseConfig)
    auth=firebase.auth()
    email=e
    password=passw
    ur=auth.create_user_with_email_and_password(email,password)
  
def loginF(e,passw):
    firebase=pyrebase.initialize_app(firebaseConfig)
    auth=firebase.auth()
    email=e
    password=passw
    try:
        ur=auth.sign_in_with_email_and_password(email,password)
        return render_template("home2.html")
    except:
        print("Wrong credentialss")
        return render_template("login2.html")



@authenticate.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        l=loginF(email,password)    
        return l
    return render_template("login2.html")
    


@authenticate.route('/logout')
#@login_required  #checks if user has logged in
def logout():
    logout_user()
    return redirect(url_for('authenticate.login'))


@authenticate.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        signup(email,password2)
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
           flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True) #remembers users
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("login2.html", user=current_user)



