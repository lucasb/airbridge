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

#from fleegme.common.extensions import init_db, init_bcrypt, init_api


def create_app(module=None):

    # Initialize applcation
    app = Flask('api')
    app.config.from_pyfile('config.cfg')

    # Register modules
    if module:
        if module not in app.config['APP_MODULES']:
            msg = "Attribute '{0}' is not a valid module.".format(module)
            raise AttributeError(msg)
        app.register_blueprint(__build_blueprint(module))
    else:
        for module in app.config['APP_MODULES']:
            app.register_blueprint(__build_blueprint(module))

    # Initialize extensions
    init_bcrypt(app)
    init_db(app)
    init_api(app)

    return app


def __build_blueprint(module):
    return import_string('api.{0}.controllers.{0}'.format(module))
