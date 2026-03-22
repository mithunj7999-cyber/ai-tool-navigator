# backend/app.py
# Run: python app.py
# Flask is configured to serve HTML from ../frontend/pages
# and static files (css/js) from ../frontend/

import os
import sys

# Allow imports from backend/ folder when running app.py directly
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask
from routes import register_routes

# Point Flask at the frontend folder for templates and static files
FRONTEND_DIR = os.path.join(os.path.dirname(__file__), '..', 'frontend')

app = Flask(
    __name__,
    template_folder=os.path.join(FRONTEND_DIR, 'pages'),
    static_folder=FRONTEND_DIR,
    static_url_path='',
)

register_routes(app)

if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "true").lower() == "true"
    app.run(debug=debug)
