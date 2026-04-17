# EOS-scripts-public

EOS scripts that can be used manually or in conjunction with event-handler.

## Installation

### 1. Download the SWIX to the switch flash

From EOS bash:
```bash
cd /mnt/flash && wget https://github.com/wdion-arista/EOS-scripts-public/releases/download/v1.0.3/pingLldpIP-1.0.3-1.noarch.swix
```

### 2. Install the extension

From EOS enable mode:
```
copy flash:pingLldpIP-1.0.3-1.noarch.swix extension:
extension pingLldpIP-1.0.3-1.noarch.swix
show extensions
```

### 3. Persist across reboots

```
copy installed-extensions boot-extensions
```
