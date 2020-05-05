from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import Form, BooleanField, SubmitField, PasswordField, StringField, FloatField, IntegerField, validators
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length, NumberRange
from app.models import Users


class RegistrationForm(FlaskForm):
    username     = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password     = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=30)])
    password2    = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose different one.')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=35)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign in')

class UpdateProfileForm(FlaskForm):
    temp = FloatField('Temperature [C]', validators=[NumberRange(min=10.0, max=30.0)])
    screen = FloatField('Screen brightness [%]', validators=[NumberRange(min=0.0, max=100.0)])
    room = IntegerField('Room brightness [lx]', validators=[NumberRange(min=100, max=1000)])
    hours = FloatField('Work hours [h]', validators=[NumberRange(min=0.0, max=23.5)])
    work_minutes = IntegerField('Duration of work interval [min]', validators=[NumberRange(min=1, max=120)])
    pause_minutes = IntegerField('Duration of break [min]', validators=[NumberRange(min=1, max=60)]) 
    submit = SubmitField('Update')

class DrinkForm(FlaskForm):
    liquids = FloatField('Drink', validators=[NumberRange(min=0.0, max=10.0)])
    submit1 = SubmitField('Drink [liters]')

class EatForm(FlaskForm):
    food = IntegerField('Eat', validators=[NumberRange(min=0, max=5)])
    submit2 = SubmitField('Eat [meals]')



