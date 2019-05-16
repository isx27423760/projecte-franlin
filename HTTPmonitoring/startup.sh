#! /bin/bash
# @edt ASIX M14 2018-2019
# crear i engegar server
#--------------------------------------
/opt/docker/install.sh && echo "Ok install"
/usr/sbin/httpd -DFOREGROUND && echo "httpd Ok"
