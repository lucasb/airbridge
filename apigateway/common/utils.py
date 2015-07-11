# -*- config:utf-8 -*-
"""
    Copyright 2015 Airbridge

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

from flask import request as flask_request

from mongoengine.errors import ValidationError

from flask.ext.restful import abort as restful_abort
from flask.ext.restful import Resource as ResourceRestful


def abort(status, message=None):
    if message is None:
        restful_abort(status)
    restful_abort(status, message=message, status=status)


def request(obj):
    return obj.from_json(flask_request.data.decode('utf-8'))


def response(obj, status=200):
    return obj.to_json(), status


class Resource(ResourceRestful):

    def dispatch_request(self, *args, **kwargs):
        try:
            resp = super(Resource, self).dispatch_request(*args, **kwargs)
        except ValidationError as e:
            abort(400, e.message)
        except ValueError:
            abort(400)
        except Exception:
            abort(500)
        return resp
