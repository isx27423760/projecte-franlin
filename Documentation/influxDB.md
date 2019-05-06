# InfluxDB

Influxdb es un servidor de base de datos de series de tiempo (timeseries), 
ideal para logs o datos para gráficas que se generen en vivo.

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
