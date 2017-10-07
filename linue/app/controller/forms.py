from wtforms import Form, StringField, PasswordField, SubmitField, validators

class LoginForm(Form):
    username = StringField('username', [validators.Length(min=3, max=10)])
    password = PasswordField('password', [validators.DataRequired()])
