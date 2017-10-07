'''
Database table mapping for linue
	-- tblUserInformation
    -- tblUserProgress
    -- tblUserComments
    -- tblCompQuestions
    -- tblCompQuestionAns
    -- tblUserCompAnswers
'''

from app import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ad46ws85qe79@localhost:3306/webdb'
db = SQLAlchemy(app)

# mapping of tblUserInformation
class tblUserInformation(db.Model):
	__tablename__ = 'tblUserInformation'
	userID = db.Column('_userID', db.Integer, primary_key=True, nullable=False)
	userFirstName = db.Column('_userFirstName', db.String(50), nullable=False)
	userLastName = db.Column('_userLastName', db.String(50), nullable=False)
	userEmail = db.Column('_userEmail', db.String(50), nullable=False)
	userPassword = db.Column('_userPassword', db.String(50), nullable=False)
	userDOB = db.Column('_userDOB', db.DateTime)
	userPhone = db.Column('_userPhone', db.String(15))
	userType = db.Column('_userType', db.String(50))
	userOrganization = db.Column('_userOrganization', db.String(50))
	userJoinDate = db.Column('_userJoinDate', db.DateTime)

	def __init__(self, userfname=None, userlname=None, useremail=None, userpass=None, userdob=None, userphone=None, usertype=None, userorg=None, userjoindate=None):
		self.userFirstName = userfname
		self.userLastName = userlname
		self.userEmail = useremail
		self.userPassword = userpass
		self.userDOB = userdob
		self.userPhone = userphone
		self.userType = usertype
		self.userOrganization = userorg
		self.userJoinDate = userjoindate

# sub-class of tblUserInformation that is specifically for registereing a new user
class NewUser(tblUserInformation):
	def __init__(self, useremail, userpass):
		super(self.__class__, self).__init__(self.userEmail, self.userPassword)
		self.userEmail = useremail
		self.userPassword = userpass

# mapping of tblUserProgress
class tblUserProgress(db.Model):
	__tablename__ = 'tblUserProgress'
	userProgressID = db.Column('_userProgressID', db.Integer, primary_key=True, nullable=False)
	userID = db.Column('_userID', db.Integer, db.ForeignKey('tblUserInformation.userID'))
	userProgressType = db.Column('_userProgressType', db.String(50))
	userProgressStartDate = db.Column('_userStartDate', db.DateTime)
	userProgressCompletionDate = db.Column('_userCompletionDate', db.DateTime)

# mapping of tblUserComments
class tblUserComments(db.Model):
	__tablename__ = 'tblUserComments'
	userCommentID = db.Column('_userCommentID', db.Integer, primary_key=True, nullable=False)
	userResponseID = db.Column('_userResponseID', db.Integer)
	userInfoID = db.Column('_userInfoID', db.Integer, db.ForeignKey('tblUserInformation.userID'))
	userComment = db.Column('_userComment', db.String(255))
	tutorialPage = db.Column('_tutorialPage', db.Integer)
	tutorialTopic = db.Column('_tutorialTopic', db.String(50))
	modStatus = db.Column('_modStatus', db.Boolean)

# mapping of tblCompQuestions
class tblCompQuestions(db.Model):
	__tablename__ = 'tblCompQuestions'
	questionID = db.Column('_questionID', db.Integer, primary_key=True, nullable=False)
	questionText = db.Column('_questionText', db.String(255))

	def __init__(self, prQuestionText):
		self.questionText = prQuestionText

# mapping of tblCompQuestionAns
class tblCompQuestionAns(db.Model):
	__tablename__ = 'tblCompQuestionAns'
	competitionQuestionAnsID = db.Column('_competitionQuestionAnsID', db.Integer, primary_key=True, nullable=False)
	questionID = db.Column('_questionID', db.Integer, db.ForeignKey('tblCompQuestions.questionID'))
	questionAnswer1 = db.Column('_questionAnswer1', db.String(100))
	questionAnswer2 = db.Column('_questionAnswer2', db.String(100))
	questionAnswer3 = db.Column('_questionAnswer3', db.String(100))
	questionCorrectAns = db.Column('_questionCorrectAns', db.Boolean)

# mapping of tblUserCompAnswers
class tblUserCompAnswers(db.Model):
	__tablename__ = 'tblUserCompAnswers'
	userAnsID = db.Column('_userAnsID', db.Integer, primary_key=True, nullable=False)
	userID = db.Column('_userID', db.Integer, db.ForeignKey('tblUserInformation.userID'))
	questionID = db.Column('_questionID', db.Integer, db.ForeignKey('tblCompQuestions.questionID'))
	competitionQuestionAnsID = db.Column('_competitionQuestionAnsID', db.Integer, db.ForeignKey('tblCompQuestionAns.competitionQuestionAnsID'))
	userQuestion1Ans = db.Column('_userQuestion1Ans', db.String(100))
	userQuestion2Ans = db.Column('_userQuestion2Ans', db.String(100))
	userQuestion3Ans = db.Column('_userQuestion3Ans', db.String(100))
	userClassName = db.Column('_userClassName', db.String(50))
	userSchoolName = db.Column('_userSchoolName', db.String(75))
	userSchoolEmail = db.Column('_userSchoolEmail', db.String(50))
	userSchoolPhone = db.Column('_userSchoolPhone', db.String(25))
