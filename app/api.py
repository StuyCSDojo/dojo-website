import cherrypy
import flask
import os
import sys
from paste import translogger
import werkzeug.contrib.fixers

from lib.security import security
from lib.views import private
from lib.views import public
from lib.views import resources
from lib.utils import utils

####  ALL OF THIS STUFF SHOULD REMAIN FREE FLOATING ####
app = flask.Flask(__name__)
app.register_blueprint(security.security)
app.register_blueprint(private.private_views)
app.register_blueprint(public.public_views)
app.register_blueprint(resources.resources)

app.wsgi_app = werkzeug.contrib.fixers.ProxyFix(app.wsgi_app)
try:
    app.secret_key = sys.argv[sys.argv.index('--key') + 1]
except ValueError:
    app.secret_key = 'e5fce5faa2e20b203c014f358f73c48f7129084ab1643c9fa6a0f87ff7a546a2'
    #get value via os.urandom(32).encode('hex')

@app.errorhandler(404)
@utils.log_name
def page_not_found(error):
    return flask.render_template('404.html'), 404

#### FREE FLOATING SECTION ENDS HERE ####

def run_server():
        # Enable WSGI access logging via Paste
        app_logged = translogger.TransLogger(app)

        # Mount the WSGI callable object (app) on the root directory
        cherrypy.tree.graft(app_logged, '/')

        # Set the configuration of the web server
        cherrypy.config.update({
            'engine.autoreload_on': True,
            'log.screen': True,
            'server.socket_file': '/tmp/website.sock'
            #'server.socket_host': '0.0.0.0',
            #'server.socket_port': 5000
        })

        # Start the CherryPy WSGI web server
        cherrypy.engine.start()
        cherrypy.engine.block()

def run():
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)

if __name__ == '__main__':
    run_server()
