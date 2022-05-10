import traceback

from apiflask import APIFlask
from flask import request, jsonify, make_response
from models import create_app, db
from models.cat_model import CatModel
import json

app = create_app()

from routings import *


if __name__ == '__main__':
    while True:
        try:
            app.run(debug=True)
        except Exception:
            print(traceback.format_exc())
