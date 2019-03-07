from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_db(app):
    db.init_app(app)
    app.db = db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book = db.Column(db.String(255))
    writer = db.Column(db.String(255))
