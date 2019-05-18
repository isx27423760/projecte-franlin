# HTTP
## @ edt ASIX M14 Curs 2018-2019

Servidor http, para su posterior monitorea con Grafana.
Telegraf  recopila información de rendimiento del servidor mediante el módulo 
[mod_status](https://httpd.apache.org/docs/2.4/mod/mod_status.html) del servidor HTTP de Apache.

El **mod_status** permite al administrador del servidor averiguar qué tan 
bien está funcionando el servidor. Se presenta una página HTML que proporciona las 
estadísticas actuales del servidor.

Algunos de los detalles que nos proporciona son :

- El número de peticiones.
- El número de peticiones inactivos.
- Número total de accesos y número de bytes servidos.
- La hora en que se inició / reinició el servidor y la hora en que se ha estado ejecutando.
- Los promedios indican la cantidad de solicitudes por segundo, la cantidad de bytes servidos por segundo y la cantidad promedio de bytes por solicitud.
- Los hosts actuales y las solicitudes que se están procesando.

#### Configuración del fichero httpd.conf

Descomentamos las lineas siguientes del servidor.

```
ExtendedStatus On
<Location "/server-status">
    SetHandler server-status
    Order allow,deny
    Allow from all
</Location>
```

**ExtendedStatus On** : Es para que muestra información adicional de nuestro servidor httpd.

**Allow from all** :  Permisos para que desde fuera del servidor podamos consultar el estado de nuestro web.


Creamos una web virtual , para hacer las consultas a esta pagina.

```
<VirtualHost www.virtual.com:80>
	ServerAdmin webmaster@www.virtual.com
	DocumentRoot /var/www/html/www.virtual.com 
	ServerName www.virtual.com
	#~ ErrorLog logs/www.one-error_log
	#~ CustomLog logs/www.one-access_log common
</VirtualHost>
```

#### Creación y ejecución del servidor Apache.

Construimos la imagen Docker:

```
# docker build -t "http:19server" .
```

Ejecutamos la imagen docker con el puerto 389 ya mapeado
```
# docker run --rm -p 80:80 --name www.myserver.org -h www.myserver.org -d http:19server
```
#### Comprovacíón 

Ejecutamos la siguiente orden para ver que funciona:

```
http://ip-docker/server-status
```






