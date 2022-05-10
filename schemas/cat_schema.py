from apiflask import APIFlask, Schema, abort
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf


class CatInSchema(Schema):
    name = String(required=True)
