# backend/app.py
import os, sys
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from database import init_db, db
from models import User
from routes import register_routes
from auth import auth_bp, init_bcrypt

BASE_DIR     = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.normpath(os.path.join(BASE_DIR, '..', 'frontend'))

app = Flask(
    __name__,
    template_folder=os.path.join(FRONTEND_DIR, 'pages'),
    static_folder=FRONTEND_DIR,
    static_url_path='',
)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'aitool-secret-2024')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # disable static file caching in dev

bcrypt        = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = None  # disable auto redirect — handle manually

init_bcrypt(bcrypt)
init_db(app)

@login_manager.user_loader
def load_user(user_id):
    # Fix SQLAlchemy 2.0 warning
    return db.session.get(User, int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    # Return JSON instead of redirect for API calls
    from flask import request, jsonify, redirect
    if request.path.startswith('/api/'):
        return jsonify({'error': 'not logged in'}), 401
    return redirect('/login')

app.register_blueprint(auth_bp)
register_routes(app)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)