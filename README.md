# EOS-scripts-public

EOS scripts that can be used manually or in conjunction with event-handler.

## Installation

### 1. Download the SWIX to the switch flash

From EOS bash:
```bash
cd /mnt/flash && wget $(wget -qO- https://api.github.com/repos/wdion-arista/EOS-scripts-public/releases/latest | python3 -c "import sys,json; assets=json.load(sys.stdin)['assets']; print(next(a['browser_download_url'] for a in assets if a['name'].startswith('pingLldpIP') and a['name'].endswith('.swix')))")
```

This resolves the latest release and downloads the versioned SWIX file automatically.

### 2. Install the extension

From EOS enable mode:
```
copy flash:pingLldpIP-1.0.2-2.noarch.swix extension:
extension pingLldpIP-1.0.2-2.noarch.swix
show extensions
```

### 3. Persist across reboots

```
copy installed-extensions boot-extensions
```
