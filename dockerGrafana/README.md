# Grafana Server 
## Proyecto 2018/2019 Franlin colque

**dockerGrafana** : Servidor grafana que permite
  la conexión y la configuración vía http (web). El servidor será llamado **grafana.server**

Construimos la imagen de grafana 

```
# docker build -t "grafana:server" .
```

Ejecutamos la imagen docker con el puerto 3000 ya mapeado

```
# docker run --rm -p 3000:3000 --name grafana.server -h grafana.server -d grafana:server
```

Ahora abrimos el navegador web y nos conectamos a Grafana:

```
http//ip-docker:3000
```


