from . import db
from . import login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
     __tablename__ = 'users'
     id = db.Column(db.Integer,primary_key = True)
     username = db.Column(db.String(255), index= True)
     email = db.Column(db.String(255),unique=True, index=True)
     bio = db.Column(db.String(5000))
     profile_pic_path = db.Column(db.String)
     pass_secure = db.Column(db.String(255))
     date_joined = db.Column(db.DateTime,default=datetime.utcnow)
     
     blogs = db.relationship('Blog',backref = 'user', lazy='dynamic')

     def __repr__(self):
         return f'User {self.username}'
     
@property
def password(self):
    raise AttributeError('You cannot read the password attribute')

@password.setter
def password(self, password):
    self.pass_secure = generate_password_hash(password)
    
def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)         
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))