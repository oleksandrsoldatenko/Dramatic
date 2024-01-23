from flask import render_template, redirect
from app.extensions import db
from database.user import User
from . import auth

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    from .forms import RegisterForm
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username = form.username.data,
                    email = form.email.data,
                    password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    return render_template('auth/signup.html', form=form)

@auth.route("/login", methods=["GET", "POST"])
def login():
    from .forms import LoginForm
    from flask_login import login_user
    from flask_sqlalchemy import session
    form = LoginForm()
    # print(User.query.all())
    if form.validate_on_submit():
        db_user = User.query.filter_by(username=form.username.data).first()
        if not db_user or db_user.password != form.password.data:
            return render_template('login.html', form=form, error='Invalid username or password')
        print(db_user)
        session.permanent = True
        login_user(db_user, remember=form.rememberme.data)
        print("logined: "+str(db_user))
        return redirect('/')
    return render_template('auth/login.html', form=form)