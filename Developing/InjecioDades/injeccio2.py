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

json_body = [{"fields": {"LOAD": 1, "ACTIVE": 2, "SUB": 3}, "tags": {"servei": "fwupd.service"}, "measurement": "fwupd.service"},
            {"fields": {"LOAD": 1, "ACTIVE": 0, "SUB": 0}, "tags": {"servei": "httpd.service"}, "measurement": "httpd.service"}]

client.write_points(json_body)
