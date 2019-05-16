#! /bin/bash
cp /opt/docker/httpd.conf /etc/httpd/conf/httpd.conf
mkdir /var/www/certs
mkdir /var/www/html/www.virtual.com
mkdir /var/www/html/www.myserver.org
# web index
cp /opt/docker/index.html /var/www/html/index.html
cp /opt/docker/index.myserver.html /var/www/html/www.myserver.org/index.html
cp /opt/docker/index.virtual.html /var/www/html/www.virtual.com/index.html

sed  's/www.myserver.org/www.myserver.org www.virtual.com/' /etc/hosts > /tmp/hosts$$
cp /tmp/hosts$$ /etc/hosts
