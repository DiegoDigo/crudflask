from flask  import Flask 
from .model import create_db
from .serializer import create_serializer
from flask_migrate import Migrate
from .books import bp_books


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/crudizin.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    create_db(app)
    Migrate(app, app.db)
    create_serializer(app)
    
    app.register_blueprint(bp_books)
    return app