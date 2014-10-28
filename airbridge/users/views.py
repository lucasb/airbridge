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

from flask import Blueprint

from ..common.api import Api, Resource
from .models import User


users = Blueprint('users', __name__, url_prefix='/users')
api = Api(users)


class UserAPI(Resource):

    def post(self):
        return {'username': 'post'}

    def get(self, username):
        if username is None:
            return User.objects.all()
        return User.objects.get_or_404(username=username)

    def put(self, username):
        print('put ' + username)
        return

    def delete(self, username):
        print('delete ' + username)
        return


# Routes
api.set_routes(UserAPI, '/', pk='username')
