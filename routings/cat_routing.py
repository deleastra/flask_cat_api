from flask import jsonify, request

from __main__ import app

from models import db
from models.cat_model import CatModel

from schemas.cat_schema import CatInSchema


@app.route('/cat', methods=['POST'])
@app.input(CatInSchema(partial=True))
def create_cat():
    json_data = request.get_json()
    print(json_data)
    if 'name' in json_data.keys():
        cat = CatModel(json_data['name'])
        db.session.add(cat)
        db.session.commit()
        db.session.flush()
        json_data['id'] = cat.id
        return jsonify(success=True, data=json_data, http_code=200)
    else:
        return jsonify(success=False, data=json_data, http_code=400)


@app.route('/cats')
def get_cats():
    all_cat = CatModel.query.all()
    cat_list = []
    for cat in all_cat:
        cat_dict = {'id': cat.id, 'name': cat.name}
        cat_list.append(cat_dict)
    return jsonify(success=True, data=cat_list, http_code=200)


@app.route('/cat/<int:cat_id>')
def get_cat_by_id(cat_id):
    try:
        cat = CatModel.query.filter_by(id=cat_id).first()
        cat = {'id': cat.id, 'name': cat.name}
        return jsonify(success=True, data=cat, http_code=200)
    except AttributeError:
        return jsonify(success=True, data={}, http_code=200)
