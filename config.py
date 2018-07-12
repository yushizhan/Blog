class Config(object):
    pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://admin:admin@localhost/blog_dev'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://admin:admin@localhost/blog'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}