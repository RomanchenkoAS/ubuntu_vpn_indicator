# VPN Indicator

A simple tray app that indicates the Nordlayer VPN connection status by running $ nordlayer status periodically.

### No VPN active
![image](https://github.com/RomanchenkoAS/ubuntu_vpn_indicator/assets/119735427/4e16104e-2da2-4981-9ab5-c6f40c8aa215)
### VPN failed 
![image](https://github.com/RomanchenkoAS/ubuntu_vpn_indicator/assets/119735427/de996ff3-4158-4e73-b6e2-ef637c08f7a9)
### VPN active
![image](https://github.com/RomanchenkoAS/ubuntu_vpn_indicator/assets/119735427/006bd3e8-73c5-4a7c-bade-89b7920c8b1a)

## Installation from executable file

### Copy Executable to a System Directory

```bash
sudo cp dist/main /usr/local/bin/vpn_indicator
```

### To enable autostart

```bash
cp dist/vpn_indicator.desktop ~/.config/autostart/
chmod +x ~/.config/autostart/vpn_indicator.desktop
```

## Building an executable file

### Prerequisites
- Ensure you have python3.10 installed on your system.
- Poetry should be installed. If not, you can install it using the provided link.


### Installation Steps
#### Clone the repository:
```bash
git clone https://github.com/RomanchenkoAS/ubuntu_vpn_indicator.git
cd ubuntu_vpn_indicator
```
#### Install the required packages using Poetry. 
This will also create a virtual environment for you.

```bash
poetry install
```

#### Compile the app:
This will generate a standalone executable for the application.

```bash
poetry run pyinstaller main.spec
```

#### Copy the executable to a system directory:
```bash
sudo cp dist/main /usr/local/bin/vpn_indicator
```
#### Autostart on Login
If you want the application to start automatically when you log in:

```bash
cp dist/vpn_indicator.desktop ~/.config/autostart/
chmod +x ~/.config/autostart/vpn_indicator.desktop
```
#### Usage
After the installation, you can run the application by simply typing:

```bash
vpn_indicator
```

To run in background 
```bash
vpn_indicator > /dev/null 2>&1 & 
```

### Development dependencies for qt version
```bash
sudo apt-get install libxcb-xinerama0
sudo apt-get install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev
```
