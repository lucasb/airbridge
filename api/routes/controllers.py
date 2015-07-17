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

from flask import Blueprint
from flask.ext.restful import Api


routes = Blueprint('routes', __name__)
api = Api(routes)


"""class UserListAPI(Resource):

    def post(self):
        user = request(User)
        user = user.save()
        return response(user, 201)

    def get(self):
        return response(User.objects.all())


class UserAPI(Resource):

    def get(self, username):
        return response(User.objects.get_or_404(username=username))

    def put(self, username):
        user = request(User)
        user.update()
        return response(user)

    def delete(self, username):
        user = User.get(username=username)
        user.delete()
        return response(user)


# Routes
api.add_resource(UserListAPI, '/users')
api.add_resource(UserAPI, '/users/<string:username>')"""
