# Documentación del Proyecto

El proyecto consiste en general en la monitorización de la infraestructura 
como por ejemplo de una empresa o entidad y lo empleare con Grafana.

En esta caso voy a explicar como montar dicha estructura con la ayuda
de **Influxdb** y **Telegraf** que forman un duo perfecto para el tratamiento de los
datos para su posterior visualización con Grafana

## Información general

* [Telegraf](https://github.com/isx27423760/projecte-franlin/blob/master/Documentation/telegraf.md): Se encarga de recolectar todos los datos que le pasamos mediante el 
            fichero de configuración **telegraf.conf**, para posteriormente informar 
            de todas las métricas recolectadas. 

* [InfluxDB](https://github.com/isx27423760/projecte-franlin/blob/master/Documentation/influxDB.md): Es el lugar donde Telegraf envía toda esta información, ya que 
			InfluxDB esta especialmente diseñado para almacenar de manera eficiente 
			una cantidad importante de información


* Grafana: Es el Dashboard que se encargara de mostrar toda la información que InfluxDB tiene 
           almacenado en las Bases de Datos en forma de gráficas que se podran configurar 
           facilmente.

## Instalación 

### Características del sistema

La instalacón se efectuara en un Fedora 27, con las siguientes caracteristicas:

```
    RAM: 16 GB
    HDD: 225 GB
    Swap: 5 GB
    System type: 64 bits
    Processor: Intel Core (TM) i7-6700 CPU @ 3.40GHz
```

### Características de los servicios

- Grafana: Versión 6.1.6 
- Telegraf: Versión 1.10.4
- InfluxDB: Versión 1.7.6

Para la instalación y puesta en marcha de los servicios ver este HowToInstall.

### Esquema de la infraestructura a montar:

![grafica](/img/graf-inf-tele.png)























