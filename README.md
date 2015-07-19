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
