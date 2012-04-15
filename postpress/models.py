#!/usr/bin/env python

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from postpress import config


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../%s' % (config.DB)
app.config['SQLALCHEMY_ECHO'] = config.DBDEBUG
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jobid = db.Column(db.Integer)
    type = db.Column(db.String(150))
    title = db.Column(db.String(120))
    location = db.Column(db.String(120))
    salary = db.Column(db.String(120))
    description = db.Column(db.String)
    published = db.Column(db.Boolean)

    def __init__(self, jobid, type, title, location, salary, description, published):
        self.jobid = jobid
        self.type = type
        self.title = title
        self.location = location
        self.salary = salary
        self.description = description
        self.published = published

    def __repr__(self):
        return '<Post %r>' % self.title

