% Proyecto fin de ciclo Grafana
% Franlin Colque
% 2019/05/22

---

## Objetivos

* Dar a conocer las bases de una monitorización.

* Colección y visualización de métricas con Telegraf, InfluxDB y Grafana.

* Mostrar la sintaxis de las tecnologias utilizadas.

* Ejemplo de uso con servidores LDAP y HTTP.

* Implementación en Dockers.

---

## Introducción

* Grafana

	Grafana es una herramienta de código abierto. Se utiliza para visualizar series de datos en el análisis de infraestructuras y aplicaciones.

* InfluxDB

	influxdb es un servidor de base de datos de series de tiempo (timeseries), ideal para logs o datos para gráficas que se generen en vivo

* Telegraf

	Telegraf es un agente ligero de recolección de datos, escrito en Go, cuyo principal propósito es enviar telemetría o métricas del sistema o de la aplicación a InfluxDB

---

## Métricas

De acuerdo con la definición técnica es sistema o estándar de medidas.
Pero prefiero definirlo como basicamente como una propiedad que medimos.
no es un como un snapshot como tal pero es algo que recogemos y los subimos a una colección. 

---

## Anatomia de una Métrica

![metrica](metrica.jpg)

--

## Métricas 2.0 Ejemplo

Antes:

```
collectd.dfs.df.srv-node-dfs10.df-complex.used
```

Despues de Telgraf:

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

## Donde almacenar estas métricas?

  - Menos esquemas 
  - Facil de montar y mantener
  - Alto rendimineto
  - gestión de retención de datos

---

## InfluxDB

Distribucion open source, es una base de datos de serie de tiempo.

Una base de datos de series de tiempo (TSDB) es un sistema de software que está 
optimizado para el manejo de datos de series de tiempo, matrices de números 
indexados por tiempo (una fecha o un rango de fecha y hora)

---
















