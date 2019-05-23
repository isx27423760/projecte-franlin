# Instalación de Grafana

Como root tenemos que ejecutar las siguientes ordenes para instalar grafana
en nuestro systema fedora27:

* Instalar paquete de  grafana .

	En primer lugar debemos agregar el repositorio de grafana a nuestra maquina como root.
```
#vim /etc/yum.repos.d/grafana.repo
[grafana]
name=grafana
baseurl=https://packages.grafana.com/oss/rpm
repo_gpgcheck=1
enabled=1
gpgcheck=1
gpgkey=https://packages.grafana.com/gpg.key
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
```
	Despues instalamos el paquete:
	```
	#dnf -y install grafana
	```
* Despues Arrancamos el servicio grafana:
	```
	#systemctl start grafana-server
	```
* Habilitar la arrancada por defecto de grafana.
	```
	#systemctl enable grafana-server
	```
