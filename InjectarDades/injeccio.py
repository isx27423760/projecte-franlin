#!/usr/bin/env python
#
from influxdb import InfluxDBClient
import json

#conectar a influxdb
client = InfluxDBClient(host='localhost', port=8086)
#crear una base de dades de proba
client.create_database('systemctl')
#entramos a una base de dades
client.switch_database('systemctl')

# functions
def load_system(load):
	if load=="failed":
		load=-1
	else:
		load=1
	return load
def active_system(active):
	if active=="failed":
		active=-2
	else:
		active=2
	return active
def sub_system(sub):
	if sub=="failed":
		sub=-3
	else:
		sub=3
	return sub
#------------------------------------------------------------------------
#LOAD   = Reflects whether the unit definition was properly loaded.
#ACTIVE = The high-level unit activation state, i.e. generalization of SUB.
#SUB    = The low-level unit activation state, values depend on unit type.

vacio=0
lineas = []
ll = []

f = open("systemctl.txt",'r')
f.readline()[2:]
for line in f:
	if line == "\n":
		vacio += 1
		break
	lineas = line.split()
	if lineas[0] == '\xe2\x97\x8f':
		desc= " ".join(lineas[5:])
		json = [{"measurement":lineas[1],"tags":{"UNIT":lineas[1]},"fields":{"LOAD":load_system(lineas[2]),"ACTIVE":active_system(lineas[3]),"SUB":sub_system(lineas[4]),"Decription":desc}}]
	else:
		desc= " ".join(lineas[4:])
		json = [{"measurement":lineas[0],"tags":{"UNIT":lineas[0]},"fields":{"LOAD":load_system(lineas[1]),"ACTIVE":active_system(lineas[2]),"SUB":sub_system(lineas[3]),"Decription":desc}}]
	client.write_points(json)
f.close()


