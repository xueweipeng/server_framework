from main import app
from flask import jsonify


@app.route('/')
def index():
    data = {
        "username": "rale",
        "age": 18,
        "desc": "this is test!!"
    }
    return jsonify(data)
