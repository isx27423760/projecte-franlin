# Pruebas de injeccio de dades

## Obrir entorn grafic remotament
[isx27423760@i18 ~]$ ssh root@i04 -X

## Instalem influxdb en una maquina de clase (i04)

## Create a database using the HTTP API:

curl -i -XPOST http://localhost:8086/query --data-urlencode "q=CREATE DATABASE proves"
## borrar una base de datos 
> DROP DATABASE "NOAA_water_database"

#######
> show databases
name: databases
name
----
_internal
proves
#####


Writing data from a file:

curl -i -XPOST 'http://localhost:8086/write?db=proves' --data-binary @cpu_data.txt

##
Writen a database pirates:
#influx -import -path=pirates.txt -precision=s

Python  library 
[root@i04 influxdb-data]# dnf -y install python-influxdb







