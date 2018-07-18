class Config(object):
    SECRET_KEY = 'yushizhan'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://blog:blog@localhost/blog_dev'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://blog:blog@localhost/blog'

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://blog:blog@localhost/blog_test'

CONFIG = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'test': TestConfig,
    'default': DevelopmentConfig
}
