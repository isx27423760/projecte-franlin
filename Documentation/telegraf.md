# Telegraf

Telegraf es un servicio que recopila y envía métricas, datos de diferentes sistemas. 
Puede recopilar datos del sistema en el que se ejecuta, como uso de disco, RAM, CPU, 
carga del sistema, conexiones y muchos más, e incluye además una creciente 
lista de plugins de entrada, como apache, consul, couchDB, Docker, Elasticsearch, 
Fluentd, HAproxy, http POST, entre otros. Su salida la envía por lo general a una base 
de datos InfluxDB, y es esta capacidad la que aprovecharemos en este tutorial.

Por lo tanto,**Telegraf** es un agente ligero de recolección de datos, esta escrito en go,
su principal objectivo es la de enviar telemetria del sistema o de un server 
a **InfluxDB** , influxDB no tiene por que estar en el mismo host que telegraf
pueden estar en distintos hosts.

### Formatos de Output Data 

Además de los formatos de datos específicos de salida,Telegraf admite un conjunto 
de formatos de datos estándar que se pueden seleccionar al configurar muchos complementos de salida.


* InfluXDB (que es la que utilizare para enviar directamente las metricas en tiempo real)
* JSON 

y tambien hay formatos como **Graphite,SplunkMetric,Carbon2,Wavefront**



