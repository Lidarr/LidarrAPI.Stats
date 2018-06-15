"""
Stats API
"""

import flask
import flask_restful

import lidarrstats
from lidarrstats.api import resources

api_blueprint = flask.Blueprint('api', __name__)
api = flask_restful.Api(api_blueprint)

api.add_resource(resources.Error, '/error')

@api_blueprint.route('/')
def info():
    return flask.jsonify(version=lidarrstats.__version__)