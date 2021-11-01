from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .models import *

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    my_user = str(current_user.id)
    exc_string = "SELECT * FROM lead WHERE user_id='"+ my_user +"'"
    data = db.engine.execute(exc_string)
    return render_template('home.html', user=current_user, data=data)

@views.route('/leads/<id>', methods=['GET', 'POST'])
def leads(id):
    current_lead = db.session.query(Lead).filter_by(user_id=current_user.id, id=id).first()
    # if request.method == 'POST':
    #     pass
    return render_template('leads.html', user=current_user, id=current_lead)