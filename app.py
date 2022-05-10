import traceback

from apiflask import APIFlask
from flask import request, jsonify, make_response
from models import create_app, db
from models.cat_model import Cat
from models.user_model import User
from models.comment_model import Comment
from models.post_model import Post
import json

app = create_app()

from routings import *


if __name__ == '__main__':
    while True:
        try:
            app.run(debug=True)
        except Exception:
            print(traceback.format_exc())
