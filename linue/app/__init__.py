'''
app/__init__.py
'''
from flask import Flask
import os

# initialization
# instance_relative_config swaps from 'relative to the application root' to 'relative to instance folder'
app = Flask(__name__, instance_relative_config=True)

from app.controller import views

# config file
app.config.from_object('config')
app.secret_key = os.urandom(24)
