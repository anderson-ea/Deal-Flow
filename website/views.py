from flask import Blueprint, render_template, request, flash, redirect
from flask.helpers import url_for
from flask_login import login_required, current_user
from .models import *
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    new_lead = Lead(user_id=current_user.id)
    if request.method == 'POST':
        db.session.add(new_lead)
        db.session.commit()
        flash('New Lead Added.', category="success")
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

@views.route('delete/<id>')
def delete(id):
    lead_to_delete = db.session.query(Lead).filter_by(user_id=current_user.id, id=id).first()
    db.session.delete(lead_to_delete)
    db.session.commit()
    return redirect(url_for('views.home'))