#!/usr/bin/env python

###Goal > Discover clients on a network (scapy documentation: https://scapy.readthedocs.io/en/latest/index.html)
#1. Create arp request directed to broadcast MAC asking for IP
#2. Send packet and receive response
#3. Parse the response
#4. Print result

import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range.")
    options = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return (clients_list)

def print_result(results_list):
    print("IP\t\t\tMAC Address\n------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])
       

options = get_arguments()
scan_result = scan("192.168.1.1/24")
print_result(scan_result)s