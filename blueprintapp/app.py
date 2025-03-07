from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder = 'templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./blueprints.db'
    app.secret_key = 'skfskf sfkkshfs'

    db.init_app(app)

    # import and register all blueprints here
    from blueprintapp.blueprints.core.routes import core
    from blueprintapp.blueprints.todos.routes import todos
    from blueprintapp.blueprints.user.routes import user

    app.register_blueprint(core, url_prefix = '/')
    app.register_blueprint(todos, url_prefix = '/todos')
    app.register_blueprint(user, url_prefix = '/user')

    migrate = Migrate(app, db)

    return app

