#!/usr/bin/env python3

#This script can be used to force communication for quiet devices
#It was created to force an ARP entry creation for host route injection
#It requires to pass an interface name as an argument.
#SYNTAX: python ping_lldp_neighbor-mgmtAddress.py <interface>
#       Ex: python ping_lldp_neighbor-mgmtAddress.py Ethernet8

import json
from jsonrpclib import Server
import sys

args = sys.argv[1:]
switch = Server( "unix:/var/run/command-api.sock" )

def get_neighbor_ip():
        interface = sys.argv[1]
        cmdList = [ "enable" , "show lldp neighbors %s detail" % (interface) ]
        cmdResponse = switch.runCmds(1, cmdList)
        neighbor_info = cmdResponse[1]['lldpNeighbors'][interface]['lldpNeighborInfo']
        if not neighbor_info:
                print('No LLDP neighbor found on %s' % interface)
                exit(1)
        mgmt_addrs = neighbor_info[0]['managementAddresses']
        if not mgmt_addrs:
                print('LLDP neighbor on %s does not advertise a management address' % interface)
                exit(1)
        return mgmt_addrs[0]['address']

def main():
        if len(args) == 0:
                print('The script requires one interface as argument')
                print('Ex: python ping_lldp_neighbor-mgmtAddress.py Ethernet8')
                exit()
        else:
                neighbor_ip = get_neighbor_ip()
                switch.runCmds(1, ['ping %s' % (neighbor_ip)])

if __name__ == '__main__':
        main()