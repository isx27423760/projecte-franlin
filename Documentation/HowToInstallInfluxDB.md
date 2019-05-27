# Instalación de InfluxDB

Como root tenemos que ejecutar las siguientes ordenes para instalar InfluxDB
en nuestro sistema fedora27:

* Instalar paquete de  InfluxDB .

	En primer lugar debemos agregar el repositorio de InfluxDB a nuestra maquina.
```
#vim /etc/yum.repos.d/influxdb.repo
[influxdb]
name=InfluxDB Repository - RHEL 
baseurl = https://repos.influxdata.com/rhel/7/x86_64/stable/
enabled = 1
gpgcheck = 1
gpgkey = https://repos.influxdata.com/influxdb.key
```
* Después instalamos el paquete:
	```
	#dnf -y install influxdb
	```
* Después Arrancamos el servicio InfluxDB:
	```
	#systemctl start influxdb
	```
* Habilitar la arrancada por defecto de InfluxDB.
	```
	#systemctl enable influxdb
	```

Por defecto el puerto HTTP es el 3000.
El destino de los logs de grafana esta ubicado en /var/log/grafana.

Si da problemas de Firewall aplicamos la siguiente orden para
abrir el puerto de grafana:

```
#firewall-cmd --add-port=3000/tcp --permanent
#firewall-cmd --reload
```
