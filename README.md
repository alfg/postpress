# PostPress #

PostPress is a small Flask web application to display job postings integrated into your website
by inserting a snippet of Javascript. PostPress provides a simple web interface to 
administrate and publish the job postings. PostPress is in early development.


## Requirements ##

- Python 2.7+
- Sqlite3
- Flask, flask-sqlalchemy

## Installation ##

As usual, it is recommended to set this up in a virtual environment.

1. If not installed already, please install sqlite3:

        $ sudo apt-get install sqlite3

2. Clone postpress.git:

        $ git clone git://github.com/alfg/postpress.git

3. Run setup.py to install dependencies:

        $ python setup.py develop

4. Open config.ini and set the required variables.

5. Run the development server:

        $ python run.py


## Notes ##

PostPress is in early development and therefore is not completely functional.
However, feel free to clone or fork and install to see the currrent progress.
