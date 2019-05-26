# Telegraf

Telegraf es un servicio que recopila y envía métricas, datos de diferentes sistemas. 
Puede recopilar datos del sistema en el que se ejecuta, como uso de disco, RAM, CPU, 
carga del sistema, conexiones y muchos más, e incluye además una creciente 
lista de plugins de entrada, como apache, consul, couchDB, Docker, Elasticsearch, 
Fluentd, HAproxy, http POST, entre otros. Su salida la envía por lo general a una base 
de datos InfluxDB, y es esta capacidad la que mostraremos en este proyecto.

Por lo tanto,**Telegraf** es un agente ligero de recolección de datos, que esta escrito en go,
su principal objectivo es la de enviar telemetria del sistema o de un server 
a **InfluxDB** o a otro sitio, influxDB no tiene por que estar en el mismo host que telegraf
pueden estar en distintos hosts.

### Características

* Escrito en Go. Se compila en un único binario sin dependencias externas.
* Consumo mínimo de memoria.
* Sistema de plugin que permite una fácil inserción de nuevos inputs y outputs.
* Gran número de plugins para la mayoría de los servicios mas populares y APIs.

### Formatos de Output Data 

Además de los formatos de datos específicos de salida,Telegraf admite un conjunto 
de formatos de datos estándar que se pueden seleccionar al configurar muchos complementos de salida.

* InfluXDB (que es la que utilizare para enviar directamente las metricas en tiempo real)
* JSON que (que genera un fichero en formato json con los datos de las metricas recogidas del determinado servicio)

y tambien hay formatos como **Graphite,SplunkMetric,Carbon2,Wavefront**.

### Ejemplo de recolección de datos de telegraf

1. **CPU**
2. **RAM** 
3. **Disk**

#### 1. CPU

Sigla de la expresión inglesa central processing unit, 'unidad central de proceso',
 que es la parte de un ordenador en la que se encuentran los elementos que sirven para procesar datos.

**Descripción**

Este plugin recoge las métricas  del CPU estándar , que genera el 
directorio **/proc**.

**Organización del directorio /proc**

El directorio /proc está organizado en directorios virtuales y subdirectorios, 
que agrupan archivos de tópicos similares. Si como root ejecutamos el comando ls /proc te despliega algo como lo siguiente:

```
# ls /proc
1     2432  3340  3715  3762  5441  815        devices      modules
129   2474  3358  3716  3764  5445  acpi       diskstats    mounts
1290  248   3413  3717  3812  5459  asound     dma          mtrr
133   2486  3435  3718  3813  5479  bus        execdomains  partitions
1420  2489  3439  3728  3814  557   dri        fb           self
165   276   3450  3731  39    5842  driver     filesystems  slabinfo
166   280   36    3733  3973  5854  fs         interrupts   splash
2     2812  3602  3734  4     6     ide        iomem        stat
2267  3     3603  3735  40    6381  irq        ioports      swaps
2268  326   3614  3737  4083  6558  net        kallsyms     sysrq-trigger
2282  327   3696  3739  4868  6561  scsi       kcore        timer_list
2285  3284  3697  3742  4873  6961  sys        keys         timer_stats
2295  329   3700  3744  4878  7206  sysvipc    key-users    uptime
2335  3295  3701  3745  5     7207  tty        kmsg         version
2400  330   3706  3747  5109  7222  buddyinfo  loadavg      vmcore
2401  3318  3709  3749  5112  7225  cmdline    locks        vmstat
2427  3329  3710  3751  541   7244  config.gz  meminfo      zoneinfo
2428  3336  3714  3753  5440  752   cpuinfo    misc
```

Los directorios con números (más sobre esto en un momento) corresponden a cada proceso en ejecución; 
un autoenlace simbólico apunta al proceso actual. Algunos archivos virtuales proveen información sobre el hardware, tal como /proc/cpuinfo

```
# cat /proc/cpuinfo 
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 42
model name	: Intel(R) Core(TM) i5-2500 CPU @ 3.30GHz
stepping	: 7
microcode	: 0x2d
cpu MHz		: 1731.439
cache size	: 6144 KB
physical id	: 0
siblings	: 4
core id		: 0
cpu cores	: 4
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
....more lines.......
```

#### 2. RAM

Sigla de Random Access Memory (‘memoria de acceso aleatorio’), memoria principal 
del ordenador, donde residen programas y datos, sobre la que se pueden efectuar operaciones de lectura y escritura.

**Descripción**

El pluguin **mem** recopila las métricas de la memoria del sistema.
Que utiliza un paquete **mem** que es similar al comando  **FREE** de linux.

Ejemplo:

```
$free -m
              total        used        free      shared  buff/cache   available
Mem:           7957        2719        2727         110        2510        4828
Swap:             0           0           0
```
Tambien recoge datos de **/proc/meminfo** de linux:

```
# cat /proc/meminfo 
MemTotal:        8148528 kB
MemFree:         2494680 kB
MemAvailable:    4678536 kB
Buffers:          334996 kB
Cached:          2081640 kB
SwapCached:            0 kB
Active:          3617120 kB
Inactive:        1318996 kB
Active(anon):    2521124 kB
Inactive(anon):   110144 kB
Active(file):    1095996 kB
Inactive(file):  1208852 kB
Unevictable:          80 kB
Mlocked:              80 kB
SwapTotal:             0 kB
SwapFree:              0 kB
Dirty:               652 kB
Writeback:             0 kB
AnonPages:       2519440 kB
Mapped:           621836 kB
Shmem:            111820 kB
Slab:             297596 kB
SReclaimable:     184944 kB
SUnreclaim:       112652 kB
KernelStack:       22720 kB
PageTables:        99344 kB
NFS_Unstable:          0 kB
.....more lines..............
```

#### 3. Disk

La unidad de disco duro o unidad de disco rígido (en inglés: hard disk drive, HDD) 
es el dispositivo de almacenamiento de datos que emplea un sistema de grabación magnética para almacenar archivos digitales.

**Descripción**

El pluguin **Disk** recopila basicamente métricas sobre el uso del disco de nuestra
maquina. 
Es como el comando **df** de linux, pero esta busca esta información en el directorio **/proc**,
mas especificamente **/proc/self/mounts** i **/proc/diskstats** para ver que dispositivos de 
almacenamiento estan conectados en ese momento en el ordenador y ver las propiedades e información necesaria de cada disco. 

ejemplo:

```
# cat /proc/diskstats 
  11       0 sr0 0 0 0 0 0 0 0 0 0 0 0
   8       0 sda 89341 50348 3159428 1184202 91928 134880 6112089 13468293 0 534707 14652505
   8       1 sda1 82850 14731 3086010 1157948 89383 134876 6112008 13426912 0 502403 14585087
   8       2 sda2 6001 35589 45874 5839 1 0 1 0 0 1618 5839
   8       3 sda3 144 21 5970 4684 6 4 80 184 0 4288 4868
   8       4 sda4 6 0 30 265 0 0 0 0 0 265 265
   8       5 sda5 304 7 19368 14576 0 0 0 0 0 11518 14576
   8      16 sdb 0 0 0 0 0 0 0 0 0 0 0
 253       0 dm-0 43 0 2072 1485 0 0 0 0 0 1130 1485
 253       1 dm-1 109 0 11384 5770 0 0 0 0 0 4445 5770
 253       2 dm-2 73 0 3512 6080 0 0 0 0 0 5504 6080
   8      32 sdc 2157 16285 21271 5691 14 0 17 3727 0 5375 9418
```

### Puesta en marcha de Telegraf

Con el siguiente comando generamos el [fichero de configuración](https://github.com/isx27423760/projecte-franlin/blob/master/telegraf.conf) principal
de telegraf y que le pasara a influxDB. 

```
telegraf -sample-config -input-filter cpu:mem:disk -output-filter influxdb > telegraf.conf
```

Y con el siguiente comando ponemos en marcha el servicio con la configuración que le pasemos. 
```
telegraf --config telegraf.conf	
```

### Cofiguración 

En la mayoría de los sistemas, la ubicación del archivo se encuentran en :
**/etc/telegraf/telegraf.conf**

#### Elementos importantes  del fichero de configuración

- **Agent**: La tabla de agentes configura Telegraf y los valores predeterminados utilizados en todos los complementos, en esta parta 
			 puedes configurar un intervalo de tiempo de recoleción de los datos,tambien los logs, el limite de buffer de las metricas,etc.

- **Plugins**: los plugins en Telegraf estan separados en cuatro partes **Inputs,Outputs,Processors y Aggregators.**
			  Solamente aplicare los inputs y outputs plugins. 

#### Inputs Plugins

Los complementos de entrada son los que reúnen y crean métricas

Y tiene estas caracteristica:

- Interval (la frecuencia con que reune métricas)
- name_override (Sobreescribe el nombre por defecto de la medida)

y otras como name_prefix,name_suffix y tags.

Ejemplo de un Input plugin:

```
[[inputs.openldap]]
  host = "172.17.0.2"
  port = 389

  # ldaps, starttls, or no encryption. default is an empty string, disabling all encryption.
  # note that port will likely need to be changed to 636 for ldaps
  # valid options: "" | "starttls" | "ldaps"
  tls = ""

  # skip peer certificate verification. Default is false.
  insecure_skip_verify = false

  # Path to PEM-encoded Root certificate to use to verify server certificate
  tls_ca = "/etc/ssl/certs.pem"

  # dn/password to bind with. If bind_dn is empty, an anonymous bind is performed.
  bind_dn = ""
  bind_password = ""

  # Reverse metric names so they sort more naturally. Recommended.
  # This defaults to false if unset, but is set to true when generating a new config
  reverse_metric_names = true
```

#### Outputs Plugins

Son los que escriben y/o envian las métricas en algun lugar en mi caso a Influxdb.

Ejemplo:
```
[[outputs.influxdb]]
  urls = [ "http://influxdb:8086" ]
  database = "telegraf"
```



