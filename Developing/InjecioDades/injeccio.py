#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from influxdb import InfluxDBClient

UNIT="UNIT"                                                                                                             
LOAD="LOAD"   
ACTIVE="ACTIVE" 
SUB="SUB"       
DESCRIPTION="DESCRIPTION"

#conectar a influxdb
client = InfluxDBClient(host='localhost', port=8086)
#crear una base de dades de proba
client.create_database('pyexample')
#veure las bases de dades
client.get_list_database()

#entramos a una base de dades
client.switch_database('pyexample')

json_body = [
    {
        "measurement": "brushEvents",
        "tags": {
            "user": "Carol",
            "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
        },
        "time": "2018-03-28T8:01:00Z",
        "fields": {
            "duration": 127
        }
    },
    {
        "measurement": "brushEvents",
        "tags": {
            "user": "Carol",
            "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
        },
        "time": "2018-03-29T8:04:00Z",
        "fields": {
            "duration": 132
        }
    },
    {
        "measurement": "brushEvents",
        "tags": {
            "user": "Carol",
            "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
        },
        "time": "2018-03-30T8:02:00Z",
        "fields": {
            "duration": 129
        }
    }
]

client.write_points(json_body)


