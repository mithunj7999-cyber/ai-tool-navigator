# backend/auth.py
from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from database import db
from models import User, PromptHistory
import uuid

auth_bp = Blueprint('auth', __name__)

def init_bcrypt(bcrypt_instance):
    global bcrypt
    bcrypt = bcrypt_instance

@auth_bp.route('/api/signup', methods=['POST'])
def signup():
    data     = request.get_json() or {}
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()
    email    = data.get('email', '').strip().lower()

    if not username or not password:
        return jsonify({'error': 'Name and password are required'}), 400
    if len(password) < 6:
        return jsonify({'error': 'Password must be at least 6 characters'}), 400
    if email and User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already registered'}), 409
    if not email:
        email = f'user_{uuid.uuid4().hex[:10]}@noemail.local'

    hashed = bcrypt.generate_password_hash(password).decode('utf-8')
    user   = User(email=email, username=username, password=hashed)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    return jsonify({'success': True, 'username': user.username, 'email': user.email})

@auth_bp.route('/api/login', methods=['POST'])
def login():
    data     = request.get_json() or {}
    login_id = data.get('login_id', '').strip().lower()
    password = data.get('password', '').strip()

    if not login_id or not password:
        return jsonify({'error': 'Username/email and password are required'}), 400

    user = User.query.filter_by(email=login_id).first()
    if not user:
        user = User.query.filter_by(username=login_id).first()
    if not user or not user.password:
        return jsonify({'error': 'Invalid username/email or password'}), 401
    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid username/email or password'}), 401

    login_user(user)
    return jsonify({'success': True, 'username': user.username, 'email': user.email})

@auth_bp.route('/api/logout', methods=['POST'])
def logout():
    logout_user()
    return jsonify({'success': True})

@auth_bp.route('/api/me')
def me():
    if current_user.is_authenticated:
        display_email = '' if 'noemail.local' in current_user.email else current_user.email
        return jsonify({
            'logged_in': True,
            'username':  current_user.username,
            'email':     display_email,
            'id':        current_user.id
        })
    return jsonify({'logged_in': False})

# ── History — NO @login_required, handle manually to avoid 302 redirect ──
@auth_bp.route('/api/history', methods=['POST'])
def save_history():
    # Return 200 silently if not logged in — don't redirect
    if not current_user.is_authenticated:
        return jsonify({'success': False, 'reason': 'not logged in'}), 200

    data = request.get_json() or {}
    h = PromptHistory(
        user_id  = current_user.id,
        topic    = data.get('topic', ''),
        category = data.get('category', ''),
        prompt   = data.get('prompt', '')
    )
    db.session.add(h)
    db.session.commit()
    return jsonify({'success': True})

@auth_bp.route('/api/history', methods=['GET'])
def get_history():
    if not current_user.is_authenticated:
        return jsonify({'error': 'not logged in'}), 401

    items = PromptHistory.query \
        .filter_by(user_id=current_user.id) \
        .order_by(PromptHistory.created_at.desc()) \
        .limit(50).all()
    return jsonify([{
        'id':         h.id,
        'topic':      h.topic,
        'category':   h.category,
        'prompt':     h.prompt,
        'created_at': h.created_at.strftime('%d %b %Y, %I:%M %p')
    } for h in items])

@auth_bp.route('/api/history/<int:hid>', methods=['DELETE'])
def delete_history(hid):
    if not current_user.is_authenticated:
        return jsonify({'error': 'not logged in'}), 401
    h = PromptHistory.query.filter_by(id=hid, user_id=current_user.id).first()
    if h:
        db.session.delete(h)
        db.session.commit()
    return jsonify({'success': True})