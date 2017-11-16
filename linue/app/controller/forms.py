from wtforms import Form, StringField, PasswordField, SubmitField, validators

class LoginSignupForm(Form):
    email = StringField('Email', [validators.Regexp(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'), validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=7, max=50), validators.DataRequired()])

class competitionForm(Form):
    className = StringField('Class Name', [validators.Regexp('^\w+$'), validators.Length(min=3, max=50), validators.DataRequired()])
    schoolName = StringField('School Name', [validators.Regexp('^\w+$'), validators.Length(min=4, max=75), validators.DataRequired()])
    schoolPupilEmail = StringField('School Pupil Email', [validators.Regexp(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'), validators.Email(), validators.DataRequired()])
    schoolTelephone = StringField('School Telephone', [validators.Regexp(r'^(?:\+?44)?[07]\d{9,13}$'), validators.NumberRange(min=0, max=25), validators.DataRequired()])
