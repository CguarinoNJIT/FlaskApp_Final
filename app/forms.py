"""Form object declaration."""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextField, SubmitField, PasswordField, SelectField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, URL

class ContactForm(FlaskForm):
    """Contact form."""
    name = StringField( 'Name',[DataRequired()])
    email = StringField( 'Email',[Email(message='Not a valid email address.'),DataRequired()])
    body = TextField('Message',[DataRequired(),Length(min=4,message=('Your message is too short.'))])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')

class SignupForm(FlaskForm):
    """Sign up for a user account."""
    email = StringField('Email',[Email(message='Not a valid email address.'),DataRequired()])
    password = PasswordField('Password',[DataRequired(message="Please enter a password."),])
    confirmPassword = PasswordField('Repeat Password',[EqualTo(password, message='Passwords must match.')])
    title = SelectField('Title',[DataRequired()],choices=[
            ('Farmer', 'farmer'),
            ('Corrupt Politician', 'politician'),
            ('No-nonsense City Cop', 'cop'),
            ('Professional Rocket League Player', 'rocket'),
            ('Lonely Guy At A Diner', 'lonely'),
            ('Pokemon Trainer', 'pokemon') ])
    website = StringField('Website',validators=[URL()])
    birthday = DateField('Your Birthday')
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')