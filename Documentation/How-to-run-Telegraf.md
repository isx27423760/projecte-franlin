# Arrancar telegraf en docker:

Telegraf es una aplicación para recopilar métricas y telemetría de aplicaciones 
y servidores y enviarlos a un almacén de datos de series temporales como InfluxDB o otra
base de datos de series temporales. 
Ejecutare telegraf en un contenedor Docker, y que pueda permitir que Telegraf recopile las 
métricas del host desde un contenedor y enviarlas a InfluxDB que se encuentra en otro contenedor.

#### Requerimientos

	1. Tener instalado Docker.
	2. Instalar InfluxDB en otro contenedor.
	3. Instalar Grafana en otro contenedor.


#### Configuración

Necesitamos el fichero por defecto de Telegraf , para poder modificarlo a nuestras necesidades.

Genermos un fichero de configuración de Telegraf ,con el siguiente comando:

```
# ./telegraf -sample-config -input-filter cpu:mem:disk:openldap -output-filter influxdb > telegraf.conf
```

Abrimos el fichero y lo editamos para que Telegraf envie las metricas a InfluxDB

```
# Configuration for sending metrics to InfluxDB
[[outputs.influxdb]]
  ## The full HTTP or UDP URL for your InfluxDB instance.
  ##
  ## Multiple URLs can be specified for a single cluster, only ONE of the
  ## urls will be written to each interval.
  # urls = ["unix:///var/run/influxdb.sock"]
  # urls = ["udp://127.0.0.1:8089"]
   urls = ["http://ip-docker:8086"]
```

Si queremos monitorizar un servidor ldap, y esta se encuentra en un docker tenemos que editar la siguiente 
linea:

```
[[inputs.openldap]]
  host = "ip-server-ldap"
  port = 389
```

**Poner en marcha el contenedor de Telgraf:**

Como Telegraf se ejecutará dentro de un contenedor, necesitamos pasar algunos recursos de host a través de 
incluir el socket docker, / proc, / sys y / etc. Esto permitirá a Telegraf recopilar datos de todo el host, 
no solo lo que es visible para el contenedor. También debemos darle al contenedor un nombre de host específico o saber la IP específica, 
ya que se pasará a InfluxDB, si no configuramos esto, se utilizará el ID del contenedor y no es lo que queremos.

```
#docker run -d --restart=always --add-host="influxdb:ip-docker" --hostname=myhostname -e "HOST_PROC=/rootfs/proc" -e "HOST_SYS=/rootfs/sys" -e "HOST_ETC=/rootfs/etc" -v $(pwd)/telegraf/telegraf.conf:/etc/telegraf/telegraf.conf:ro -v /var/run/docker.sock:/var/run/docker.sock:ro -v /sys:/rootfs/sys:ro -v /proc:/rootfs/proc:ro -v /etc:/rootfs/etc:ro telegraf
```

