from flask import Blueprint, render_template, request, redirect, url_for, abort, flash
from flask_login import login_user, logout_user, login_required, current_user
from .models import Contact, User
from . import db

bp = Blueprint('main', __name__)

# Página principal: lista apenas os contatos do usuário logado
@bp.route('/')
@login_required
def index():
    contacts = Contact.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', contacts=contacts)

# Criar um novo contato
@bp.route('/create', methods=['POST'])
@login_required
def create():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    notes = request.form['notes']

    contact = Contact(
        name=name,
        email=email,
        phone=phone,
        notes=notes,
        user_id=current_user.id
    )
    db.session.add(contact)
    db.session.commit()
    return redirect(url_for('main.index'))

# Deletar contato
@bp.route('/delete/<int:id>')
@login_required
def delete(id):
    contact = Contact.query.get_or_404(id)
    if contact.user_id != current_user.id:
        abort(403)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('main.index'))

# Exibir formulário de edição
@bp.route('/edit/<int:id>', methods=['GET'])
@login_required
def edit(id):
    contact = Contact.query.get_or_404(id)
    if contact.user_id != current_user.id:
        abort(403)
    return render_template('edit_contact.html', contact=contact)

# Atualizar contato
@bp.route('/update/<int:id>', methods=['POST'])
@login_required
def update(id):
    contact = Contact.query.get_or_404(id)
    if contact.user_id != current_user.id:
        abort(403)
    contact.name = request.form['name']
    contact.email = request.form['email']
    contact.phone = request.form['phone']
    contact.notes = request.form['notes']
    db.session.commit()
    return redirect(url_for('main.index'))

# Registro de novo usuário
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if User.query.filter_by(email=email).first():
            flash('E-mail já registrado.')
            return redirect(url_for('main.register'))

        user = User(email=email, password=password)  # senha em texto plano por enquanto
        db.session.add(user)
        db.session.commit()
        flash('Registro concluído. Faça login.')
        return redirect(url_for('main.login'))

    return render_template('register.html')

# Login
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and user.password == password:  # comparação simples, sem hash
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('Credenciais inválidas.')

    return render_template('login.html')

# Logout
@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout realizado.')
    return redirect(url_for('main.login'))
