import re

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError

def validate_password_strength(form, field):
    password = field.data

    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")

    if not re.search(r"[A-Z]", password):
        raise ValidationError("Password must contain at least one uppercase letter.")

    if not re.search(r"[a-z]", password):
        raise ValidationError("Password must contain at least one lowercase letter.")

    if not re.search(r"\d", password):
        raise ValidationError("Password must contain at least one number.")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        raise ValidationError("Password must contain at least one special character.")

class RegisterForm(FlaskForm):

    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=3,max=30)]
    )

    email = StringField(
        "Email",
        validators=[DataRequired(),Email()]
    )

    password = PasswordField(
    "Password",
    validators=[
        DataRequired(),
        validate_password_strength
      ]
    )

    submit = SubmitField("Register")


class LoginForm(FlaskForm):

    email = StringField(
        "Email",
        validators=[DataRequired(),Email()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )

    submit = SubmitField("Login")