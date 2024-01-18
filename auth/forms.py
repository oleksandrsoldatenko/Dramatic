from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, Regexp, ValidationError

def validate_username(form, username):
    from database import User
    user = User.query.filter_by(username=username.data).first()
    if user:
        raise ValidationError("username already in use")
    
def validate_email(form, email):
    from database import User
    user = User.query.filter_by(email=email.data).first()
    if user:
        raise ValidationError("email already in use")
    
    
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=15), validate_username])
    email = EmailField('Email', validators=[DataRequired(), Email(), Regexp(r".+@gmail\.com"), validate_email])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=30), Regexp(r"(?=.*[a-z])(?=.*[A-Z]+)(?=.*\d)(?=.*[!@#$%&._/])[a-zA-Z\d!@#$%&._/]{8,}", message="Password must contain at least\n one uppercase character\n one lowercase characters one special character and one number")])
    checkbox = BooleanField('I Agree to Privacy Policy', validators=[DataRequired()])
    
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=15)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=30), Regexp(r"(?=.*[a-z])(?=.*[A-Z]+)(?=.*\d)(?=.*[!@#$%&._/])[a-zA-Z\d!@#$%&._/]{8,}", message="Password must contain at least\n one uppercase character\n one lowercase characters one special character and one number")])
    checkbox = BooleanField('I Agree to Privacy Policy', validators=[DataRequired()])
    rememberme = BooleanField('Remember me')
    