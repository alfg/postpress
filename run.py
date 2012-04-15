#!/usr/bin/env python

from postpress import views
from postpress import models
from postpress import config

# Imports and creates DB with models
from postpress.models import db

# Create database schema
db.create_all()

# app = Flask
app = views.app

# Return an App
if __name__ == "__main__":
    views.app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
