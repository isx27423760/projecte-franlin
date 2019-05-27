# Instalación de Telegraf

Como root tenemos que ejecutar las siguientes ordenes para instalar Telegraf
en nuestro sistema fedora27:

* Instalar paquete de  InfluxDB.

	En primer lugar debemos agregar el repositorio de InfluxDB a nuestra maquina.
```
#vim /etc/yum.repos.d/influxdb.repo
[influxdb]
name = InfluxDB Repository - RHEL 
baseurl = https://repos.influxdata.com/rhel/7/x86_64/stable/
enabled = 1
gpgcheck = 1
gpgkey = https://repos.influxdata.com/influxdb.key
```
* Después instalamos el paquete:
	```
	#dnf -y install telegraf
	```
* Después arrancamos el servicio Telegraf:
	```
	#systemctl start telegraf
	```
* Habilitar la arrancada por defecto de Telegraf.
	```
	#systemctl enable telegraf
	```

