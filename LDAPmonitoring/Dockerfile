# Version: 0.0.1
# @edt M14 2018-2019
# ldapserver grafana.org to monitoring
# -------------------------------------
FROM fedora:27
RUN dnf -y install procps openldap-clients openldap-servers vim nmap
RUN mkdir /opt/docker
COPY * /opt/docker/
RUN chmod +x /opt/docker/install.sh /opt/docker/startup.sh
WORKDIR /opt/docker
CMD ["/opt/docker/startup.sh"]


