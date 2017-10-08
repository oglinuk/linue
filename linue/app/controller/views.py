'''
view handlers
'''

from flask import render_template, redirect, request
from app import app
from app.controller import forms
from app.db import database as db
from app.model import dal
import random as RNG
from datetime import datetime

######Route handlers######

# Home
@app.route('/')
@app.route('/home/')
def serveDefault():
    return render_template('/index.html')

# Blog
@app.route('/blog/')
def serveBlog():
    return render_template('/blog.html')

# Projects
@app.route('/projects/')
def serveProjects():
    return render_template('/projects.html')

# Playground for Nerds
@app.route('/pfn/')
def servePNF():
    return render_template('/pfn.html')

# Setup
@app.route('/setup/')
def serveSetup():
    return render_template('/setup.html')

# Login
@app.route('/login/', methods=['GET', 'POST'])
def serveLogin():
    loginForm = forms.LoginForm(request.form)
    if request.method == 'POST' and loginForm.validate():
        user = db.tblUserInformation.query.filter_by(name=request.form['username'].lower()).first()
        if user.valid_password(request.form['password']):
            session['session_id'] = user.new_session()
            return redirect('/')
        else:
            return render_template('/login.html', form=loginForm, error='Invalid Login')
    else:
        return render_template('/login.html', form=loginForm)

# Sign-up
@app.route('/signup/', methods=['GET', 'POST'])
def serveSignup():
    try:
        signupForm = forms.LoginForm(request.form)
        if request.method == 'POST' and signupForm.validate():
            newUser = db.NewUser(request.form['username'], request.form['password'])
            print(newUser.userEmail, newUser.userPassword)
            if newUser.valid_password(request.form['password']):
                session['session_id'] = newUser.new_session()
                return redirect('/')
            else:
                return render_template('/signup.html', form=signupForm, error='Invalid Signup')
        else:
            return render_template('/signup.html', form=signupForm)
    except Exception as e:
        return str(e)

@app.route('/competition/')
def serveCompForm():
    try:
        return render_template('/compForm.html', question1='Best programming language?', question1Answer1='Python', question1Answer2='C#', question1Answer3='Go',
                                question2='What is the best website?', question2Answer1='Google.com', question2Answer2='StackOverflow.com', question2Answer3='This one',
                                question3='What is the meaning of life?', question3Answer1='Nothing', question3Answer2='Living', question3Answer3='42')
    except Exception as e:
        return str(e)

# RNG route handler that serves a random page
@app.route('/rng/')
def serveRNG():
    randomPage = RNG.randint(1, 5)
    page = None
    if randomPage == 1:
        page = '/index.html'
    elif randomPage == 2:
        page = '/blog.html'
    elif randomPage == 3:
        page = '/projects.html'
    elif randomPage == 4:
        page = '/pfn.html'
    elif randomPage == 5:
        page = '/setup.html'
    return render_template(page)
