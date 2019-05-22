#Documentation

Install telegraf en un ordinador de l'escola per example:
# vim /etc/yum.repos.d/influxdb.repo

[root@localhost ~]# dnf -y install telegraf
[root@localhost ~]# nmap localhost
PORT     STATE SERVICE
111/tcp  open  rpcbind
631/tcp  open  ipp
5432/tcp open  postgresql

### Llavors ens conectem a la maquina de amazon
#ssh -i .ssh/mykey.pem fedora@35.178.250.67

Fen un git clone del nostre repositori on esta el influxdb y grafana:

canviem el /etc/hosts:
[fedora@ip-172-31-26-39 ~]$ cat /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
#192.168.0.2 php
172.41.0.2 grafana.server
172.41.0.3 influxdb.server


Fem la seguent ordre desde la maquina local
#tunel directe hacia influxdb
#ssh -i .ssh/mykey.pem -L 8086:influxdb.server:8086 fedora@35.178.250.67 

Llavors en aquest punt Telegraf esta vomitant tota la informacio de la nostra maquina local
cap a influxdb de amazon.

Fem un altre tunel directe perque amazon de linux no te navegador , llavors ho obrim al nostre sistema
#ssh -i .ssh/mykey.pem -L 3000:grafana.server:3000 fedora@35.178.250.67 

Veiem com els ports estan oberts
[root@localhost ~]# nmap localhost
PORT     STATE SERVICE
111/tcp  open  rpcbind
631/tcp  open  ipp
3000/tcp open  ppp
5432/tcp open  postgresql
8086/tcp open  d-s-n
