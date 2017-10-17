'''
view handlers
'''

from flask import render_template, redirect, request, session
from app import app
from app.controller import forms
from app.model.dal import dalObject
import random
from datetime import datetime


dalObj = dalObject()

compQuestions = ['What is the best programming language?',
'What is the meaning of life?',
'What is the best website?',
'Who should you ask when in doubt?',
'What is the best country in the world?',
'What is the best subject in the entire universe?',
'What language should you never learn?',
'What is the most prominent language used in the industry?',
'What language is this website made in?']

compQuestionAns = [['Python', 'C#', 'Go'],
['42', 'living', 'nothing'],
['StackOverflow.com', 'This website', 'Google.com'],
['StackOverflow', 'Siri', 'Your parent(s)'],
[ 'New Zealand', 'Norway', 'America'],
['IT', 'Math', 'Science'],
['PHP', 'Python', 'Perl'],
['C', 'Java', 'C++'],
['Python', 'PHP', 'JavaScript']]

######Route handlers######

# Home
@app.route('/')
@app.route('/home/')
def serveDefault():
    try:
        if dalbj.tblCompQuestions.query.all() == []:
            print('[LINUE] POPULATING COMP-QUESTIONS W/ ANSWERS [LINUE]')
            # Populate tblCompQuestions and tblCompQuestionAns
            for question in compQuestions:
                dalObj.cCompQuestions(question)

            for i, ans in enumerate(compQuestionAns):
                dalObj.cCompQuestionAns(i+1, ans[0], ans[1], ans[2], 1)

        if 'username' in session:
            username = session['username']
            return render_template('/index.html', signedInStatus=username)
        return render_template('/index.html', signedInStatus='You are not logged in')
    except Exception as e:
        print(str(e))
        return render_template('/404.html', error=str(e))

# Blog
@app.route('/blog/')
def serveBlog():
    try:
        return render_template('/blog.html')
    except Exception as e:
        return render_template('/404.html', error=str(e))

# Projects
@app.route('/projects/')
def serveProjects():
    try:
        return render_template('/projects.html')
    except Exception as e:
        return render_template('/404.html', error=str(e))

# Playground for Nerds
@app.route('/pfn/')
def servePNF():
    try:
        return render_template('/pfn.html')
    except Exception as e:
        return render_template('/404.html', error=str(e))

# Setup
@app.route('/setup/')
def serveSetup():
    try:
        return render_template('/setup.html')
    except Exception as e:
        return render_template('/404.html', error=str(e))

# Login
@app.route('/login/', methods=['GET', 'POST'])
def serveLogin():
    try:
        loginForm = forms.LoginForm(request.form)
        if request.method == 'POST' and loginForm.validate():
            # NOTE: Need to fix this line of code so that it queries the tblUserInformation userName field
            user = dalObj.tblUserInformation.query.filter_by(name=request.form['username'].lower()).first()
            if user.valid_password(request.form['password']):
                session['session_id'] = user.userEmail
                return redirect('/')
            else:
                return render_template('/login.html', form=loginForm, error='Invalid Login')
        else:
            return render_template('/login.html', form=loginForm)
    except Exception as e:
        return render_template('/404.html', error=str(e))


# Sign-up
@app.route('/signup/', methods=['GET', 'POST'])
def serveSignup():
    try:
        signupForm = forms.SignupForm(request.form)
        if request.method == 'POST' and signupForm.validate():
            newUser = dalObj.cNewUser(request.form['username'], request.form['email'], request.form['password'])
            if request.form['password'] != None and request.form['username'] != None:
                session['session_id'] = newUser
                return redirect('/')
            else:
                return render_template('/signup.html', form=signupForm, error='Invalid Signup')
        else:
            return render_template('/signup.html', form=signupForm)
    except Exception as e:
        return render_template('/404.html', error=str(e))

# Competition
@app.route('/competition/')
def serveCompForm():
    try:
        # Random question assignment w/ corresponding answers
        question1 = dalObj.rCompQuestions()
        question1Ans1, question1Ans2, question1Ans3 = dalObj.rCompQuestionAns(question1.questionID)
        question2 = dalObj.rCompQuestions()
        question2Ans1, question2Ans2, question2Ans3 = dalObj.rCompQuestionAns(question2.questionID)
        question3 = dalObj.rCompQuestions()
        question3Ans1, question3Ans2, question3Ans3 = dalObj.rCompQuestionAns(question3.questionID)

        return render_template('/compForm.html', question1=question1.questionText, question1Answer1=question1Ans1, question1Answer2=question1Ans2, question1Answer3=question1Ans3,
                                question2=question2.questionText, question2Answer1=question2Ans1, question2Answer2=question2Ans2, question2Answer3=question2Ans3,
                                question3=question3.questionText, question3Answer1=question3Ans1, question3Answer2=question3Ans2, question3Answer3=question3Ans3)
    except Exception as e:
        return render_template('/404.html', error=str(e))

# Thank You!
@app.route('/thankyou/')
def serveThankYou():
    return render_template('/thankyou.html')

# 404 Error
@app.route('/404/')
def serve404():
    return render_template('/404.html')

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
            page = '/competitonForm.html'
        return render_template(page)
    except Exception as e:
        return render_template('/404.html', error=str(e))
