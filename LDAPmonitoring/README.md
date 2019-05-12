# ldapserver monitoring

## @edt ASIX M14 2018-2019

Repositorio  donde usamos un server ldap , para posteriormente 
monitorizarlo con grafana.

### Monitoring

Existem dos formas de configuracion para habilitar el monitoreo del
servidor LDAP.

1. **Via cn=config**
2. **Via slapd.conf**

Utilizare la segunda opción ya que hay mas documentacion en el manual de **openldap**

**Configuracion de monitorep via slapd.conf**

- Primero tenemos que estar seguros de que la configuración del esquema  **core.schema**
este incluido en el fichero **slapd.conf**, ya que el backend monitor lo requiere.

```
#cat slapd.conf

#
# See slapd.conf(5) for details on configuration options.
# This file should NOT be world readable.
#

include		/etc/openldap/schema/corba.schema
include		/etc/openldap/schema/core.schema
include		/etc/openldap/schema/cosine.schema
include		/etc/openldap/schema/duaconf.schema

```

- Despues creamos una instancia del backend **monitor** de base de datos 
debajo de la base de datos principal.

```	
# enable monitoring
database monitor

```

- Finalmente damos permisos para que podamos consultar el estado de nuestro
servidor LDAP.

```
access to *
       by * write
       by * read
       by * none
```

#### Executing

Contruimos la imagen Docker:

```
# docker build -t "ldap:19server" .
```

Ejecutamos la imagen docker con el puerto 389 ya mapeado
```
# docker run --rm -p 389:389 --name ldap.server -h ldap.server -d ldap:19server
```
#### Comprovacíón 

Ejecutamos la siguiente orden para ver que funciona:

```
$ ldapsearch -x -h 172.17.0.2 -D 'cn=Manager,dc=edt,dc=org' -w  secret -b 'cn=Monitor' -s base 1.1
# extended LDIF
#
# LDAPv3
# base <cn=Monitor> with scope baseObject
# filter: (objectclass=*)
# requesting: 1.1 
#

# Monitor
dn: cn=Monitor

# search result
search: 2
result: 0 Success

# numResponses: 2
# numEntries: 1

```



