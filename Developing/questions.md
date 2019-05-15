# Questions

- **Quien genera los datos?**

	Telegraf es el encargado de generar los datos , apartir del proceso de recopilacion de los datos de un
	determinado servicio o recurso.

- **Quien recoge los datos?**

	InfluxDB , que es la Base de datos escalable para metricas, time-series, y eventos en tiempo real.

- **Quien los muestra?**

	Grafana, es la encargada de mostrar en diferentes diagramas la informacion recibida de InfluxDB.

- **El fichero en row de los datos se puede acceder/editar?**

	Telegraf es capaz , aparte de enviar directamente los datos a InfluxDB, de permitir
	genera un fichero con el contenido de todos los datos.

- **Como se organiza la información?**

	La informacion se organiza en influxDB en  datos de series 
	de tiempo que son simplemente mediciones o eventos que se rastrean, monitorean, muescan y agregan a lo largo del tiempo.
	Esto podría ser métricas del servidor, monitoreo del rendimiento de la aplicación, datos de red, datos de sensores, eventos, clics,etc.
	
- **como se accede a ella ?**

	Como una base de datos normal, **use dbs**

- **Las metricas en Telegraf , como se explica ?**

	Las métricas de Telegraf son la representación interna utilizada para modelar 
	datos durante el procesamiento. Estas métricas se basan en gran medida en el modelo de datos InfluxDB 
	y contienen cuatro componentes principales: **Measurement name,Tags,Fields y Timestamp.**
	
	
	Este tipo de indicador solo existe en la memoria y debe convertirse a una representación concreta para poder 
	ser transmitido o visto. Telegraf proporciona formatos de datos de salida (también conocidos como serializadores) 
	para estas conversiones. El serializador predeterminado de Telegraf se convierte al InfluxDB Line Protocol, 
	que proporciona un alto rendimiento y un mapeo directo uno a uno de las métricas de Telegraf.

- **Telegraf es configurable , cuantos campos si es que es configurable?**



- **Que son las series en influxdb?**

	InfluxDB, una serie es la recopilación de datos que comparten una política de retención, medición y conjunto de etiquetas. 

- **Diferencia entre series y medidas en nifluxDB ?**

	La medición actúa como un contenedor para etiquetas, campos y la columna de tiempo, y el nombre de la medición es la descripción 
	de los datos que se almacenan en los campos asociados. Los nombres de medición son cadenas y, para cualquier usuario de SQL, una 
	medición es conceptualmente similar a una tabla. La única medida en la muestra de datos es el censo. 

	Una sola medida puede pertenecer a diferentes políticas de retención. 
	Una política de retención describe cuánto tiempo InfluxDB conserva los datos (DURACIÓN) y cuántas copias de estos datos se almacenan en el clúster (REPLICACIÓN).

- **diferencias entre tag keys y field keys?**
	InfluxDB permite especificar fields y tags, siendo ambos pares key / value, donde la diferencia es que los tags se indexan automáticamente.

- **Que son las metricas?**
	una propiedad que medimos.



## Telgraf :


Telegraf es un agente para recopilar, procesar, agregar y escribir métricas.
Los objetivos de diseño son tener una huella de memoria mínima con un sistema de 
complementos para que los desarrolladores de la comunidad puedan agregar fácilmente el soporte para recopilar métricas.
Telegraf es impulsado por complementos y tiene el concepto de 4 tipos de complementos distintos:
	
	* Input plugins : recopilar métricas del sistema, servicios o API de terceros
	* Processor Plugins: Transformar, decorar y / o filtrar métricas.
	* Aggregator Plugins: crean métricas agregadas (por ejemplo, media, mínima, máxima, cuantiles, etc.)
	* Output Plugins: escribir métricas a varios destinos
	




