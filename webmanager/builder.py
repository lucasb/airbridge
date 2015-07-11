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

from flask import Flask

from werkzeug.utils import import_string

from airbridge.common.database import set_db


def create_app(module):

    app = Flask('airbridge')
    app.config.from_pyfile('config.cfg.py')

    set_db(app)

    blueprint = import_string('airbridge.{0}.views.{0}'.format(module))
    app.register_blueprint(blueprint)

    return app
