---
title: "Software installation"
---

# Installing for the first time

Follow these instructions if you have a compatible device that doesn't yet have Battery emulator installed.

## Web installer

The easiest way to install Battery Emulator is via the Web Installer, using a compatible browser (Chrome/Edge).

1. Visit https://dalathegreat.github.io/BE-Web-Installer/

2. Follow the instructions to plug in your device over USB, erase it, and flash a suitable factory image.

## Manual installation (via terminal)

If you are unable to use the Web Installer, you can download and flash a factory image yourself.

1. Find and download the appropriate factory image for your device from https://github.com/dalathegreat/BE-Web-Installer/tree/main/images

2. Open up a terminal and `cd` to the folder you downloaded the factory image to.

3. Plug in your device over USB and run `esptool` to flash the factory image. This will involve installing `esptool` first.

  - If you have Python3 and `pip` available:
    ```sh
    pip install esptool
    esptool write-flash -e 0 BE_v9.1.4_LilygoT-CAN485.factory.bin
    ```
  - Or by installing `uv` (see https://docs.astral.sh/uv/getting-started/installation/) and using that:
    ```sh
    uv tool run --from=esptool esptool write-flash -e 0 BE_v9.1.4_LilygoT-CAN485.factory.bin
    ```
    (change the filename above to match the file you downloaded).
4. Reset or unplug/replug the device so that it starts up.

5. Connect to the `BatteryEmulator` WiFi SSID, password 123456789

6. Go to http://192.168.4.1 and configure the device (connecting it to your own WiFi, and/or changing the AP WiFi password).

# Upgrading

Here we assume you already have Battery emulator running on your device with access to the web interface. 

1. Download the appropriate **update** image for your hardware from [release assets](https://github.com/dalathegreat/Battery-Emulator/releases)

2. Navigate to Battery emulator's OTA update page.

3. Select the update image file you downloaded.

4. OTA update page should update the firmware and reboot the device.

Any settings you have saved will be preserved.
