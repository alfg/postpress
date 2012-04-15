#!/usr/bin/env python

from flask import Flask
from flask import redirect

app = Flask(__name__)

@app.route("/post", methods=['POST'])
def post():

    return redirect(url_for('index'))
