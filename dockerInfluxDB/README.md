# InfluxDB Server 
## Proyecto 2018/2019 Franlin colque

**francs2/influxdb:server** Servidor **influxDB**. Servidor influxdb que pemite
  la conexión y la configuración de almacenamiento de los datos para posteriormente
  representarlo en **Grafana**. El servidor sera llamado **influxdb.server**

Construimos la imagen de influxdb 
```
# docker build -t "influxdb:server" .
```
Ejecutamos la imagen docker con el puerto 8086 i 8088 ya mapeado
```
# docker run --rm -p 8086:8086 -p 8088 --name influxdb.server -h influxdb.server -d influxdb:server
```




