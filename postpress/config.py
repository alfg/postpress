#!/usr/bin/env python

from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read('config.ini')

# Read config.ini and store into variables
HOST = config.get('app', 'HOST')
PORT = int(config.get('app', 'PORT'))
DEBUG = config.get('app', 'DEBUG')

DB = config.get('database', 'DB')
DBDEBUG = config.get('database', 'DBDEBUG')
