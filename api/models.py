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

from remodel import helpers
from remodel import connection
from remodel.models import Model


connection.pool.configure(db='airbridge')


class Account(Model):
    has_many = ('App', 'Group', 'Identity',)


class App(Model):
    belongs_to = ('Account',)
    has_many = ('Permission',)


class Group(Model):
    belongs_to = ('Account',)
    has_many = ('Identity', 'Permission',)


class Identity(Model):
    belongs_to = ('Account',)
    has_many = ('Attribute',)


class Permission(Model):
    belongs_to = ('App', 'Group',)


class Attribute(Model):
    belongs_to = ('Identity',)


helpers.create_tables()
helpers.create_indexes()
