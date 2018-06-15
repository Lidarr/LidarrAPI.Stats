"""
Application from blueprints
"""

import flask

from lidarrstats.api import api

app = flask.Flask(__name__)
app.register_blueprint(api.api_blueprint, url_prefix='/api')

def debug():
    app.run(port=8945, debug=True)

if __name__ == '__main__':
    debug()