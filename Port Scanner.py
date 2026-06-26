#!/usr/bin/env python3
import socket
import ipaddress
import re
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535
open_ports = []
while True:
    ip_input = input("Enter an IP address to scan: ")
    try:
        ipaddress.ip_address(ip_input)
        print("Valid IP address.")
        break
    except ValueError:
        print("Invalid IP address. Please try again.")
while True:
    print("Enter a port range to scan (e.g., 0-65535) :")
    port_range_input = input("Enter port range: ")
    port_range_valid = port_range_pattern.search(port_range_input.replace(" ", ""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        if port_min < 0 or port_max > 65535 or port_min > port_max:
            print("Invalid port range. Please try again.")
        else:
            print(f"Valid port range: {port_min}-{port_max}")
            break
for port in range(port_min, port_max + 1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((ip_input, port))
            open_ports.append(port)
    except:
        pass
for port in open_ports:
    print(f"Port {port} is open on {ip_input}.")
