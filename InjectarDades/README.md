# Injectar datos

Para injectar datos propios a influxdb utilizare
un python que tendra importado una libreria de influxDB,

Tambien un scrip en bash para recolectar datos nuevos hacia un fichero
que sera canviante y posteriormente ejecutara el programa en python 
de injectar los datos a la base de datos de InfluxDB.

Este scrip se ejecutara cada 60 segundos con un crontab.

```
$ crontab -l
* * * * * /var/tmp/injeccio/scrip.sh
```
