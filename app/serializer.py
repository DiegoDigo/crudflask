from flask_marshmallow import Marshmallow
from .model import Book

ma = Marshmallow()

def create_serializer(app):
    ma.init_app(app)


class BookSchema(ma.ModelSchema):
    class Meta:
        model = Book