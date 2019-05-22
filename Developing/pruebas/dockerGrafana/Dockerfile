#Version: 0.0.1
#@edt  2018-2019
#Proyecto : installing grafana
#------------------------------------------
FROM fedora:27
LABEL author="@edt ASIX M14 Curs 2018-2019"
LABEL description="Installing Server Grafana in fedora:27 " 
RUN mkdir /opt/docker
COPY * /opt/docker/
COPY grafana.repo  /etc/yum.repos.d/grafana.repo
RUN dnf -y install iproute iputils uw-imap passwd tree vim procps nmap net-tools httpd grafana
RUN chmod +x /opt/docker/install.sh /opt/docker/startup.sh
WORKDIR /usr/share/grafana
CMD ["/opt/docker/startup.sh"]
