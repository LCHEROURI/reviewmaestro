import os
import sys

# Keep local imports working when the app is run with `python src/main.py`.
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory
from flask_cors import CORS
from src.models.user import db
from src.routes.user import user_bp
from src.routes.restaurant import restaurant_bp
from src.routes.review import review_bp
from src.routes.response import response_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))

secret_key = os.environ.get('SECRET_KEY')
is_production = os.environ.get('FLASK_ENV') == 'production'

if not secret_key:
    if is_production:
        raise RuntimeError('SECRET_KEY must be set in production')
    secret_key = 'dev-only-secret-change-me'

app.config['SECRET_KEY'] = secret_key

cors_origins = os.environ.get('CORS_ORIGINS')
if cors_origins:
    CORS(app, origins=[origin.strip() for origin in cors_origins.split(',') if origin.strip()])
elif is_production:
    CORS(app, origins=[])
else:
    CORS(app)

app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(restaurant_bp, url_prefix='/api')
app.register_blueprint(review_bp, url_prefix='/api')
app.register_blueprint(response_bp, url_prefix='/api')

database_url = os.environ.get('DATABASE_URL')
if not database_url:
    database_dir = os.path.join(os.path.dirname(__file__), 'database')
    os.makedirs(database_dir, exist_ok=True)
    database_url = f"sqlite:///{os.path.join(database_dir, 'app.db')}"

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
        return "Static folder not configured", 404

    if path and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)

    index_path = os.path.join(static_folder_path, 'index.html')
    if os.path.exists(index_path):
        return send_from_directory(static_folder_path, 'index.html')

    return "index.html not found", 404


if __name__ == '__main__':
    app.run(
        host=os.environ.get('HOST', '0.0.0.0'),
        port=int(os.environ.get('PORT', 5000)),
        debug=os.environ.get('FLASK_DEBUG', 'false').lower() == 'true',
    )
