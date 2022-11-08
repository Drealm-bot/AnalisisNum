from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jahshsj'

    from .views import views
    from .singular import singular

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(singular, url_prefix='/singular/')

    return app