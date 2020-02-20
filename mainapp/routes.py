from flask import render_template, redirect, url_for, flash
from mainapp.forms import RegistrationFrom, LoginForm
from mainapp.models import User
from mainapp.__init__ import bcrypt, db, app
from flask_login import login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from mainapp.index_img import change_img, change_img1


# routes for index,register,login,logout,error...

@app.route('/')
def home():
    img1 = change_img()
    img2 = change_img1()
    
    return render_template('index.html', img=img1, img1=img2)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
       
        return redirect(url_for('home'))
    form = RegistrationFrom()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hash_pw)
        db.session.add(user)
        db.session.commit()
        #flash('hurreey account created','success')
        return redirect(url_for('login'))

    return render_template('sign_up.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        
        return redirect(url_for('home'))
    form = LoginForm()
    # if form.validate_on_submit():

    user = User.query.filter_by(email=form.email.data).first()

    if user and bcrypt.check_password_hash(user.password, form.password.data):

        login_user(user, remember=form.remember.data)
        flash('hurreey login success', 'success')
        return redirect(url_for('home'))
    return render_template('sign_in.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/error')
def error():
    return render_template('error.html')
