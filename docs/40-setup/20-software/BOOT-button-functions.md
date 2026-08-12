The dedicated button wired to `GPIO0` (typically labelled **BOOT** or **FLA** on boards that have it) has a special purpose: holding it down while powering up the board will enter it into bootloader mode, allowing you to [install the firmware](Software-installation.md) into the flash memory of the MCU.

On the other hand, at runtime, after Battery Emulator has booted up, this button can be also used for maintenance tasks requiring physical presence at the location. There are three maintenance actions that are triggered by pressing and holding that button for different lengths of time. This gives you a way to recover access to the device, or reset it, using only the physical button — without needing the web interface, a serial connection, or a re-flash.

# Button long-press actions

All three actions are chosen by **how long you hold the button before releasing it**. Nothing happens while the button is still down; the device only decides what to do at the moment you let go. This means you can safely hold the button and watch the LED feedback until you reach the length you want, and you can always abort simply by releasing early or before five seconds have passed.

On boards fitted with a status LED, the device flashes the LED white while you hold the button so you can see which action you are about to trigger, with the flashing getting faster as you pass each threshold. As soon as you release, the LED returns to its normal status display. On boards without a status LED — or where that connection has been configured to drive a display instead of an LED — the actions still work in exactly the same way; you simply won't see the flashing and will need to time the hold yourself.

## Start Wi-Fi access point

Holding the button for **at least 5 seconds but less than 15 seconds** starts the Wi-Fi access point. On boards with a multi-colour status LED, once you cross the five-second mark the LED begins flashing **white slowly** (400ms), confirming you have reached this first action. Use this when the device is not reachable on your normal network, and you have disabled the access point earlier in the settings — for example if it can't connect to your router, or you don't know its address — and you want to bring up its own Wi-Fi network so you can connect to it directly and open the web interface. If the access point is already running, this does nothing.

## Wipe Wi-Fi client settings

Holding the button for **at least 15 seconds but less than 30 seconds** clears the Wi-Fi network settings and restarts the device. When you pass the 15 second mark, the white flashing speeds up to a noticeably faster rate (200ms), letting you know you have moved into this action. If you let go here, this erases only the information needed to join your local network — the network name (SSID), its password, the Wi-Fi channel, any fixed (static) IP configuration and the Wi-Fi PHY calibration data. Everything else is kept, including your battery and inverter configuration, MQTT settings, the device hostname, and the access point settings. This is the right choice when the only problem is that the wrong network details were entered and you simply want to start over on the network side. So that the device is reachable again afterwards, this action also makes sure the access point is switched on when it restarts, even if you had previously turned it off in the settings. 

Note: The access point credentials remain the ones you had previously configured, they are not wiped. After you finish reconfiguring the device, you'll have to manually disable the access point again.

## Factory reset

Holding the button for **30 seconds or more** performs a full factory reset and restarts the device. The white flashing speeds up again to a very rapid blink (100ms), signalling that you have reached the most powerful action; if you keep holding at this pace and then release, the full reset is carried out. This clears **all** stored settings plus the Wi-Fi PHY calibration data and returns the Battery-Emulator to its out-of-the-box defaults, just as if you had used the factory reset option in the web interface or flashed as new. This is intended to be used as a last resort, when the device is so misconfigured that nothing else works. Because it erases everything, you will need to set the device up again from scratch afterwards.

# After the device restarts

The 15-second and 30-second actions both restart the device. Before restarting, Battery Emulator safely pauses operation and opens the contactors, so the reset happens in a controlled way rather than opening the contactors mid-operation.

After a Wi-Fi settings wipe or a factory reset, the device performs full RF calibration (~100 ms extra RF init) and rewrites fresh calibration only once, and then comes back up without a configured client network and will not try to join your local network until you set it up again. In both cases it is reachable through its own access point, so you can connect to that and use the web interface to reconfigure it.

# Notes and safety

Because each action is only carried out when you release the button — and never while it is simply held down — a button that becomes stuck or is held indefinitely will not trigger a reset on its own. The two most powerful actions, clearing the network settings and the full factory reset, are also placed at deliberately long hold times (15 and 30 seconds) so they cannot be triggered by a brief accidental press.

If your board does not have a button configured for this purpose, these long-press actions are simply unavailable.
