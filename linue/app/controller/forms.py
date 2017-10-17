from wtforms import Form, StringField, PasswordField, SubmitField, validators

class LoginForm(Form):
    email = StringField('email', [validators.Email()])
    password = PasswordField('password', [validators.Length(min=7, max=255), validators.DataRequired()])

class SignupForm(Form):
    email = StringField('email', [validators.Email()])
    password = PasswordField('password', [validators.Length(min=7, max=255), validators.DataRequired()])
