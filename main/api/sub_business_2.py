from flask import jsonify
from flask import Blueprint

bp_business2 = Blueprint("business2", __name__)


@bp_business2.route('/1')
def index():
    data = {
        "username": "rale",
        "age": 18,
        "desc": "this is test!!"
    }
    return jsonify(data)
