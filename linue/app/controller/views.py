'''
view handlers
'''

from flask import render_template
from app import app
from app.model import dbmodel
#from app.db.database import DatabaseModel
import random as RNG

######Route handlers######

# Home
@app.route('/')
@app.route('/home/')
def serveDefault():
    dbmodel.cCompQuestions('Hello World')
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

# Login page
@app.route('/login/', methods=['GET'])
def serveLogin():
    return render_template('/login.html')

# Login handler
@app.route('/login/', methods=['POST'])
def serveLoginSubmit():
    return render_template('/login.html')

# Sign-up
@app.route('/sign-up/')
def serveSignup():
    return render_template('/signup.html')

@app.route('/competition/')
def serveCompForm():
    return render_template('/compForm.html')

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
