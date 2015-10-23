Airbridge
=========

Airbridge is an API Gateway to integrate applications easily between APIs. Security control, transformation structure(from soap to rest and xml to json) become Airbridge a helpful tool to manage resources(mainly in microservices architecture), is also a converter data to integrate old services with new clients such as, mobile apps and/or Angular websites.

Modules and features:
* Console (Clients, Users, Services)
* API (URI / Version / Type)

INSTALL
-------
```
cd /path/to/airbridge
pip install -r requirements.txt
```

RUN
-------
- Specific module
```
python run.py api
```

- All modules
```
python run.py --all
```

For more options use that
```
python run.py -h
```

License
-----
The project Leafbird is licensed under the Apache license version 2.0.

Copyright 2015 Leafbird

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
