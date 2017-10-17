'''
linue db access layer
'''
import random
import app.db.database as database
from app.db.database import tblUserInformation, NewUser, tblUserProgress, tblUserComments, tblCompQuestions, tblCompQuestionAns, tblUserCompAnswers
#from flask_sqlalchemy import SQLAlchemy


class dalObject(object):
    """The 1 containing object with methods interacting with the database"""
    def __init__(self):
        self.db = database.get_db()
        self.database = self.db.create_all()
        self.db.session.commit()
        self.tblUserInfomation = tblUserInformation
        self.tblNewUser = NewUser
        self.tblUserProgress = tblUserProgress
        self.tblUserComments = tblUserComments
        self.tblCompQuestions = tblCompQuestions
        self.tblCompQuestionAns = tblCompQuestionAns
        self.tblUserCompAnswers = tblUserCompAnswers
        print('[LINUE] DATABASE SUCCESSFULLY MAPPED [LINUE]')

    ###### db functions ######


    ###### CRUD Statements ######

    # Create statements
    def cUserInformation(self, prFName, prLName, prEmail, prPassword, prDOB, prPhone, prType, prOrganization, prJoinDate):
        try:
            # Insert statement
            row = tblUserInformation(rFName, prLName, prEmail, prPassword, prDOB, prPhone, prType, prOrganization, prJoinDate)

            # Commit
            self.db.session.add(row)
            self.db.session.commit()
        except Exception as e:
            print(str(e) + '# cUserInformation')
            return str(e) + '# cUserInformation'

    def cNewUser(self, prUserName, prEmail, prPassword):
        # Insert statement
        row = NewUser(prUserName, prEmail, prPassword)

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def cUserProgress(self, prProgressType, prProgressStartDate, prProgressCompletionDate):
        # Insert statement
        row = tblUserProgress(prProgressType, prProgressStartDate, prProgressCompletionDate)

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def cUserComments(self, prComment, prTutorialPage, prTutorialTopic, prModStatus):
        # Insert statement
        row = tblUserComments(prComment, prTutorialPage, prTutorialTopic, prModStatus)

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def cCompQuestions(self, prQuestionText):
        # Insert statement
        row = tblCompQuestions(prQuestionText)

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def cCompQuestionAns(self, prQuestionID, prQuestionAns1, prQuestionAns2, prQuestionAns3, prQuestionCorrectAns):
        # Insert statement
        row = tblCompQuestionAns(prQuestionID, prQuestionAns1, prQuestionAns2, prQuestionAns3, prQuestionCorrectAns)

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def cUserCompAnswers(self, prQuestion1Ans, prQuestionAns2, prQuestionAns3, prClassName, prSchoolName, prSchoolEmail, prSchoolPhone):
        # Insert statement
        row = tblUserCompAnswers(prQuestion1Ans, prQuestionAns2, prQuestionAns3, prClassName, prSchoolName, prSchoolEmail, prSchoolPhone)

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    # Retrieve statements
    def rUserInformation(self):
        # Insert statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def rUserProgress(self):
        # Insert statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def rUserComments(self):
        # Insert statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def rCompQuestions(self):
        # Insert statement
        t = tblCompQuestions.query.all()

        return random.choice(t)

    def rCompQuestionAns(self, prQuestionID):
        # Insert statement
        t = tblCompQuestionAns.query.filter_by(questionID=prQuestionID)
        q1 = t[0].questionAnswer1
        q2 = t[0].questionAnswer2
        q3 = t[0].questionAnswer3

        return q1, q2, q3

    def rUserCompAnswers(self):
        # Insert statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    # Update statements
    def uUserInformation(self):
        # Insert statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def uUserProgress(self):
        # Insert statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def uUserComments(self):
        # Insert statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def uCompQuestions(self):
        # Insert statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def uCompQuestionAns(self):
        # Insert statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def uUserCompAnswers(self):
        # Insert statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    # Delete statements
    def dUserInformation(self):
        # Insert statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def dUserProgress(self):
        # Insert statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def dUserComments(self):
        # Insert statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def dCompQuestions(self):
        # Insert statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def dCompQuestionAns(self):
        # Insert statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def dUserCompAnswers(self):
        # Insert statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()
