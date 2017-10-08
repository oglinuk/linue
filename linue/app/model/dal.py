'''
linue data access layer
'''
from app.db import database
from sqlalchemy import MetaData, Table, insert, update, select


###### Database debug functions ######

def getSpecificDBTable(prTable):
    table = None
    if prTable == 'tblUserInformation':
        table = data.tblUserInformation
    elif prTable == 'tblUserProgress':
        table = data.tblUserProgress
    elif prTable == 'tblUserComments':
        table = data.tblUserComments
    elif prTable == 'tblCompQuestions':
        table = data.tblCompQuestions
    elif prTable == 'tblCompQuestionAns':
        table = data.tblCompQuestionAns
    elif prTable == 'tblUserCompAnswers':
        table = data.tblUserCompAnswers
    else:
        return print('No table named %s' % (prTable))

    #tableColumns = [c.name for c in table.columns]
    return table

###### CRUD Statements ######

# Create statements
def cUserInformation(prFName, prLName, prEmail, prPassword, prDOB, prPhone, prType, prOrganization, prJoinDate):
    # Table
    table = getSpecificDBTable('tblUserInformation')

    # Insert statement
    values = data.tblUserInformation(prFName, prLName, prEmail, prPassword, prDOB, prPhone, prType, prOrganization, prJoinDate)

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate
    #print([attr for attr in dir(data.tblUserInformation) if attr.startswith('user')])
    print(values.userID, values.userFirstName, values.userLastName, values.userEmail, values.userPassword, values.userDOB, values.userPhone, values.userType, values.userOrganization, values.userJoinDate)

def cNewUser(prEmail, prPassword):
    # Table
    table = getSpecificDBTable('tblUserInformation')

    # Insert statement
    values = data.NewUser(prEmail, prPassword)

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate
    print(values.userEmail + '\n' + values.userPassword)

def cUserProgress(prProgressType, prProgressStartDate, prProgressCompletionDate):
    # Table
    table = getSpecificDBTable()

    # Insert statement
    values = None

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate

def cUserComments(prComment, prTutorialPage, prTutorialTopic, prModStatus):
    # Table
    table = getSpecificDBTable()

    # Insert statement
    values = None

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate

def cCompQuestions(prQuestionText):
    # Table
    table = getSpecificDBTable('tblCompQuestions')

    # Insert statement
    values = data.tblCompQuestions(prQuestionText)

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate
    print(values.questionText)

def cCompQuestionAns(prQuestionAns1, prQuestionAns2, prQuestionAns3, prQuestionCorrectAns):
    # Table
    table = getSpecificDBTable()

    # Insert statement
    values = None

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate

def cUserCompAnswers(prQuestion1Ans, prQuestionAns2, prQuestionAns3, prClassName, prSchoolName, prSchoolEmail, prSchoolPhone):
    # Table
    table = getSpecificDBTable()

    # Insert statement
    values = None

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate

# Retrieve statements
def rUserInformation():
    # Table
    table = getSpecificDBTable()

    # Insert statement
    values = None

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate

def rUserProgress():
    # Table
    table = getSpecificDBTable()

    # Insert statement
    values = None

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate

def rUserComments():
    # Table
    table = getSpecificDBTable()

    # Insert statement
    values = None

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate

def rCompQuestions():
    # Table
    table = getSpecificDBTable()

    # Insert statement
    values = None

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate

def rCompQuestionAns():
    # Table
    table = getSpecificDBTable()

    # Insert statement
    values = None

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate

def rUserCompAnswers():
    # Table
    table = getSpecificDBTable()

    # Insert statement
    values = None

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate

# Update statements
def uUserInformation():
    # Table
    table = getSpecificDBTable()

    # Insert statement
    values = None

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate

def uUserProgress():
    # Table
    table = getSpecificDBTable()

    # Insert statement
    values = None

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate

def uUserComments():
    # Table
    table = getSpecificDBTable()

    # Insert statement
    values = None

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate

def uCompQuestions():
    # Table
    table = getSpecificDBTable()

    # Insert statement
    values = None

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate

def uCompQuestionAns():
    # Table
    table = getSpecificDBTable()

    # Insert statement
    values = None

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate

def uUserCompAnswers():
    # Table
    table = getSpecificDBTable()

    # Insert statement
    values = None

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate

# Delete statements
def dUserInformation():
    # Table
    table = getSpecificDBTable()

    # Insert statement
    values = None

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate

def dUserProgress():
    # Table
    table = getSpecificDBTable()

    # Insert statement
    values = None

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate

def dUserComments():
    # Table
    table = getSpecificDBTable()

    # Insert statement
    values = None

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate

def dCompQuestions():
    # Table
    table = getSpecificDBTable()

    # Insert statement
    values = None

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate

def dCompQuestionAns():
    # Table
    table = getSpecificDBTable()

    # Insert statement
    values = None

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate

def dUserCompAnswers():
    # Table
    table = getSpecificDBTable()

    # Insert statement
    values = None

    # Commit
    data.db.session.add(values)
    data.db.session.commit()

    # Validate
