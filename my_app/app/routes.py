from flask import Blueprint, render_template, redirect, url_for, request, jsonify, flash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Interaction, Feedback, db

main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__)
chat_bp = Blueprint('chat', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@main_bp.route('/project_info')
def project_info():
    return render_template('project_info.html')

@chat_bp.route('/log_chat', methods=['POST'])
@login_required
def log_chat():
    data = request.json
    user_message = data.get("user_message")
    bot_response = data.get("bot_response")
    
    interaction = Interaction(user_message=user_message, bot_response=bot_response)
    db.session.add(interaction)
    db.session.commit()

    return jsonify({"status": "success"})

@main_bp.route('/feedback', methods=['GET', 'POST'])
@login_required
def feedback():
    if request.method == 'POST':
        feedback = request.form.get('feedback')
        feedback_entry = Feedback(username=current_user.username, feedback=feedback)
        db.session.add(feedback_entry)
        db.session.commit()
        flash('Thank you for your feedback!', 'success')
        return redirect(url_for('main.index'))
    return render_template('feedback.html')