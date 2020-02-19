from flask import Flask
from flask_uploads import UploadSet,configure_uploads,IMAGES
from config import config_options
from flask_login import LoginManager
from flask_mail import Mail


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

mail = Mail()

photos  = Uploadset('photos',IMAGES)
def create_app(config_name):
    app = Flask(__name__)
    
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    
    #Initializing Flask Extensions
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # configure UploadSet
    configure_uploads(app,photos)  
    
    
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app    
    