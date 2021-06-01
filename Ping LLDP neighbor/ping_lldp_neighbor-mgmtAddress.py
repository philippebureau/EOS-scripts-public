#!/usr/bin/env python

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
        neighbor_ip = cmdResponse[1]['lldpNeighbors'][interface]['lldpNeighborInfo'][int('0')]['managementAddresses'][int(0)]['address']
        return neighbor_ip
def main():
        if len(args) == 0:
                print 'The script requires one interface as argument'
                print 'Ex: python ping_lldp_neighbor-mgmtAddress.py Ethernet8'
                exit()
        else:
                neighbor_ip = get_neighbor_ip()
                switch.runCmds(1, ['ping %s' % (neighbor_ip)])

if __name__ == '__main__':
   main()