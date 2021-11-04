from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import *
from . import db

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)

@views.route('/leads/<id>', methods=['GET', 'POST'])
@login_required
def leads(id):
    current_lead = db.session.query(Lead).filter_by(user_id=current_user.id, id=id).first()
    if request.method == 'POST':

        name = request.form.get('name')
        email = request.form.get('email')
        source = request.form.get('source')
        model = request.form.get('model')
        phone = request.form.get('phone')
        last = request.form.get('last')
        stage = request.form.get('stage')
        note = request.form.get('note')
        
        
        current_lead.name = name
        current_lead.email = email
        current_lead.source = source
        current_lead.model = model
        current_lead.phone = phone
        current_lead.last = last
        current_lead.stage = stage
        current_lead.notes = note

        db.session.commit()

        flash('Changes Saved.', category='success')

    return render_template('leads.html', user=current_user, id=current_lead)