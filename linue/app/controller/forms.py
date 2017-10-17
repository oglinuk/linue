from wtforms import Form, StringField, PasswordField, SubmitField, validators

class LoginForm(Form):
    email = StringField('email', [validators.Email()])
    password = PasswordField('password', [validators.DataRequired()])

class SignupForm(Form):
    username = StringField('username', [validators.Length(min=3, max=10)])
    password = PasswordField('password', [validators.DataRequired()])
    email = StringField('email', [validators.Email()])
