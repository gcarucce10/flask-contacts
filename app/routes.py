from flask import Blueprint, render_template, request, redirect, url_for
from .models import Contact
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

@bp.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    notes = request.form['notes']

    contact = Contact(name=name, email=email, phone=phone, notes=notes)
    db.session.add(contact)
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/delete/<int:id>')
def delete(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('main.index'))

# Show the edit form and handle the update
@bp.route('/edit/<int:id>', methods=['GET'])
def edit(id):
    contact = Contact.query.get_or_404(id)
    return render_template('edit_contact.html', contact=contact)

# The user can update the contact and submit the form
@bp.route('/update/<int:id>', methods=['POST'])
def update(id):
    contact = Contact.query.get_or_404(id)
    contact.name = request.form['name']
    contact.email = request.form['email']
    contact.phone = request.form['phone']
    contact.notes = request.form['notes']
    db.session.commit()
    return redirect(url_for('main.index'))