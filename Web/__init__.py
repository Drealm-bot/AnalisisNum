from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jahshsj'

    from .views import views
    from .singular import singular
    from .multiple import multiple

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(singular, url_prefix='/singular/')
    app.register_blueprint(multiple, url_prefix='/multiple/')

    return app