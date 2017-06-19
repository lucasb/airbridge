#!/usr/bin/env python

import json
import falcon
import rethinkdb as r


CONN = r.connect(db='test')

class TestResource:
    """ Gets text with test message """

    def on_get(self, req, resp):
        """ Gets text with test message """
        resp.body = "Falcon works!"

class RethinkDBResource:
    """Rethink test"""

    def on_get(self, req, res):
        """ Get data from athours table """
        result = r.table('authors').run(CONN)
        res.body = json.dumps(list(result))

API = falcon.API()
API.add_route('/test', TestResource())
API.add_route('/db', RethinkDBResource())
