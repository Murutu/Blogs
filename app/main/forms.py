from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    title= StringField('Blog title', validators=[Required()])
    content = TextAreaField('Text', validators=[Required()])
    category = SelectField('Type', choices=[('footballclubs','footballclubs blogs'),('poetry','poetry blogs'),('nostalgia','nostalgia blogs'),('artists','artists blogs')])
    submit = SubmitField('Submit')
    
class CommentForm(FlaskForm):
    text = TextAreaField('comment below:',validators=[Required()])
    submit = SubmitField('submit')    


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
