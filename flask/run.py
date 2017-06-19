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
import argparse
import logging

from threading import Thread

from api.builder import create_app as build_api
from console.builder import create_app as build_console


# Constants
CONFIG_FILE = '../config.cfg'
MODULES = { 'api', 'console' }


# Arguments to start app
parser = argparse.ArgumentParser(prog='airbridge',
                                 description='Airbridge API Gateway runner.')

parser.add_argument('module', type=str, nargs='?', default=None,
                    help='name of specific module to run')

parser.add_argument('-a', '--all', dest="all", action='store_const',
                    const=True, default=False, help='run all apps')
parser.add_argument('-d', '--debug', dest="debug", action='store_const',
                    const=True, default=False,
                    help='change default config to debug')
parser.add_argument('--config', dest='config', type=str, default=CONFIG_FILE,
                    help='path to config file', metavar='')


# Run
def run(args):
    "Run application with config and arguments set"

    def start_app(name):
        "Start specific app for a module"
        app = eval("build_%s('%s')" % (name, args.config))
        name = name.upper()
        debug = args.debug if args.debug else app.config['%s_RUN_DEBUG' % name]
        app.run(host=app.config['%s_RUN_HOST' % name],
                port=app.config['%s_RUN_PORT' % name],
                use_reloader=app.config['%s_RUN_USE_RELOADER' % name],
                debug=debug)

    try:
        if not args.all and args.module is not None:
            start_app(args.module)
        elif args.all and args.module is None:
            for item in MODULES:
                Thread(target=start_app, args=(item,)).start()
        else:
            sys.exit('error: A module name or arg --all are required.')
    except:
        sys.exit('error: Application found an unexpected error to start.')


run(parser.parse_args())
