#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from influxdb import InfluxDBClient

# ~ f=open("systemctl.txt","r")
# ~ f.readline(3);
# ~ kk=""
# ~ for line in f:
	# ~ print line,
# ~ f.close()

vacio=0

lineas = []

f = open("kkk.tt",'r')
f.readline()[2:]
for line in f:
	if line == "\n":
		vacio += 1
		break
	lineas = line.split()
	print(lineas)
	#print line,
f.close()


