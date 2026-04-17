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

## Optional ping parameters

Configure via EOS daemon block — all options are optional and fall back to defaults:

```
daemon pingLldpIP
   option ping-count value 5
   option ping-timeout value 2
   option ping-source value Management0
   option ping-vrf value MGMT
   no shutdown
```

| Option | Default | Description |
|---|---|---|
| `ping-count` | 2 | Number of ping packets |
| `ping-timeout` | 2 | Ping timeout in seconds |
| `ping-source` | *(none)* | Source interface or IP |
| `ping-vrf` | *(default VRF)* | VRF to ping from |

## Event-handler

Example: Ping Ethernet4's neighbor by management IP when the interface comes up:

```
event-handler ping-lldp-eth4
    trigger on-intf Ethernet4 operstatus
    delay 30
    action bash ping_lldp_neighbor-mgmtAddress.py Ethernet4
```

**Note: adjust the delay to match your environment — LLDP convergence interval or portfast configuration.**
