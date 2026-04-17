#!/usr/bin/env python3

# Pings an LLDP neighbor by system name to force ARP entry creation for host route injection.
# SYNTAX: ping_lldp_neighbor-sysName.py <interface>
#    Ex: ping_lldp_neighbor-sysName.py Ethernet8

from jsonrpclib import Server
import sys

switch = Server("unix:/var/run/command-api.sock")

def get_neighbor_name(interface):
    cmdResponse = switch.runCmds(1, ["enable", f"show lldp neighbors {interface} detail"])
    neighbor_info = cmdResponse[1]['lldpNeighbors'][interface]['lldpNeighborInfo']
    if not neighbor_info:
        print(f'No LLDP neighbor found on {interface}')
        sys.exit(1)
    return neighbor_info[0]['systemName']

def main():
    if len(sys.argv) < 2:
        print('The script requires one interface as argument')
        print('Ex: ping_lldp_neighbor-sysName.py Ethernet8')
        sys.exit(1)
    interface = sys.argv[1]
    neighbor_name = get_neighbor_name(interface)
    switch.runCmds(1, [f'ping {neighbor_name}'])

if __name__ == '__main__':
    main()
