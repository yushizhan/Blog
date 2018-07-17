from . import main
from flask import *
from ..models import *

@main.route('/')
def index():
    # Login state
    if 'username' in session:
        user = User.query.filter_by(username=session['username']).first()
        return render_template('index.html', current_user=user)
    else:
        return render_template('index.html', current_user=None)