#!/usr/bin/python3

import scapy.all as scapy
import argparse

def get_ip(): #get the ip address or whole ip range from the user

	parser=argparse.ArgumentParser()	
	parser.add_argument("-r","--range",dest="ipadrr",help="Specify an IP Address or a range of IP Address")
	options = parser.parse_args()

	if not options.ipadrr:
		parser.error("[-] Specify an IP Address or a range of IP Address --help for more details")

	return options

def scan(ip): #use the ipaddress argument to use as a input in the scan function
	
	arp_header = scapy.ARP(pdst = ip)
	ether_header = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_packet = ether_header/arp_header
	answered_list = scapy.srp(arp_request_packet,timeout=1)[0]
	
	targets_list = []
	
	for elements in answered_list:
		client_dict = {"ip":elements[1].psrc,"mac":elements[1].hwsrc}
		targets_list.append(client_dict)
	
	return targets_list


def report(targets_list):

	print ("IpAdrr\t\t\tMacAddr")
	print ("------------------------------------------")
	for target in targets_list:
		print (target['ip'],"\t\t",target['mac'])

ip = get_ip()


scan_result = scan(ip.ipadrr)


report(scan_result)



