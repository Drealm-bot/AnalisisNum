from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jahshsj'

    from .views import views
    from .SNENL import SNENL

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(SNENL, url_prefix='/SNENL/')

    return app