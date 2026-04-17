#!/usr/bin/env python3

# Pings an LLDP neighbor by management IP to force ARP entry creation for host route injection.
# SYNTAX: ping_lldp_neighbor-mgmtAddress.py <interface>
#    Ex: ping_lldp_neighbor-mgmtAddress.py Ethernet8
#
# Optional EOS daemon config:
#   daemon pingLldpIP
#      option ping-count value 5
#      option ping-timeout value 2
#      option ping-source value Management0
#      option ping-vrf value MGMT
#      no shutdown

from jsonrpclib import Server
import sys

switch = Server("unix:/var/run/command-api.sock")

def get_options():
    try:
        response = switch.runCmds(1, ["enable", "show daemon pingLldpIP"])
        options = response[1]['daemons']['pingLldpIP']['data']['options']
        count   = options.get('ping-count',   {}).get('value', '2')
        timeout = options.get('ping-timeout', {}).get('value', '2')
        source  = options.get('ping-source',  {}).get('value', '')
        vrf     = options.get('ping-vrf',     {}).get('value', '')
        return count, timeout, source, vrf
    except Exception:
        return '2', '2', '', ''

def get_neighbor_ip(interface):
    cmdResponse = switch.runCmds(1, ["enable", f"show lldp neighbors {interface} detail"])
    neighbor_info = cmdResponse[1]['lldpNeighbors'][interface]['lldpNeighborInfo']
    if not neighbor_info:
        print(f'No LLDP neighbor found on {interface}')
        sys.exit(1)
    mgmt_addrs = neighbor_info[0]['managementAddresses']
    if not mgmt_addrs:
        print(f'LLDP neighbor on {interface} does not advertise a management address')
        sys.exit(1)
    return mgmt_addrs[0]['address']

def build_ping_cmd(target, count, timeout, source, vrf):
    cmd = f'ping vrf {vrf} {target}' if vrf else f'ping {target}'
    cmd += f' repeat {count} timeout {timeout}'
    if source:
        cmd += f' source {source}'
    return cmd

def main():
    if len(sys.argv) < 2:
        print('The script requires one interface as argument')
        print('Ex: ping_lldp_neighbor-mgmtAddress.py Ethernet8')
        sys.exit(1)
    interface = sys.argv[1]
    neighbor_ip = get_neighbor_ip(interface)
    count, timeout, source, vrf = get_options()
    switch.runCmds(1, [build_ping_cmd(neighbor_ip, count, timeout, source, vrf)])

if __name__ == '__main__':
    main()
