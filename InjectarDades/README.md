# Injectar datos

Para injectar datos a influxdb utilizare
un scrip python que tendra importado una libreria de influxDB, para
analizar el comando **systemctl**, que que es el encargado de 
centralizar el manejo del sistema, para poder ver el estado de todos
los servicios que tenemos instalado en nuestro ordenador. 

Para poder utilizar la libreria de python antes tienes que descargalo.

```
#dnf -y install python-influxdb
```

La orden **systemctl** muestra el siguiente output:

```
$systemctl
  UNIT                                                                                        LOAD   ACTIVE SUB       DESCRIPTION
  gpm.service                                                                                 loaded active running   Console Mouse manager           
● httpd.service                                                                               loaded failed failed    The Apache HTTP Server
....more lines.........
```

Tambien un scrip en bash para recolectar datos nuevos hacia un fichero
que sera mutable y posteriormente ejecutara el programa en python 
de injectar los datos a la base de datos de InfluxDB.

Este scrip se ejecutara cada 60 segundos con un crontab,lo que significa
que cada minuto se injectaran datos del estado de los servicios a InfluxDB,
evidentemente el servidor influxdb previamente tiene que estar puesto en marcha.

```
$ crontab -l
* * * * * /var/tmp/injeccio/scrip.sh
```
