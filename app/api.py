from flask import Flask, Session
from sys import argv
from werkzeug.contrib.fixers import ProxyFix

from lib.security.security import security
from lib.views.publicViews import publicViews
from lib.views.privateViews import privateViews

####  ALL OF THIS STUFF SHOULD REMAIN FREE FLOATING ####
app = Flask(__name__)
app.register_blueprint(security)
app.register_blueprint(publicViews)
app.register_blueprint(privateViews)

app.wsgi_app = ProxyFix(app.wsgi_app)
try:
    app.secret_key = argv[argv.index('--key') + 1]
except ValueError:
    app.secret_key = 'afsdhghjkasdfUASGFDHusdfhyaYYJHJSDF'
#### FREE FLOATING SECTION ENDS HERE ####
    
def run():
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    run()
