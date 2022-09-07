#!/bin/python
import socket
import time

# lb_fqdn = Load Balancer fully qualified domain name
# file_path = Path for /etc/hosts
# dns_entries = Entries to check in the /etc/hosts file

lb_fqdn = ''
file_path = "/etc/hosts"
dns_entries = [""]

# Get a list with the two ips of a Load Balancer

ips = []

while len(ips) < 2:
    ip = socket.gethostbyname(lb_fqdn)
    if ip not in ips:
        ips.append(ip)
    time.sleep(1)

# Look for any of the ips in the hosts file

file_ok = False

for ip in ips:
    with open(file_path,'r') as file:
        content = file.read()
        if ip in content:
            file_ok = True

if file_ok:
    print("Se ha encontrado una IP del balanceador en el fichero.")
else:
    for dns_entry in dns_entries:
        with open(file_path, "r") as f:
            lines = f.readlines()
        with open(file_path, "w") as f:
            for line in lines:
                if dns_entry in line:
                    f.write(ips[0] + "  " + dns_entry + "\n")
                else:
                    f.write(line)