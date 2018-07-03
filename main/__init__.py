from flask import Flask


def register_route(app):
    from main.api.sub_business_1 import bp_business1
    app.register_blueprint(bp_business1, url_prefix='/business1')
    from main.api.sub_business_2 import bp_business2
    app.register_blueprint(bp_business2, url_prefix='/business2')
    return app


application = Flask(__name__)
app = register_route(application)

