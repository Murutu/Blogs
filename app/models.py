from . import db
from . import login_manager
from datetime import datetime

class User(db.Model):
     __tablename__ = 'users'
     id = db.Column(db.Integer,primary_key = True)
     username = db.Column(db.String(255), index= True)
     email = db.Column(db.String(255),unique=True, index=True)
     bio = db.Column(db.String(5000))
     profile_pic_path = db.Column(db.String)
     pass_secure = db.Column(db.String(255))
     date_joined = db.Column(db.DateTime,default=datetime.utcnow)

     def __repr__(self):
         return f'User {self.username}'
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))