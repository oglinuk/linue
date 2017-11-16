'''
view handlers
'''
import sys
import random
from app import app
from app.controller import forms
from app.model.dal import dalObject
from flask import render_template, redirect, request, session, escape

# Main Data Access Layer object
dalObj = dalObject()

######Route handlers######

# Home
@app.route('/')
@app.route('/home/')
def serveDefault():
    try:
        # Populate tblCompQuestions and tblCompQuestionAns if table is empty
        if dalObj.tblCompQuestions.query.all() == []:
            print('[LINUE] POPULATING COMP-QUESTIONS W/ ANSWERS [LINUE]')
            dalObj.popDB()

        if 'username' in session:
            return render_template('/index.html', signedInStatus=session['username'])
        return render_template('/index.html', signedInStatus='You are not logged in')
    except Exception as e:
        print(str(e))
        return render_template('/404.html',  error='{} - Error is near line {}'.format(str(e), (sys.exc_info()[-1].tb_lineno)))

# Blog
@app.route('/blog/')
def serveBlog():
    try:
        return render_template('/blog.html')
    except Exception as e:
        return render_template('/404.html',  error='{} - Error is near line {}'.format(str(e), (sys.exc_info()[-1].tb_lineno)))

# Projects
@app.route('/projects/')
def serveProjects():
    try:
        return render_template('/projects.html')
    except Exception as e:
        return render_template('/404.html',  error='{} - Error is near line {}'.format(str(e), (sys.exc_info()[-1].tb_lineno)))

# Playground for Nerds
@app.route('/pfn/')
def servePNF():
    try:
        return render_template('/pfn.html')
    except Exception as e:
        return render_template('/404.html',  error='{} - Error is near line {}'.format(str(e), (sys.exc_info()[-1].tb_lineno)))

# Setup
@app.route('/setup/')
def serveSetup():
    try:
        return render_template('/setup.html')
    except Exception as e:
        return render_template('/404.html',  error='{} - Error is near line {}'.format(str(e), (sys.exc_info()[-1].tb_lineno)))

# Login
@app.route('/login/', methods=['GET', 'POST'])
def serveLogin():
    try:
        loginSignupForm = forms.LoginSignupForm(request.form)
        if request.method == 'POST' and loginSignupForm.validate():
            # NOTE: Need to fix this line of code so that it queries the tblUserInformation userName field
            user = dalObj.rUserEmailInformation.query.filter_by(name=request.form['username'].lower()).first()
            if user.valid_password(request.form['password']):
                session['session_id'] = user.userEmail
                return redirect('/')
            else:
                return render_template('/login.html', form=LoginSignupForm, error='Invalid Login')
        else:
            return render_template('/login.html', form=loginSignupForm)
    except Exception as e:
        return render_template('/404.html',  error='{} - Error is near line {}'.format(str(e), (sys.exc_info()[-1].tb_lineno)))


# Sign-up
@app.route('/signup/', methods=['GET', 'POST'])
def serveSignup():
    try:
        loginSignupForm = forms.LoginSignupForm(request.form)
        if request.method == 'POST':
            dalObj.cNewUser(request.form['email'], request.form['password'])
            session['session_id'] = request.form['email']
            return render_template('/', signedInStatus=session['session_id'])
        else:
            return render_template('/signup.html', form=loginSignupForm)
    except Exception as e:
        return render_template('/404.html',  error='{} - Error is near line {}'.format(str(e), (sys.exc_info()[-1].tb_lineno)))

# Competition
@app.route('/competition/')
def serveCompForm():
    try:
        compForm = forms.competitionForm(request.form)

        # Random question assignment w/ random corresponding answers
        question1 = dalObj.rCompQuestions()
        question1Ans1, question1Ans2, question1Ans3 = dalObj.rRNGCompQuestionAns(question1.questionID)
        question2 = dalObj.rCompQuestions()
        question2Ans1, question2Ans2, question2Ans3 = dalObj.rRNGCompQuestionAns(question2.questionID)
        question3 = dalObj.rCompQuestions()
        question3Ans1, question3Ans2, question3Ans3 = dalObj.rRNGCompQuestionAns(question3.questionID)

        return render_template('/compForm.html', form=compForm, question1=question1.questionText, question1Answer1=question1Ans1, question1Answer2=question1Ans2, question1Answer3=question1Ans3,
                                question2=question2.questionText, question2Answer1=question2Ans1, question2Answer2=question2Ans2, question2Answer3=question2Ans3,
                                question3=question3.questionText, question3Answer1=question3Ans1, question3Answer2=question3Ans2, question3Answer3=question3Ans3)
    except Exception as e:
        # If the database is empty, redirect to homepage to trigger popDB()
        if 'empty' in str(e):
            return redirect('/')
        return render_template('/404.html',  error='{} - Error is near line {}'.format(str(e), (sys.exc_info()[-1].tb_lineno)))

# Thank You!
@app.route('/thankyou/', methods=['GET', 'POST'])
def serveThankYou():
    try:
        loginSignupForm = forms.LoginSignupForm(request.form)
        if request.method == 'POST':
            # NOTE: Need to refactor 130-135 to check if no radio buttons are ticked
            rbTicked = []
            rbList = ['q1Ans1', 'q1Ans2', 'q1Ans3', 'q2Ans1', 'q2Ans2', 'q2Ans3','q3Ans1', 'q3Ans2', 'q3Ans3']
            for radioButton in rbList:
                if request.form.get(radioButton):
                    rbTicked.append(radioButton)
            dalObj.cUserCompAnswers(escape(request.form[rbTicked[0]]), escape(request.form[rbTicked[1]]), escape(request.form[rbTicked[2]]), escape(request.form['className']), escape(request.form['schoolName']), escape(request.form['schoolPupilEmail']), escape(request.form['schoolTelephone']))
            userSubmission = dalObj.rUserCompAnswers()
        return render_template('/thankyou.html', form=loginSignupForm, q1=userSubmission[0], q2=userSubmission[1], q3=userSubmission[2], className=userSubmission[3], schoolName=userSubmission[4], schoolPupilEmail=userSubmission[5], schoolTelephone=userSubmission[6])
    except Exception as e:
        return render_template('/404.html', error='{} - Error is near line {}'.format(str(e), (sys.exc_info()[-1].tb_lineno)))

# 404 Error
@app.errorhandler(404)
def serve404(error):
    return render_template('/404.html', error='{} - Error is near line {}'.format(error, (sys.exc_info()[-1].tb_lineno)))

# Random
@app.route('/rng/')
def serverandom():
    try:
        randomPage = random.randint(0, 5)
        page = None
        if randomPage == 0:
            page = '/index.html'
        elif randomPage == 1:
            page = '/blog.html'
        elif randomPage == 2:
            page = '/projects.html'
        elif randomPage == 3:
            page = '/pfn.html'
        elif randomPage == 4:
            page = '/setup.html'
        elif randomPage == 5:
            page = '/404.html'
        return render_template(page)
    except Exception as e:
        return render_template('/404.html', error=str(e))
