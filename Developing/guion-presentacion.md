# Presentacion

(About Me)

## Objectius


## Introduccion

		Grafana 
		
		InfluxDB
		
		Telegraf

## 

(telegraf)

-- Metricas

Que son las metricas:
de acuerdo con la definicion tecnica es un Un sistema o estándar de medidas.
pero prefiero definirlo como basicamente como una propiedad que medimos.
no es un como un snapshot como tal pero es algo que recogemos y los subimos a una coleccion 

--Anatomia de la medida.

Mostrar un ejemplo simple de representacion de una metrica:


cpu_usr 98 152923923 process=ie.exe
cpu_usr = name 
98=valor
152923923 = timestamp

process=ie.exe  == metadatos (son aquellos datos que hablan de los datos ) o sea describen el contenido de los archivos  o la informacion de los mismos.


(Influx DB) pre-iniciación.

---time series databases.
que es (wiki)

una metrica:
db.connections 31 141436454  server=myhost type=open

Poner la tabla de metrics de una base de datos de influxdb:

y tags-value:



En algun lugar tenemos que poner estos datos:
  - Menos esquemas 
  - Facil demontar y mantener
  - Alto rendimineto
  - tiene gestión de retención de datos
  
---

InfluxDB  Iniciación 

Que es ?
Distribucion open source, es una base de datos de serie de tiempo.

Soporta:
	- HTTP API.
	- SQL-like query language.
	- Buena seleccion de la libreria de clientes y plugins
	- Data retention policy

Por que me gusta?
	- Flexibilidad en el nombre de las metricas (no tines que estar poniendo tu los tags i todo eso)
	- No limitacion en las columnas.
	- Facil de manejar, una buena documentacion.
	- Presicion  de tiempo en milisegundos.
---	
Ejemplo de hacer run al  servidor infludb
 - esto es todo el texto que sale cuando ejecutamos el servidor influxdb
(Imagen de influxdb)


---
Config
Mostrat el fichero de configuracion y explicar un poco
 
---

hTTP API 
 (poner una imagen API de crear una base de datos)
 (poner una imagen API crear valores)
 (poner una imagen API borrar una tabla) no necesitas autenticacion de query

-- 

SQL-like Query Language:

Sintaxis general :
 - List Series 
 - Select ... From ...Where ... Group by ....LIMIT
 - Delete From ... Where....
 - Drop series

Seleccionando datos:
imagen de ordenes de influxDB:  -- To puedes hacer busquedas de presicion de milisegundos.

--
Aggregate Functions

COunt, sum, min , max , mean 

Temas mas avanzados: (lo comento porque son muy dificiles)

 - Seguridad - cluster admin, database admin, data base user
 - Clustering y replicacion
 - Retencion de datos.

---

Grafana 

Que es ?


---
Que es lo que me gusta ?
 
 - autocontenido y facil de montar.
 - detector de metricas
 - facil de compartir (SMTP, snapshot / dashboard)
 - Acces control (LDAP)
 - Admite certificados.
 - Team perfecto con InfluxDB
 - Mejor que otras herraminetas.
 
----
Imagen de richo en grafica


---
Imagen de Query editor

---
Que recoger
	












############################

Que es monitoreo?

Un monitorización es la herramineta y proceso que mide y administra nuestros sistemas

Por que es necesario la monitorización?

* disponibilidad (si esta up or down)
* Deteccion  de fallos. (si el servidor esta funcionando correctamente)
* planificación de capacidades(ver si money)
* Alertas(avisar cualquier imprevisto)

componentes de una monitorización

* Dato(medida)
* Recolector
* Almacenamiento
* Herraminetas de Visualización


Que es Grafana?

muchas origenes de almacenamiento: Graphite influxdb Prometheus Elastichsearch

pros:
	* Open Source
	* Web based
	* Support Windows installation
	* Muchos Origenes de datos.
	* Facil de utilizar y brillante
	* Control de Acceso amplio


