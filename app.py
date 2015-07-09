from flask import Flask
app = Flask(__name__)

#Make the WSGI interface available at the top level
wsgi_app = app.wsgi_app

#Import all routes from routes.py
from routes import *;

if __name__ == '__main__':
    app.run(debug=False)