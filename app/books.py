from flask import Blueprint, current_app, request
from .model import Book
from .serializer import BookSchema


bp_books = Blueprint('books', __name__)

@bp_books.route("/book", methods =['GET'])
def all_books():
    bs = BookSchema(many=True)
    books = Book.query.all()
    return bs.jsonify(books), 200


@bp_books.route("/book", methods =['POST'])
def create_book():
    bs = BookSchema()
    book, error = bs.load(request.json)
    current_app.db.session.add(book)
    current_app.db.session.commit()    
    return bs.jsonify(book), 201


@bp_books.route("/book/<id>", methods =['DELETE'])
def create_book(id: int):    
    Book.query.filter(Book.id==id).delete()   
    return "", 200


@bp_books.route("/book/<id>", methods =['PUT'])
def create_book(id: int):    
    query = Book.query.filter(Book.id==id)
    query.update(request.json)
    current_app.db.sesstion.commit()
    return bs.jsonify(query.first()), 200