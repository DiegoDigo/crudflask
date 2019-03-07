from flask import Blueprint, current_app, request
from .model import Book
from .serializer import BookSchema


bp_books = Blueprint('books', __name__)

@bp_books.route("/mostrar", methods =['GET'])
def all_books():
    bs = BookSchema(many=True)
    books = Book.query.all()
    return bs.jsonify(books), 200


@bp_books.route("/mostrar", methods =['POST'])
def create_book():
    bs = BookSchema()
    book, error = bs.load(request.json)
    current_app.db.session.add(book)
    current_app.db.session.commit()    
    return bs.jsonify(book), 201