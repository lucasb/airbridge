#!/usr/bin/env python

import falcon

class TestResource:
    """ Gets text with test message """

    def on_get(self, req, resp):
        """ Gets text with test message """
        resp.body = "Falcon works!"

API = falcon.API()
API.add_route('/test', TestResource())
