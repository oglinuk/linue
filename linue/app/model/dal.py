'''
linue db access layer
'''

# NOTE: Need to add try/except statements to each method in the dalObject

import random
import app.db.database as database
from app.db.database import tblUserInformation, NewUser, tblUserProgress, tblUserComments, tblCompQuestions, tblCompQuestionAns, tblUserCompAnswers
from app.db.population import compQuestions, compQuestionAns

class dalObject(object):
    """The Data Access Layer object with methods to interact with the database"""
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

    def popDB(self):
        # Populates tblCompQuestions
        for question in compQuestions:
            self.cCompQuestions(question)

        # Populates tblCompQuestionAns
        for i, ans in enumerate(compQuestionAns):
            self.cCompQuestionAns(i+1, ans[0], ans[1], ans[2], ans[0])

    ###### CRUD Statements ######

    ##### Create statements #####
    def cUserInformation(self, prFName, prLName, prEmail, prPassword, prDOB, prPhone, prType, prOrganization, prJoinDate):
        try:
            # Insert statement
            row = tblUserInformation(rFName, prLName, prEmail, prPassword, prDOB, prPhone, prType, prOrganization, prJoinDate)

            # Commit
            self.db.session.add(row)
            self.db.session.commit()

            # Validate
            print('[LINUE] SUCCESSFULLY INSERTED STATEMENT - cUserInformation - 38 [LINUE]')

        except Exception as e:
            print(str(e) + '# cUserInformation')
            return str(e) + '# cUserInformation'

    def cNewUser(self, prEmail, prPassword):
        # Insert statement
        row = NewUser(prEmail, prPassword)

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

        # Validate
        print('[LINUE] SUCCESSFULLY INSERTED STATEMENT - cNewUser - 54 [LINUE]')

    def cUserProgress(self, prProgressType, prProgressStartDate, prProgressCompletionDate):
        # Insert statement
        row = tblUserProgress(prProgressType, prProgressStartDate, prProgressCompletionDate)

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

        # Validate
        print('[LINUE] SUCCESSFULLY INSERTED STATEMENT - cUserProgress - 65 [LINUE]')

    def cUserComments(self, prComment, prTutorialPage, prTutorialTopic, prModStatus):
        # Insert statement
        row = tblUserComments(prComment, prTutorialPage, prTutorialTopic, prModStatus)

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

        # Validate
        print('[LINUE] SUCCESSFULLY INSERTED STATEMENT - cUserComments - 76 [LINUE]')

    def cCompQuestions(self, prQuestionText):
        # Insert statement
        row = tblCompQuestions(prQuestionText)

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

        # Validate
        print('[LINUE] SUCCESSFULLY INSERTED STATEMENT - cCompQuestions - 87 [LINUE]')

    def cCompQuestionAns(self, prQuestionID, prQuestionAns1, prQuestionAns2, prQuestionAns3, prQuestionCorrectAns):
        # Insert statement
        row = tblCompQuestionAns(prQuestionID, prQuestionAns1, prQuestionAns2, prQuestionAns3, prQuestionCorrectAns)

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

        # Validate
        print('[LINUE] SUCCESSFULLY INSERTED STATEMENT - cCompQuestionAns - 98 [LINUE]')

    def cUserCompAnswers(self, prQuestion1Ans, prQuestionAns2, prQuestionAns3, prClassName, prSchoolName, prSchoolEmail, prSchoolPhone):
        # Insert statement
        row = tblUserCompAnswers(prQuestion1Ans, prQuestionAns2, prQuestionAns3, prClassName, prSchoolName, prSchoolEmail, prSchoolPhone)

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

        # Validate
        print('[LINUE] SUCCESSFULLY INSERTED STATEMENT - cUserCompAnswers - 109 [LINUE]')

    ##### Retrieve statements #####
    def rUserEmailInformation(self, prUserEmail):
        # Retrieve statement
        t = tblUserInformation.query.filter_by(userEmail=prUserEmail)
        return t

    def rUserProgress(self):
        # Retrieve statement
        row = None

    def rUserComments(self):
        # Retrieve statement
        row = None

    def rCompQuestions(self):
        # Retrieve statement
        t = tblCompQuestions.query.all()
        return random.choice(t)

    def rRNGCompQuestionAns(self, prQuestionID):
        # Retrieve statement
        t = tblCompQuestionAns.query.filter_by(questionID=prQuestionID)
        qAns = [t[0].questionAnswer1, t[0].questionAnswer2, t[0].questionAnswer3]
        random.shuffle(qAns)
        return qAns

    def rCorrectCompQuestionAns(self):
        t = tblCompQuestionAns.query.all()
        return t

    def rUserCompAnswers(self):
        # Retrieve statement
        t = tblUserCompAnswers.query.with_entities(tblUserCompAnswers.userQuestion1Ans, tblUserCompAnswers.userQuestion2Ans, tblUserCompAnswers.userQuestion3Ans, tblUserCompAnswers.userClassName, tblUserCompAnswers.userSchoolName, tblUserCompAnswers.userSchoolEmail, tblUserCompAnswers.userSchoolPhone)
        return t[-1]

    ##### Update statements #####
    def uUserInformation(self):
        # Retrieve statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def uUserProgress(self):
        # Update statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def uUserComments(self):
        # Update statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def uCompQuestions(self):
        # Update statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def uCompQuestionAns(self):
        # Update statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def uUserCompAnswers(self):
        # Update statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    ##### Delete statements #####
    def dUserInformation(self):
        # Delete statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def dUserProgress(self):
        # Delete statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def dUserComments(self):
        # Delete statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def dCompQuestions(self):
        # Delete statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def dCompQuestionAns(self):
        # Delete statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()

    def dUserCompAnswers(self):
        # Delete statement
        row = None

        # Commit
        self.db.session.add(row)
        self.db.session.commit()
