#!/usr/bin/env python

#This script can be used to force communication for quiet devices
#It was created to force an ARP entry creation for host route injection
#It requires to pass an interface name as an argument.
#SYNTAX: python ping_lldp_neighbor.py <interface>
#       Ex: python ping_lldp_neighbor.py Ethernet8

import json
from jsonrpclib import Server
import sys

args = sys.argv[1:]
switch = Server( "unix:/var/run/command-api.sock" )

def get_neighbor_name():
        interface = sys.argv[1]
        cmdList = [ "enable" , "show lldp neighbors %s detail" % (interface) ]
        cmdResponse = switch.runCmds(1, cmdList)
        neighbor_name = cmdResponse[1]['lldpNeighbors'][interface]['lldpNeighborInfo'][int('0')]['systemName']
        return neighbor_name
def main():
        if len(args) == 0:
                print 'The script requires one interface as argument'
                print 'Ex: python ping_lldp_neighbor.py Ethernet8'
                exit()
        else:
                neighbor_name = get_neighbor_name()
                switch.runCmds(1, ['ping %s.live.rt.cbcrc.ca' % (neighbor_name)])

if __name__ == '__main__':
   main()