#! /bin/bash
# Franlin Colque 
# hisx 2019
#--------------------------------------------------------

systemctl > /var/tmp/injeccio/systemctl.txt

python /var/tmp/injeccio/injeccio.py

rm /var/tmp/injeccio/systemctl.txt

