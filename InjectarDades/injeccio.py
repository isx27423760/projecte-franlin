#!/usr/bin/env python
#nombre:franlin 
#curso:hisx2
#año: 2019
#descripcion: programa para injectar los datos extrados y posteriormente
#			tratados y enviados a la base de datos influxdb.
#-----------------------------------------------------------------
from influxdb import InfluxDBClient
#conectarse a InfluxDB
client = InfluxDBClient(host='localhost', port=8086)
#crear la base de datos (>CREATE DATABASE )
client.create_database('systemctl')
#conectarse a la base de datos creada anteriormente (> use DATABASE)
client.switch_database('systemctl')
# functions 
def load_system(load):
	'''If load is failed in systemctl put -1 ,If not 1'''
	if load=="failed":
		load=-1
	else:
		load=1
	return load
def active_system(active):
	'''If active is failed in systemctl put -2 ,If not 2'''
	if active=="failed":
		active=-2
	else:
		active=2
	return active
def sub_system(sub):
	'''If sub is failed in systemctl put -3 ,If not 3'''
	if sub=="failed":
		sub=-3
	else:
		sub=3
	return sub
#--------------------------------------------------------------------------
# $man systemctl
#LOAD   = Reflects whether the unit definition was properly loaded.
#ACTIVE = The high-level unit activation state, i.e. generalization of SUB.
#SUB    = The low-level unit activation state, values depend on unit type.
#-------------------------------------------------------------------------
item=0
lineas = []
f = open("/var/tmp/injeccio/systemctl.txt",'r')
f.readline()[2:]
for line in f:
	if line == "\n":
		item += 1
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


