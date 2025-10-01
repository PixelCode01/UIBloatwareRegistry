# Wi-Fi ADB Guide

Use Wi-Fi debugging when a cable is unreliable or you want to keep the device untethered while removing apps. Follow the steps below from top to bottom.

## Prerequisites

- Android 11 or newer with Developer Options unlocked
- Phone and computer on the same Wi-Fi network
- USB cable for the first pairing (only needed once per network)
- Android Platform Tools (adb) available on your computer or the packaged copy shipped with this project

## Enable Developer Options and Wi-Fi debugging

1. Connect the phone with USB and run `adb devices` once to confirm debugging is allowed. Accept the prompt on the device.
2. Open **Settings → Developer options**.
3. Turn on **Wireless debugging**. If the option is greyed out, toggle USB debugging off and on first.
4. Tap **Wireless debugging → Pair device with pairing code**. Leave this screen open.

## Pair the device

1. Run the tool with the new Wi-Fi helpers:
   ```powershell
   python main.py --wifi
   ```
   The program prompts for the IP address and pairing code.
2. Enter the pairing IP and port shown on the phone.
3. Enter the six-digit pairing code. A confirmation message appears if pairing succeeds.

You can also provide everything up front:
```powershell
python main.py --wifi-endpoint 192.168.0.42:5555 --wifi-pair 192.168.0.42:38921 --wifi-code 123456
```

## Reconnect later without a cable

Once paired, enable TCP/IP on the device whenever you plug in a cable:
```powershell
python main.py --enable-tcpip --tcpip-port 5555
```

Then unplug the cable and connect over Wi-Fi:
```powershell
python main.py --wifi-endpoint 192.168.0.42:5555
```

If you forgot the endpoint, run `adb devices -l` to list active wireless sessions.

## Troubleshooting

- **Device not found**: verify both devices share the same network, or disable VPNs and private DNS.
- **Pairing fails immediately**: pairing codes expire after about thirty seconds; request a new one before retrying.
- **Commands are slow**: keep the screen awake and close heavy network traffic apps; 5 GHz Wi-Fi is more stable than 2.4 GHz.
- **Need to reset**: disable Wireless debugging in Developer Options, re-enable it, and pair again.

After a successful Wi-Fi connection you can follow the normal removal workflow. Test mode continues to work with the `--test` flag even when Wi-Fi debugging is active.
