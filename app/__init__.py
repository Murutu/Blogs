from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    
#Initializing Flask Extensions
login_manager.init_app(app)    
    
    
# Registering the blueprint
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)    
    