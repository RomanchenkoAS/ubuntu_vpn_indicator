## Installation

### Developement dependencies for qt version

```bash
sudo apt-get install libxcb-xinerama0
sudo apt-get install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev
```

### Copy Executable to a System Directory

```bash
sudo cp dist/main /usr/local/bin/vpn_indicator
```

### To enable autostart

```bash
cp dist/vpn_indicator.desktop ~/.config/autostart/
chmod +x ~/.config/autostart/vpn_indicator.desktop
```


