from flask import jsonify
from flask import Blueprint
from flask import request

upgrade = Blueprint("upgrade", __name__)


@upgrade.route('/check', methods=['GET'])
def check_upgrade():
    version = request.args.get('version')
    data = {
        "data": {
            "version": 1111,
            "url": "aaaaaa"
        },
        "code": 200,
        "message": "success"
    }
    return jsonify(data)
