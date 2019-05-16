#Version: 0.0.1
#@edt  2018-2019
#Proyecto : installing http server
#------------------------------------------
FROM fedora:27
LABEL author="@edt ASIX M14 Curs 2018-2019"
LABEL description="Installing Server httpd in fedora:27 " 
RUN mkdir /opt/docker
COPY * /opt/docker/
#COPY influxdb.repo  /etc/yum.repos.d/influxdb.repo
RUN dnf -y install iproute iputils passwd tree vim procps nmap net-tools httpd telnet
RUN chmod +x /opt/docker/install.sh /opt/docker/startup.sh
WORKDIR /opt/docker
CMD ["/opt/docker/startup.sh"]
