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

from airbridge.common.database import db


class User(db.Document):
    email = db.EmailField(primary_key=True)
    username = db.StringField(unique=True)
    password = db.StringField(required=True)
    first_name = db.StringField(required=False)
    last_name = db.StringField(required=False)


class Client(db.Document):
    client_id = db.StringField(primary_key=True)
