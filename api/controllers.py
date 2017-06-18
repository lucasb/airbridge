#!/usr/bin/env python

"""
    Copyright 2017 Airbridge

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
import falcon
from models import Account


class AccountResource:
    def on_get(self, req, res):
        all = Account.all()
        res.body = json.dumps(self._present_list(all))

    def on_post(self, req, res):
        try:
            raw_body = req.stream.read()
            body = json.loads(raw_body.decode('utf-8'))
            new_account = Account.create(name=body['name'])
            new_account.save()
            res.status = falcon.HTTP_201
            res.body = json.dumps(self._present_one(new_account))
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400, 'Invalid JSON',
                                   'Could not decode the request body. The JSON was incorrect.')
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', ex)

    def _present_one(self, obj):
        return {
            'id': obj['id'],
            'name': obj['name'],
        }

    def _present_list(self, array):
        return list(map(lambda i: self._present_one(i), array))

