# -*- config:utf-8 -*-
"""
    Copyright 2014 Airbridge

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import json

from flask import Blueprint, jsonify, request, make_response
from flask.views import MethodView

from werkzeug.exceptions import HTTPException, default_exceptions


class Api():

    def __init__(self, app):

        if not isinstance(app, Blueprint):
            HttpError(app)

        self.app = app

    def set_routes(self, view, url, endpoint=None,
                   pk='id', pk_type='string', pk_default=None):

        if endpoint is None:
            endpoint = type(view).__name__

        view_func = view.as_view(endpoint)

        self.app.add_url_rule(url, view_func=view_func, methods=['POST'])
        self.app.add_url_rule(url, defaults={pk: pk_default},
                              view_func=view_func, methods=['GET'])
        self.app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk),
                              view_func=view_func, methods=['GET', 'PUT',
                                                            'DELETE'])


class HttpError():

    def __init__(self, app):

        def make_json_error(ex):
            response = jsonify(message=str(ex))
            response.status_code = (ex.code
                                    if isinstance(ex, HTTPException)
                                    else 500)
            return response

        for code in default_exceptions:
            app.error_handler_spec[None][code] = make_json_error


class Resource(MethodView):

    def dispatch_request(self, *args, **kwargs):

        meth = super(Resource, self).dispatch_request(*args, **kwargs)

        response = make_response(self._parse(meth))
        response.headers['Content-Type'] = 'application/json'
        response.status_code = 200 if request.method != 'POST' else 201

        return response

    def _parse(self, data):

        if self._is_json(data):
            d = data.from_json()
        else:
            d = data.to_json()
        return d

    def _is_json(self, value):

        try:
            json.loads(value)
        except TypeError or ValueError:
            return False
        return True
