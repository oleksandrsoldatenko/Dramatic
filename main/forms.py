from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, Regexp, ValidationError
from wtforms.widgets import TextArea

class CommentForm(FlaskForm):
    comment = StringField('Username', validators=[DataRequired(), Length(max=150)], widget=TextArea())