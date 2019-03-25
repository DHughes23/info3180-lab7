from flask_wtf import FlaskForm
from wtforms import FileField, TextArea
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed

class UploadForm(FlaskForm):
    description = TextArea('Description', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
