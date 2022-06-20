import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'very secret key')
    FLASK_APP = os.environ.get('FLASK_APP', 'app.py')
    FLASK_APP_HOST_ADDRESS = os.environ.get('FLASK_APP_HOST_ADDRESS', '0.0.0.0')
    FLASK_APP_HOST_PORT = os.environ.get('FLASK_APP_HOST_PORT', 5000)

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    PRODUCTION = False


class ProductionConfig(Config):
    DEBUG = False
    PRODUCTION = True


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}