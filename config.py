import os
class Config:
    '''
    General configuration parent class
    '''
    debug = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://peter:ozil@localhost/saka'
    
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    
#  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
class  DevConfig(Config):
    '''
    Development configuration child class
    Args:
         Config: The parent configuration class with General configuration settings
    '''
    SECRET_KEY = 'call'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://peter:ozil@localhost/saka'
    DEBUG = True
    ENV = 'development'
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}  