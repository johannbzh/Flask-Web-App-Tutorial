from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/') # homepage
@login_required() # Can't access the homepage unless you're logged in
def home():
  return render_template('home.html')
