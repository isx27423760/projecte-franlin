#!/usr/bin/env python
#
from influxdb import InfluxDBClient
import json

#conectar a influxdb
client = InfluxDBClient(host='localhost', port=8086)
#entramos a una base de dades
client.switch_database('systemctl')

# lista = ['fwupd.service', 'loaded', 'active', 'running', 'Firmware', 'update', 'daemon']
def my_function(lista):
    '''funcion de tratamiento de lista'''
    LOAD=-1
    ACTIVE=-1
    SUB=-1
    if lista[0] == '\xe2\x97\x8f':
        if lista[2] == "failed":
            LOAD = 0
        else:
            LOAD = 1
        if lista[3] == "failed":
            ACTIVE = 0
        else:
            ACTIVE = 2
        if lista[4] == "failed":
            SUB = 0
        else:
            SUB = 3
        my_json_string = json.dumps([{"measurement":lista[1],"tags":{"servei":lista[1]},"fields":{"LOAD": LOAD,"ACTIVE":ACTIVE,"SUB":SUB}}])
        #print my_json_string
    else:
        if lista[1] == "failed":
            LOAD = 0
        else:
            LOAD = 1
        if lista[2] == "failed":
            ACTIVE = 0
        else:
            ACTIVE = 2
        if lista[3] == "failed":
            SUB = 0
        else:
            SUB = 3
        my_json_string = json.dumps([{"measurement":lista[0],"tags":{"servei":lista[0]},"fields":{"LOAD": LOAD,"ACTIVE":ACTIVE,"SUB":SUB}}])
    return my_json_string

#----------------------------------------------------------------------------------------------------------------------------------------------

vacio=0
lineas = []
ll = []
str1="["
str2="]"
f = open("systemctl.txt",'r')
f.readline()[2:]
for line in f:
	if line == "\n":
		vacio += 1
		break
	lineas = line.split()
        ll =  my_function(lineas)
        #ll = str1+ my_function(lineas)+str2
	#client.write_points(ll)
f.close()
#client.write_points(ll)

json = ll[4:]

print json

#json1 = [{"fields": {"LOAD": 1, "ACTIVE": 2, "SUB": 3}, "tags": {"servei": "gdm.service"}, "measurement": "gdm.service"}]

#client.write_points(json)

#print json

#### ERRORS####################



# ~ [root@i04 influxdb-data]# python prova.py 
# ~ [{"fields": {"LOAD": 1, "ACTIVE": 0, "SUB": 0}, "tags": {"servei": "httpd.service"}, "measurement": "httpd.service"}]
# ~ Traceback (most recent call last):
  # ~ File "prova.py", line 74, in <module>
    # ~ client.write_points(json)
  # ~ File "/usr/lib/python2.7/site-packages/influxdb/client.py", line 468, in write_points
    # ~ tags=tags, protocol=protocol)
  # ~ File "/usr/lib/python2.7/site-packages/influxdb/client.py", line 532, in _write_points
    # ~ protocol=protocol
  # ~ File "/usr/lib/python2.7/site-packages/influxdb/client.py", line 300, in write
    # ~ data = make_lines(data, precision).encode('utf-8')
  # ~ File "/usr/lib/python2.7/site-packages/influxdb/line_protocol.py", line 125, in make_lines
    # ~ point.get('measurement', data.get('measurement'))))
# ~ AttributeError: 'str' object has no attribute 'get'



#	Insertant manualment si funciona:
#		> show databases
#	name: databases
#	name
#	----
#	_internal
#	proves
#	pirates
#	systemctl
#	pyexample
#	> use systemctl
#	Using database systemctl
#	> show measurements 
#	> show measurements 
#	> show measurements 
#	> show measurements 
#	> show measurements 
#	name: measurements
#	name
#	----
#	gdm.service
#	> select * from "gdm.service"
#	name: gdm.service
#	time                ACTIVE LOAD SUB servei
#	----                ------ ---- --- ------
#	1558692039760804430 2      1    3   gdm.service
