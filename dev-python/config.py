import os
import random, string


class Config(object):
    CSRF_ENABLED = True
    CORS_ENABLED = False,
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None
    SQLALCHEMY_DATABASE_URI = \
            'mysql+pymysql://{user}:{password}@{host}/{database}'.format(
            user='your_username',
            password='your_password', 
            host='db-q5n2g',
            database='your_database'
        )

class DevelopmentConfig(Config):
    TESTING = False
    DEBUG = True
    IP_HOST = '0.0.0.0'
    PORT_HOST = 5005
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = '0.0.0.0'  # Aqui geralmente é um IP de um servidor na nuvem e não o endereço da máquina local
    PORT_HOST = 5000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)
  

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    IP_HOST = '0.0.0.0'  # Aqui geralmente é um IP de um servidor na nuvem e não o endereço da máquina local
    PORT_HOST = 5000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig()
}

app_active = os.getenv('FLASK_ENV')
