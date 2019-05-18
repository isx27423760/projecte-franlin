# InfluxDB

Influxdb es un servidor de base de datos de series de tiempo (timeseries), 
ideal para logs o datos para gráficas que se generen en vivo, ademas tiene un rendimiento
importante ante la entrada de grandes datos.

Programado en go permite la interacción via API HTTP(S) (JSON) e interficie web y los datos de gestionan con un lenguaje similar a SQL.

**Conceptos basicos de InfluxDB**

* **Database:** es el contenedor lógico que contiene series temporales, usuarios, políticas de retención ,etc.

* **Measurement:** es la estructura en la que se almacenan los datos. En el ejemplo anterior sería la tabla «host_performance»

* **Timestamp:** todo dato almacenado en InfluxDB tiene asociado la fecha y hora. 
				InfluxDB almacena la fecha en formato UTC siguiendo el RFC3339. En el ejemplo anterior, el timestamp se indica en la columna «time»

* **Field:** es el par clave-valor que almacena los valores de datos en InfluxDB y siempre están asociados a un timestamp (columnas sin indexar en SQL). 
Son campos no indexados, y que pueden tener datos de tipo strings, floats, integers o booleans. 
Es obligatorio contar con Fields en nuestra infraestructura de datos. 
En el ejemplo anterior, «cpu_usage» y «mem_usage» son fields. Tenemos Field-keys (cpu_usage y mem_usage) y Field-values (10, 30, 50, 40 …)

* **Tags:**  es el par-clave-valor que almacena valores de metadatos (columnas indexades en SQL).
Son campos indexados y almacenados como strings. Son opcionales en la infraestructura de datos. En el ejemplo anterior,  «host» y «cluster» son Tags. Tenemos Tags-keys (host y cluster) y Tags-values (esxi01.localdomain.local, esxi02.localdomain.local, cluster01…)

* **Point:** es el conjunto de valores de fields y tags asociados a un timestamp. Podríamos asociarlo a un registro de la tabla. (Similar a las filas de SQL) 

## Caracteristicas de influxDB

Algunas de las características que definen InfluxDB son las siguientes:

-  Se asume que si se envía el mismo dato varias veces, es el mismo dato por lo que se aplica la 
política de resolución de conflictos (de forma resumida, si son exactamente los mismos datos de tags set, 
field set, timestamp, se sobreesciben los valores en field set con los datos del último Point) por lo que en ciertos casos, se pueden perder datos.

- El borrado de datos es una situación extraña. Normalmente se borran datos antiguos. Se limita la funcionalidad de borrado para incrementar las de escritura y lectura

- La actualización de datos también es una situación poco común, por lo que su funcionalidad está restringida.

- La mayoría de los datos tienen timestamps recientes y se guardan en orden ascendente para mejorar el rendimiento.

- La base de datos puede gestionar un gran volumen de lecturas y escrituras, priorizandolas sobre la vista de los datos.

- No está soportado el uso de joins entre tablas.

- Los puertos InfluxDB en el interfaz web de cliente (8083) y el del API de la propia base de datos (8086).

### Ejemplo de ordenes basicas de ejecucion en InfluxDB

Primero ponemos en marcha el servidor con el siguiente comando:
```
# /usr/bin/influxd -pidfile /var/run/influxdb/influxd.pid -config /etc/influxdb/influxdb.conf

 8888888           .d888 888                   8888888b.  888888b.
   888            d88P"  888                   888  "Y88b 888  "88b
   888            888    888                   888    888 888  .88P
   888   88888b.  888888 888 888  888 888  888 888    888 8888888K.
   888   888 "88b 888    888 888  888  Y8bd8P' 888    888 888  "Y88b
   888   888  888 888    888 888  888   X88K   888    888 888    888
   888   888  888 888    888 Y88b 888 .d8""8b. 888  .d88P 888   d88P
 8888888 888  888 888    888  "Y88888 888  888 8888888P"  8888888P"

2019-05-09T09:48:00.097569Z	info	InfluxDB starting	{"log_id": "0FI~iptG000", "version": "1.7.6", "branch": "1.7", "commit": "01c8dd416270f424ab0c40f9291e269ac6921964"}

.............more lines ....................................................
```
Luego entramos dentro del sell del servidor para realizar modificaciones,consultas,etc.

```
[root@56f4bbfcf5ce /]# influx
Connected to http://localhost:8086 version 1.7.6
InfluxDB shell version: 1.7.6
Enter an InfluxQL query
> 
```

- Create database : para crear una base de datos en influxdb 
	ejecutamos la siguiente orden.
	
	```
	> CREATE DATABASE test
	```

- Mostrar las base de datos que tenemos en nuestro servidor.

	```
	> SHOW DATABASES
	name: databases
	name
	----
	_internal
	statsdemo
	test
	```
- Entramos en la nueva base de datos creado anteriormente.

	```
	> USE test
	Using database test
	```
- Inertamos datos de prueba 

	```
	INSERT cpu,host=serverA value=0.64
	```
- El comando de Insert no produce ningún output, pero deberíamos poder 
  ver los datos cuando realizas una consulta:
  
  ```
	> select * from cpu
	name: cpu
	time                host    value
	----                ----    -----
	1557396283942172538 serverA 0.64

## Conceptos a tener en cuenta de la base de datos:

```
        1. show databases        show database names
        2. show series           show series information
        3. show measurements     show measurement information
        4. show tag keys         show tag key information
        5. show field keys       show field key information
```

## Diferencias entre InfluxDB i una base de datos SQL

InfluxDB está hecho para trabajar con datos de series de tiempo. 
Las bases de datos SQL pueden manejar series de tiempo, pero no se crearon 
estrictamente para ese propósito. 
En resumen, InfluxDB está diseñado para almacenar un gran volumen de datos de 
series de tiempo y realizar análisis en tiempo real de esos datos.

En InfluxDB no tiene que definir esquemas por adelantado.

En Cuanto a la estructura :

```

        SQL table                                           #  InfluxDB measurenmets (table)
                                                            #
+---------+---------+---------------------+--------------+  #  name: foodships    
| park_id | planet  | time                | #_foodships  |  #  tags: park_id=1, planet=Earth
+---------+---------+---------------------+--------------+  #  time                     #_foodships
|       1 | Earth   | 1429185600000000000 |            0 |  #  ----                     ------------
|       1 | Earth   | 1429185601000000000 |            3 |  #  2015-04-16T12:00:00Z     0
|       1 | Earth   | 1429185602000000000 |           15 |  #  2015-04-16T12:00:01Z     3
|       1 | Earth   | 1429185603000000000 |           15 |  #  2015-04-16T12:00:02Z     15
+---------+---------+---------------------+--------------+  #  2015-04-16T12:00:03Z     15

```
En resúmen:

- Una medida(measurenmets) en InfluxDB es similar a una tabla de SQL
- Los tags(etiquetas) InfluxDB (park_id y planet) son como columnas indexadas en una base de datos SQL.
- Los fields(campos) de InfluxDB (#_foodships) son como columnas no indexadas en una base de datos SQL.
- Los points(puntos) en InfluxDB (por ejemplo, 2015-04-16T12: 00: 00Z 0) son similares a las filas de SQL.




