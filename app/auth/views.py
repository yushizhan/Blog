from . import auth
from .. import db
from ..models import *
from flask import *
from forms import RegisterForm, LoginForm

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data,
        password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("you can now login!")
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth.route('/logout')
def logout():
    pass

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            return redirect(url_for('main.index'))
        else:
            flash("account not exist!")
    return render_template("login.html", form=form)
    