# coding: utf-8

import MySQLdb
import os
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key is here'

HOST = os.environ.get("SPORTS_DB_URL")
USER = os.environ.get("SPORTS_DB_USER")
PASSWD = os.environ.get("SPORTS_DB_PASS")
DB = os.environ.get("SPORTS_DB_NAME")
db = MySQLdb.connect(host=HOST,user=USER,passwd=PASSWD,db=DB)
basedir = os.path.abspath(os.path.dirname(__file__))

from . import views, forms
