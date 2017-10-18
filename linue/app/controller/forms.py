from wtforms import Form, StringField, PasswordField, SubmitField, validators

class LoginSignupForm(Form):
    email = StringField('email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('password', [validators.Length(min=7, max=50), validators.DataRequired()])

class competitionForm(Form):
    className = StringField('className', [validators.Length(min=3, max=50), validators.DataRequired()])
    schoolName = StringField('schoolName', [validators.Length(min=4, max=75), validators.DataRequired()])
    schoolPupilEmail = StringField('schoolPupilEmail', [validators.Email(), validators.DataRequired()])
    schoolTelephone = StringField('schoolTelephone', [validators.NumberRange(min=0, max=25), validators.DataRequired()])
