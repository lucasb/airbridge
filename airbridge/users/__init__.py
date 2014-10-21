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


from flask import Flask
from ..database import set_db

name = 'users'

app = Flask('airbridge')
app.config.from_pyfile('config.cfg')
app.config['APPLICATION_ROOT'] += name

set_db(app)


def run_users():
  """
  Start micro service for users module from Airbridge Paas
  """
  set_blueprints()
  app.run(host=app.config['RUN_HOST'], 
          port=app.config['RUN_PORT'], 
          use_reloader=app.config['RUN_USE_RELOADER'], 
          debug=app.config['RUN_DEBUG'])


def set_blueprints():
  from .views import user
  app.register_blueprint(user)