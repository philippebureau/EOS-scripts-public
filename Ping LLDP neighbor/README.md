# Ping LLDP Neighbor

These scripts can be used to ping an interface neighbor using LLDP data

They all need an argument to specify the target interface

The scripts use unix socket to interact with EOS and requires the following configuration

```
management api http-commands
    protocol unix-socket
    no shutdown
```

The script should be copied in flash before use

Syntax from EOS : 'bash python /mnt/flash/<scriptname> <interface>'

Example : Execute the script to ping interface ethernet 4 neighbor using the system name 
```
bash python /mnt/flash/ping_lldp_neighbor-sysName.py Ethernet4
```

The script can be used in event-handler.

Example : Execute the script to ping interface ethernet 4 neighbor using the management IP when the interface comes up
```
event-handler wake-movable-eth4
    trigger on-intf Ethernet4 operstatus
    delay 30
    action bash python /mnt/flash/ping_lldp_neighbor-mgmtAddress.py Ethernet4
```
**Note: delay should be adjusted to match the envronment variables such as LLDP intervals or if portfast is configured**