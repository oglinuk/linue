'''
linue model

Handles the logic of the website database
'''

from app.db import database
from sqlalchemy import MetaData, Table


###### Database debug functions ######

# Show all DB tables
def getDBTables():
    eng = database.getDBEngine()
    return eng.table_names()

def getSpecificDBTable(prTable):
    table = None
    if prTable == 'tblUserInformation':
        table = database.getDBTable(prTable)
    elif prTable == 'tblUserProgress':
        table = database.getDBTable(prTable)
    elif prTable == 'tblUserComments':
        table = database.getDBTable(prTable)
    elif prTable == 'tblCompQuestions':
        table = database.getDBTable(prTable)
    elif prTable == 'tblCompQuestionAns':
        table = database.getDBTable(prTable)
    elif prTable == 'tblUserCompAnswers':
        table = database.getDBTable(prTable)
    else:
        return print('No table named %s' % (prTable))
    return print([c.name for c in table.columns])

###### CRUD Statements ######

# Create statements
def cUserInformation(prFName, prLName, prEmail, prPassword, prDOB, prPhone, prType, prOrganization, prJoinDate):
    pass

def cUserProgress(prProgressType, prProgressStartDate, prProgressCompletionDate):
    pass

def cUserComments(prComment, prTutorialPage, prTutorialTopic, prModStatus):
    pass

def cCompQuestions(prQuestionText):
    table = getSpecificDBTable('tblCompQuestions')
    insertStatement = insert(table)
    insertStatement = insertStatement.values('_questionText' : 'hello world')
    session = getDBSession()
    print(session.execute(insertStatement))
    session.commit()

def cCompQuestionAns(prQuestionAns1, prQuestionAns2, prQuestionAns3, prQuestionCorrectAns):
    pass

def cUserCompAnswers(prQuestion1Ans, prQuestionAns2, prQuestionAns3, prClassName, prSchoolName, prSchoolEmail, prSchoolPhone):
    pass

# Retrieve statements
def rUserInformation():
    pass

def rUserProgress():
    pass

def rUserComments():
    pass

def rCompQuestions():
    pass

def rCompQuestionAns():
    pass

def rUserCompAnswers():
    pass

# Update statements
def uUserInformation():
    pass

def uUserProgress():
    pass

def uUserComments():
    pass

def uCompQuestions():
    pass

def uCompQuestionAns():
    pass

def uUserCompAnswers():
    pass

# Delete statements
def dUserInformation():
    pass

def dUserProgress():
    pass

def dUserComments():
    pass

def dCompQuestions():
    pass

def dCompQuestionAns():
    pass

def dUserCompAnswers():
    pass
