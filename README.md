# EOS-scripts-public

EOS scripts that can be used manually or in conjunction with event-handler.

## Installation

### 1. Download the SWIX to the switch flash

From EOS bash:
```
copy https://github.com/wdion-arista/EOS-scripts-public/releases/download/v1.0.2/pingLldpIP-1.0.2-3.noarch.swix flash:
```

### 2. Install the extension

From EOS enable mode:
```
copy flash:pingLldpIP-1.0.2-3.noarch.swix extension:
extension pingLldpIP-1.0.2-3.noarch.swix
show extensions
```

### 3. Persist across reboots

```
copy installed-extensions boot-extensions
```
