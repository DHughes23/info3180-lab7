from flask_wtf import FlaskForm
from wtforms import FileField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed

class UploadForm(FlaskForm):
    description = TextAreaField('Description', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
