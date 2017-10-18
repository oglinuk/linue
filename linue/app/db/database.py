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
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def get_db():
	return db

# mapping of tblUserInformation
class tblUserInformation(db.Model):
	__tablename__ = 'tblUserInformation'
	userID = db.Column('_userID', db.Integer, primary_key=True, nullable=False)
	userFirstName = db.Column('_userFirstName', db.String(50))
	userLastName = db.Column('_userLastName', db.String(50))
	userEmail = db.Column('_userEmail', db.String(50), nullable=False)
	userPassword = db.Column('_userPassword', db.String(50), nullable=False)
	userDOB = db.Column('_userDOB', db.DateTime)
	userPhone = db.Column('_userPhone', db.String(15))
	userType = db.Column('_userType', db.String(50))
	userOrganization = db.Column('_userOrganization', db.String(50))
	userJoinDate = db.Column('_userJoinDate', db.DateTime)
	userCompAnsID = db.relationship('tblUserCompAnswers', backref='userInformation', lazy=True)

	def __init__(self, prUserName = None, prUserFName = None, prUserLName = None, prUserEmail = None, prUserPass = None, prUserDOB = None, prUserPhone = None, prUserType = None, prUserOrg = None, prUserJoinDate = None):
		self.userName = prUserName
		self.userFirstName = prUserFName
		self.userLastName = prUserLName
		self.userEmail = prUserEmail
		self.userPassword = prUserPass
		self.userDOB = prUserDOB
		self.userPhone = prUserPhone
		self.userType = prUserType
		self.userOrganization = prUserOrg
		self.userJoinDate = prUserJoinDate

# sub-class of tblUserInformation that is specifically for registereing a new user
class NewUser(tblUserInformation):
	def __init__(self, prUserEmail, prUserPass):
		super(self.__class__, self).__init__(self.userEmail, self.userPassword)
		self.userEmail = prUserEmail
		self.userPassword = prUserPass

# mapping of tblUserProgress
class tblUserProgress(db.Model):
	__tablename__ = 'tblUserProgress'
	userProgressID = db.Column('_userProgressID', db.Integer, primary_key=True, nullable=False)
	userID = db.Column('_userID', db.Integer, db.ForeignKey('tblUserInformation.userID'))
	userProgressType = db.Column('_userProgressType', db.String(50))
	userProgressStartDate = db.Column('_userStartDate', db.DateTime)
	userProgressCompletionDate = db.Column('_userCompletionDate', db.DateTime)

	def __init__(self, prUserProgressType, prUserProgressStartDate, prUserProgressCompletionDate):
		self.userProgressType = prUserProgressType
		self.userProgressStartDate = prUserProgressStartDate
		self.userProgressCompletionDate = prUserProgressCompletionDate

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

	def __init__(self, prUserResponseID, prUserComment, prTutorialPage, prTutorialTopic, prModStatus):
		self.userResponseID = prUserResponseID
		self.userComment = prUserComment
		self.tutorialPage = prTutorialPage
		self.tutorialTopic = prTutorialTopic
		self.modStatus = prModStatus

# mapping of tblCompQuestions
class tblCompQuestions(db.Model):
	__tablename__ = 'tblCompQuestions'
	questionID = db.Column('_questionID', db.Integer, primary_key=True, nullable=False)
	questionText = db.Column('_questionText', db.String(100))
	ansID = db.relationship('tblCompQuestionAns', backref='compQuestion', lazy=True)
	userCompAnsID = db.relationship('tblUserCompAnswers', backref='compQuestion', lazy=True)

	def __init__(self, prQuestionText=None):
		self.questionText = prQuestionText

# mapping of tblCompQuestionAns
class tblCompQuestionAns(db.Model):
	__tablename__ = 'tblCompQuestionAns'
	competitionQuestionAnsID = db.Column('_competitionQuestionAnsID', db.Integer, primary_key=True, nullable=False)
	questionID = db.Column('_questionID', db.Integer, db.ForeignKey('tblCompQuestions._questionID'))
	questionAnswer1 = db.Column('_questionAnswer1', db.String(100))
	questionAnswer2 = db.Column('_questionAnswer2', db.String(100))
	questionAnswer3 = db.Column('_questionAnswer3', db.String(100))
	questionCorrectAns = db.Column('_questionCorrectAns', db.String(100))
	userCompAnsID = db.relationship('tblUserCompAnswers', backref='compQuestionAns', lazy=True)

	def __init__(self, prAnsID, prQuestionAns1, prQuestionAns2, prQuestionAns3, prQuestionCorrectAns):
		self.questionID = prAnsID
		self.questionAnswer1 = prQuestionAns1
		self.questionAnswer2 = prQuestionAns2
		self.questionAnswer3 = prQuestionAns3
		self.questionCorrectAns = prQuestionCorrectAns

# mapping of tblUserCompAnswers
class tblUserCompAnswers(db.Model):
	__tablename__ = 'tblUserCompAnswers'
	userAnsID = db.Column('_userAnsID', db.Integer, primary_key=True, nullable=False)
	userID = db.Column('_userID', db.Integer, db.ForeignKey('tblUserInformation._userID'))
	questionID = db.Column('_questionID', db.Integer, db.ForeignKey('tblCompQuestions._questionID'))
	competitionQuestionAnsID = db.Column('_competitionQuestionAnsID', db.Integer, db.ForeignKey('tblCompQuestionAns._competitionQuestionAnsID'))
	userQuestion1Ans = db.Column('_userQuestion1Ans', db.String(100))
	userQuestion2Ans = db.Column('_userQuestion2Ans', db.String(100))
	userQuestion3Ans = db.Column('_userQuestion3Ans', db.String(100))
	userClassName = db.Column('_userClassName', db.String(50))
	userSchoolName = db.Column('_userSchoolName', db.String(75))
	userSchoolEmail = db.Column('_userSchoolEmail', db.String(50))
	userSchoolPhone = db.Column('_userSchoolPhone', db.String(25))

	def __init__(self, prQuestion1Ans, prQuestion2Ans, prQuestion3Ans, prClassName, prSchoolName, prSchoolEmail, prSchoolPhone):
		self.userQuestion1Ans = prQuestion1Ans
		self.userQuestion2Ans = prQuestion2Ans
		self.userQuestion3Ans = prQuestion3Ans
		self.userClassName = prClassName
		self.userSchoolName = prSchoolName
		self.userSchoolEmail = prSchoolEmail
		self.userSchoolPhone = prSchoolPhone
