from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    first = StringField('Firstname',
                        validators=[DataRequired(), Length(min=2, max=20)])
    last = StringField('Lastname',
                       validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    institute = StringField('Institute', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    codechef = StringField('Codechef Handle',
                           validators=[DataRequired(), Length(min=2, max=20)])
    codeforces = StringField('Codeforces Handle',
                             validators=[DataRequired(), Length(min=2, max=20)])
    hackerrank = StringField('Hackerrank Handle',
                             validators=[DataRequired(), Length(min=2, max=20)])
    hackerearth = StringField('Hackerearth Handle',
                              validators=[DataRequired(), Length(min=2, max=20)])

    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
