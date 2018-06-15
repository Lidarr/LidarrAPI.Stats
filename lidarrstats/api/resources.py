"""
API resources
"""

import flask
import flask_restful
import flask_restful.reqparse
import rethinkdb

RETHINK_HOST = 'rethink'
RETHINK_DB = 'stats'

def _check_table(connection, table_name):
    """
    Checks that db has table and creates it if not

    # TODO Move this to some global startup function so it isn't run at every request

    :param table_name:
    :return:
    """
    if not rethinkdb.db_list().contains(RETHINK_DB).run(connection):
        print('Creating db {}'.format(RETHINK_DB))
        rethinkdb.db_create(RETHINK_DB).run(connection)

    db = rethinkdb.db(RETHINK_DB)

    if not db.table_list().contains(table_name).run(connection):
        print('Creating table {}'.format(table_name))
        db.table_create(table_name).run(connection)

    return db.table(table_name)

class Error(flask_restful.Resource):
    def post(self):
        if not flask.request.json:
            return {'error': 'POST data required'}, 400

        try:
            connection = rethinkdb.connect(RETHINK_HOST, timeout=3)
        except rethinkdb.ReqlTimeoutError as e:
            print(e)
            return {'error': 'Internal error'}, 500

        parser = flask_restful.reqparse.RequestParser()
        parser.add_argument('Client-Id', location='headers')
        parser.add_argument('client_id')
        parser.add_argument('type', required=True)

        args = parser.parse_args()

        item = {}
        item['client'] = args['Client-Id'] or args['client_id']
        item['type'] = args['type']
        item['body'] = flask.request.json

        table = _check_table(connection, 'error')
        ret = table.insert(item).run(connection)

        if ret['errors']:
            print('Error adding to db: {}'.format(ret))
            return {'error': 'Internal error'}, 500

        id = list(ret['generated_keys'])[0]
        return {'id': id}, 200