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

from flask import Blueprint, jsonify, request
from flask.views import MethodView

from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException


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
                          view_func=view_func, methods=['GET', 'PUT', 'DELETE'])


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

    resp = super(Resource, self).dispatch_request(*args, **kwargs)
    print(request.method)
    return resp
