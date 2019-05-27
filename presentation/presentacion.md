% Proyecto fin de ciclo Grafana
% Franlin Colque
% 2019/05/22

---

## Objetivos

* Dar a conocer las bases de una monitorización.

* Colección y visualización de métricas con Telegraf, InfluxDB y Grafana.

* Mostrar la sintaxis de las tecnologías utilizadas.

* Ejemplo de uso con servidores LDAP y HTTP.

* Implementación en Dockers.

---

## Introducción

* Grafana

	Grafana es una herramienta de código abierto. Se utiliza para visualizar series de datos en el análisis de infraestructuras y aplicaciones.

* InfluxDB

	Influxdb es un servidor de base de datos de series de tiempo (timeseries), ideal para logs o datos para gráficas que se generen en vivo.

* Telegraf

	Telegraf es un agente ligero de recolección de datos, escrito en Go, cuyo principal propósito es enviar telemetría o métricas del sistema o de la aplicación a InfluxDB.

---

## Métricas

De acuerdo con la definición técnica es sistema o estándar de medidas.
Pero prefiero definirlo como básicamente como una propiedad que medimos.
No es un como un snapshot como tal pero es algo que recogemos y los subimos a una colección. 

---

## Anatomía de una Métrica

![metrica](metrica.jpg)

---

## Métricas Ejemplo

Antes:

```
collectd.dfs.df.srv-node-dfs10.df-complex.used
```

Después de Telgraf:

```
{
	server: dfs1
	what: diskspace
	mountpoint: srv/node/dfs10
	unit: B
	type: used
	metric_type: gauge
}
```

---


## telegraf

* Recogida de los datos, de diferentes fuentes.
* Procesado de los datos, para transformar y formatear los mismos.
* Estadística de los datos como media, mínimo, máximo, etc.
* Salida de los datos, para redistribuir los mismos a distintas aplicaciones.


---

## Donde almacenar estas métricas?

  - Menos esquemas 
  - Fácil de montar y mantener
  - Alto rendimiento
  - Gestión de retención de datos

---

## InfluxDB

Distribución open source, es una base de datos de serie de tiempo.

Una base de datos de series de tiempo (TSDB) es un sistema de software que está 
optimizado para el manejo de datos de series de tiempo, matrices de números 
indexados por tiempo (una fecha o un rango de fecha y hora).

Puertos:
- 8086
- 8088 


---

## Características

- HTTP API.
- SQL-like query language.
- Buena selección de la librería de clientes y plugins.
- Data retention policy


---

## Por que la elección de InfluxDB?

* Flexibilidad en el nombre de las métricas.
* Sin limitación en las columnas.
* Fácil de manejar, una buena documentación.
* Presición  de tiempo en milisegundos.

---

## SQL-like Query Language

Sintaxis general:

- List Series 
- Select ... From ...Where ... Group by ....LIMIT
- Delete From ... Where....

Además dispone de funciones:

* COUNT(), DISTINCT(), MEDIAN(), MAX(), MIN(), SUM(),etc.

---

## Autenticación

- TLS 
	```
	[http]
	enabled = true
	bind-address = ":8086"
	auth-enabled = true # ✨
	log-enabled = true
	https-certificate = "/etc/ssl/influxdb.pem"
	```
- Cuenta de usuario
	```
	#influx
	> CREATE USER franlin WITH PASSWORD 'xxxxxx' WITH ALL PRIVILEGES
	```
	```
	#influx
	Connected to http://localhost:8086 version 1.4.x
	InfluxDB shell 1.4.x
	> auth
	username: franlin
	password:
	>
	```

---

## Grafana

Características principales:
- Open Source.
- Web based.
- Soporta Windows.
- Muchos orígenes de datos.
- Gráficos elegantes.
- Paneles dinámicos, reutilizables y altamente extensible.
- Autenticación a través de LDAP, Google Auth, Grafana.com, Github y Gitlab.
- Comparte de datos y cuadros de mando entre diferentes hosts.
- TLS.

---

## Recursos y servicios

Recursos: 
- CPU
- RAM
- Disk
Servicios:
- OpenLDAP
- HTTP

---

## Servidor LDAP

Configurar slapd.conf:
```
database monitor
access to *
     by dn.exact="cn=Manager,dc=example,dc=com
     by * none
```

---

## Comprobación

```
[root@localhost]$ ldapsearch -x -LLL -D  'cn=Manager,dc=grafana,dc=org' \
	-w secret  -b 'cn=Monitor' -s base '(objectClass=*)' '*' '+'

dn: cn=Monitor
objectClass: monitorServer
structuralObjectClass: monitorServer
cn: Monitor
creatorsName:
modifiersName:
createTimestamp: 20190527185826Z
modifyTimestamp: 20190527185826Z
description: This subtree contains monitoring/managing objects.
description: This object contains information about this server.
description: Most of the information is held in operational attributes, which 
 must be explicitly requested.
monitoredInfo: OpenLDAP: slapd 2.4.45 (Dec  6 2017 14:25:36)
entryDN: cn=Monitor
subschemaSubentry: cn=Subschema
hasSubordinates: TRUE
```
---

## Servidor HTTP

Configuramos el fichero httpd.conf
``` 
	ExtendedStatus On
	<Location "/server-status">
		SetHandler server-status
		Order allow,deny
		Allow from all
	</Location>
```

---

## Docker Compose

Este mecanismo permite utilizar varias imágenes y comunicarlas, para 
obtener los requisitos necesarios para hacer funcionar nuestra estructura
de gestión.

      version: "3"
      services:
        #Servidor Grafana
        grafana:
          build:
            context: $PWD/dockerGrafana/
            dockerfile: Dockerfile
          container_name: grafana.server
          hostname: grafana.server
          ports:
            - "3000:3000"
          volumes:
          # Data persistency
            - "grafana_data:/usr/share/grafana/data"
          networks:
           - mynet

---

## Conclusiones

componentes de una monitorización

* Dato(medida)
* Recolector
* Almacenamiento
* Herramientas de Visualización

Un monitorización es la herramienta y proceso que mide y administra nuestros sistemas.

* disponibilidad (si esta up or down)
* Detección  de fallos. (si el servidor está funcionando correctamente)
* planificación de capacidades(ver si money)
* Alertas(avisar cualquier imprevisto)







