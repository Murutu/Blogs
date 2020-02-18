from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

photos  = Uploadset('photos',IMAGES)
def create_app(config_name):
    app = Flask(__name__)
    
#Initializing Flask Extensions
login_manager.init_app(app)
mail.init_app(app)

# configure UploadSet
connfigure_uploads(app,photos)  
    
    
# Registering the blueprint
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)    
    