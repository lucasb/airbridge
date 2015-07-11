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

import logging

from flask import Flask
from werkzeug.utils import import_string
from console.extensions import bcrypt, db


app_name = 'console'


def create_app():
    """Initialize applcation with configs"""
    app = Flask(app_name)
    app.config.from_pyfile('config.cfg')

    configure_blueprints(app)
    configure_extensions(app)
    configure_logger(app)

    return app


def configure_logger(app):
    """Create log file to application"""
    log_filename = "%s_log" % app.config['PROJECT_NAME'] + app_name
    log_file = logging.FileHandler(
                            filename=app.config['LOG_PATH'] % log_filename)
    log_file.setFormatter(logging.Formatter(app.config['LOG_FORMAT']))
    log_level = loggin.DEBUG if app.config['CONSOLE_RUN_DEBUG'] else logging.INFO
    log_file.setLevel(log_level)
    app.logger.addHandler(log_file)


def configure_blueprints(app):
    """Register modules"""
    app.register_blueprint(
                import_string('%s.access.controllers.access' % app_name))
    app.register_blueprint(
                import_string('%s.services.controllers.services' % app_name))


def configure_extensions(app):
    """Initialize extensions"""
    bcrypt.init_app(app)
    db.init_app(app)
