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

import sys
#import thread
from threading import Thread

from api.builder import create_app as build_api
from console.builder import create_app as build_console


APPS = {
    'api',
    'console'
}

config_file = '../config.cfg'


def start_app(name):
    app = eval("build_%s('%s')" % (name, config_file))
    name = name.upper()
    app.run(host=app.config['%s_RUN_HOST' % name],
            port=app.config['%s_RUN_PORT' % name],
            use_reloader=app.config['%s_RUN_USE_RELOADER' % name],
            debug=app.config['%s_RUN_DEBUG' % name])

try:
    if len(sys.argv) > 1:
        start_app(str(sys.argv[1]))
    else:
        for item in APPS:
            Thread(target=start_app, args=(item,)).start()
except Exception:
    raise Exception('Errors found in application start.')
