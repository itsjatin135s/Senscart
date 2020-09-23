from flask import render_template, redirect, url_for, flash,request,current_app
import os
from forms import RegistrationFrom, LoginForm
from models import User
from __init__ import bcrypt, db, app
from flask_login import login_user, logout_user, login_required, current_user,LoginManager,UserMixin
from search.amazonoff import amzoff
from search.snapdealoff import snapoff
from search.flipkartoff import flipoff
from search.flipkart import flipkart
from search.amazon import amazon
from search.snapdeal import snapdeal


@app.route('/')
def home():
    data1 = amzoff()
    photo,title1,productlink,discount = snapoff()
    data=flipoff()
    return render_template('index.html', data1=data1,data=data,data2=zip(photo,title1,productlink,discount))




@app.route('/compare/<string:id>')
def details(id):
    flipdata=flipkart(id)
    amzdata=amazon(id)
    snapdata=snapdeal(id)
    return render_template('shop.html',flipdata=flipdata,amzdata=amzdata,snapdata=snapdata)


@app.route('/compared/PersonalisedForYou',methods=['POST'])
def compare():
    query = request.form['query']
    id=query
    flipdata=flipkart(query)
    amzdata=amazon(query)
    snapdata=snapdeal(query)
    return render_template('shop.html',flipdata=flipdata,amzdata=amzdata,snapdata=snapdata)



@app.route('/signup', methods=['Get','POST'])
def SignUp():
    if current_user.is_authenticated:

        return redirect(url_for('home'))
    #if request.method == 'GET' :
     #   return redirect(url_for('home'))
    form = RegistrationFrom()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hash_pw)
        db.session.add(user)
        db.session.commit()
        #flash('hurreey account created','success')
        return redirect(url_for('home'))

    return render_template('signup.html', form=form)


@app.route('/SignIn', methods=['GET','POST'])
def SignIn():

    if current_user.is_authenticated:

        return redirect(url_for('home'))
    #if request.method == 'GET' :
     #   return redirect(url_for('home'))
    form = LoginForm()
    # if form.validate_on_submit():

    user = User.query.filter_by(email=form.email.data).first()

    if user and bcrypt.check_password_hash(user.password, form.password.data):

        login_user(user, remember=form.remember.data)
        # flash('hurreey login success', 'success')
        return redirect(url_for('home'))
    return render_template('signin.html', form=form)


@app.route("/SignOut")
@login_required
def SignOut():
    logout_user()
    return redirect(url_for('home'))


@app.route('/error')
def error():
    return render_template('error.html')
