# Ping LLDP Neighbor

These scripts ping an interface's LLDP neighbor to force ARP entry creation for host route injection.

The scripts use the unix socket to interact with EOS and require the following configuration:

```
management api http-commands
    protocol unix-socket
    no shutdown
```

## Usage

After installing the SWIX extension, aliases are configured automatically:

```
ping-lldp-sysname Ethernet4
ping-lldp-mgmt Ethernet4
```

## Event-handler

Example: Ping Ethernet4's neighbor by management IP when the interface comes up:

```
event-handler ping-lldp-eth4
    trigger on-intf Ethernet4 operstatus
    delay 30
    action bash ping_lldp_neighbor-mgmtAddress.py Ethernet4
```

**Note: adjust the delay to match your environment — LLDP convergence interval or portfast configuration.**
