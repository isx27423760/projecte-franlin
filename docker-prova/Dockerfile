FROM fedora:27
LABEL author="@edt ASIX Project Franlin"
LABEL description="Projecte Grafana-influxdb-telegraf Curs 2018-2019"
RUN dnf -y wget install iproute iputils nmap uw-imap procps net-tools passwd httpd vsftpd openssh-server tftp-server vim
RUN mkdir /opt/docker
#RUN mkdir /opt/docker/xinetd.d
#COPY xinetd.d/* /opt/docker/xinetd.d/
ADD * /opt/docker/
#RUN chmod +x /opt/docker/startup.sh /opt/docker/install.sh
WORKDIR /opt/docker
#CMD [ "/opt/docker/startup.sh" ]

