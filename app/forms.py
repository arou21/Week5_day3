from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, EqualTo

class UserCreationForm(FlaskForm):
    first_name = StringField("first_name", validators = [DataRequired()])
    last_name = StringField("last_name", validators = [DataRequired()])
    user_name = StringField("user_name", validators = [DataRequired()])
    email = StringField("Email", validators = [DataRequired()])
    password = PasswordField("Password", validators = [DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField()

class LoginForm(FlaskForm):
    email = StringField("Email", validators = [DataRequired()])
    password = PasswordField("Password", validators = [DataRequired()])
    submit = SubmitField()

class PoknameForm(FlaskForm):
    pokname = StringField("first_name", validators = [DataRequired()])
    pokname = StringField("last_name", validators = [DataRequired()])
    submit = SubmitField()

class ProfileForm(FlaskForm):
    first_name = StringField("first_name", validators = [DataRequired()])
    last_name = StringField("last_name", validators = [DataRequired()])
    gender = StringField("gender", validators = [DataRequired()])
    age = IntegerField("age", validators = [DataRequired()])
    submit = SubmitField(label="Update")

class CatchForm(FlaskForm):
    pokname = StringField("first_name", validators = [DataRequired()])
    submit = SubmitField(label="Catch")

