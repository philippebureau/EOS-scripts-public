# EOS-scripts-public

EOS scripts that can be used manually or in conjunction with event-handler.

## Installation

From EOS enable mode:
```
copy https://github.com/wdion-arista/EOS-scripts-public/releases/download/v1.0.3/pingLldpIP-1.0.3-1.noarch.swix extension:
extension pingLldpIP-1.0.3-1.noarch.swix
show extensions
```

### Persist across reboots

```
copy installed-extensions boot-extensions
```
