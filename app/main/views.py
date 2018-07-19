from flask import render_template, session, redirect, url_for
from ..models import User, Post
from . import main
from .forms import PostForm
from .. import db

@main.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    user = None
    if 'username' in session:
        user = User.query.filter_by(username=session['username']).first()
    if user and form.validate_on_submit():
        post = Post(body=form.body.data, author=user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', current_user=user, form=form, posts=posts)

