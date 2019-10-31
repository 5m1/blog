from flask import Flask
from app.api import bp as api_bp
from app.extensions import cors, db, migrate


def create_app(config_class=None):
    app = Flask(__name__)
    configure_app(app, config_class)
    configure_blueprints(app)
    configure_extensions(app)
    configure_before_handlers(app)
    configure_after_handlers(app)
    configure_errorhandlers(app)
    return app

def configure_app(app, config_class):
    app.config.from_object(config_class)
    app.url_map.strict_slashes = False

def configure_blueprints(app):
    app.register_blueprint(api_bp, url_prefix='/api')

def configure_extensions(app):
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

def configure_before_handlers(app):
    '''Configures the before request handlers'''
    pass

def configure_after_handlers(app):
    '''Configures the after request handlers'''
    pass

def configure_errorhandlers(app):
    '''Configures the error handlers'''
    pass
