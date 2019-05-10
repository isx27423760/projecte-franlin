# How install grafana in FEDORA 27

[root@i16 projecte]# dnf -y install https://dl.grafana.com/oss/release/grafana-5.4.2-1.x86_64.rpm

[root@i16 projecte]# systemctl daemon-reload

[root@i16 projecte]# systemctl start grafana-server




### Configuracion para crear usuario de postgres con permiso read only enpostgres

* Primero configuramos la base de datos para crear el user
[root@i18 ~]# vim /var/lib/pgsql/data/pg_hba.conf 

# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     trust
# IPv4 local connections:
host    all             all             127.0.0.1/32            trust
# IPv6 local connections:
host    all             all             ::1/128                 trust

Creamos un rol
postgres=# CREATE ROLE rol_readonly;

postgres@trac:~$ createuser -h localhost -p 5432 -U postgres -D -E -g rol_readonly -P -R -S usr_grafana






