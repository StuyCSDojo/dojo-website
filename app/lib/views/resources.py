import flask
import os.path

from lib.utils import utils

resources = flask.Blueprint('resources', __name__)

@resources.route('/public_resources/knights-tour-sketchpad/')
@resources.route('/public_resources/knights-tour-sketchpad/<path:filename>')
@utils.log_name
def knight_tour(filename = 'index.html'):
    path = os.path.join('useful_links/knights-tour-sketchpad', filename)
    return flask.current_app.send_static_file(path)

@resources.route('/public_resources/nqueens-sketchpad/')
@resources.route('/public_resources/nqueens-sketchpad/<path:filename>')
@utils.log_name
def nqueens_sketchpad(filename = 'index.html'):
    path = os.path.join('useful_links/nqueens-sketchpad', filename)
    return flask.current_app.send_static_file(path)
