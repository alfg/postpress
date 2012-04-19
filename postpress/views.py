#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import render_template
from flask import request, redirect, url_for

from postpress import config
from postpress.models import *

app = Flask(__name__)

# All views below
@app.route("/")
def index():
    posts = Post.query.all()

    return render_template('index.html', posts=posts)

@app.route("/settings")
def settings():
   
    users = User.query.all()

    return render_template('settings.html', users=users)

@app.route('/post/<job_id>')
def show_post(job_id):
    post = Post.query.filter_by(jobid=job_id).first()

    return render_template('post.html', post=post)

# Controllers
@app.route("/add", methods=['POST'])
def add():
    jobid = request.form['jobid']
    jobtype = request.form['jobtype']
    location = request.form['location']
    title = request.form['title']
    salary = request.form['salary']

    post = Post(jobid, jobtype, location, title, salary, "Insert Description Here", False)
    db.session.add(post)
    db.session.commit()

    return redirect(url_for('show_post', job_id=jobid))

@app.route("/update", methods=['POST'])
def update():
    jobid = request.form['jobid']
    action = request.form['submit']

    if action == "update":
        description = request.form['description']
        q = Post.query.filter_by(jobid=jobid).first()
        q.description = description
        db.session.add(q)
        db.session.commit()

        return redirect(url_for('show_post', job_id=jobid))

    elif action == "delete":
        q = Post.query.filter_by(jobid=jobid).first()
        db.session.delete(q)
        db.session.commit()

        return redirect(url_for('index'))

    elif action == "publish":
        q = Post.query.filter_by(jobid=jobid).first()
        q.published = True
        db.session.add(q)
        db.session.commit()

    elif action == "private":
        q = Post.query.filter_by(jobid=jobid).first()
        q.published = False
        db.session.add(q)
        db.session.commit()
    
    else:
        return "error"

    return redirect(url_for('show_post', job_id=jobid))

@app.route("/render")
def render():

    posts = Post.query.all()
    
    return render_template('render/html.html', posts=posts)

# Error Pages
@app.errorhandler(500)
def error_page(e):
    return render_template('error_pages/500.html'), 500

@app.errorhandler(404)
def not_found(e):
    return render_template('error_pages/404.html'), 404


