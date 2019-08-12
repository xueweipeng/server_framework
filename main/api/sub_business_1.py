from flask import jsonify
from flask import Blueprint

bp_business1 = Blueprint("business1", __name__)


@bp_business1.route('/')
def index():
    data = {
        "username": "rale",
        "age": 18,
        "desc": "this is test!!"
    }
    return jsonify(data)
