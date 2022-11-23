# PyhtonControlCenter
Python Control Center is a control center for linux terminal designed for "bspwm" environments where we don't find the classic xorg or gnome cc as in common graphical environments.

```
888       888 888     888       d8888 888
888   o   888 888     888      d88888 888
888  d8b  888 888     888     d88P888 888        (code by WUAL)
888 d888b 888 888     888    d88P 888 888            twitter.com/codewual
888d88888b888 888     888   d88P  888 888     github.com/14wual
88888P Y88888 888     888  d88P   888 888            youtube: WualPK
8888P   Y8888 Y88b. .d88P d8888888888 888     
888P     Y888  "Y88888P" d88P     888 88888888
```

<h2>What I can do?</h2>

<div class="list">
    <ul>
        <a href="#Wifi"><li><b>Wi-Fi</b></li></a>
        <ul>
            <li><b>Turn Wi-Fi On or Off</b>  - This script checks if you have an internet connection by pinging google, if so it unplugs the Wi-Fi adapter, and if not, turns it on</li>
            <li><b>Wi-Fi Setup</b> - Type the SSID of the router you want to connect to, type the password of the access point and YOU'RE CONNECTED!</li>
            <li><b>IPv4 Setting</b> - This script has two options (3 if we count the help module), one of them renews your ip and the other creates the <i>"interfaces"</i> file (file that configures a static IP) to later copy it to <i>/etc/network/interfaces</i> and give you a static IP</li>
        </ul>
    </ul>
    <ul>
        <a href="#Bluetooth"><li><b>Bluetooth</b></li></a>
        <p>The Bluetooth module is still under development, a new version will be published soon. If you decide to use the script regularly, check for updates regularly in order to enjoy all the features</p>
        <ul>
            <li><b>Turn Bluetooth On or Off</b> - ¡<i>This script is still under development</i> ! - Check the status of the Bluetooth service. If it is active, it deactivates and blocks it, otherwise it activates and unlocks it.</li>
            <li><b>Connect Bluetooth Device</b> - Write the name of your device and connect quickly</li>
            <li><b>Disconnect Bluetooth Device</b> - Disconnect all devices connected to the Bluetooth service</li>
        </ul>
    </ul>
    <ul>
        <a href="#Brightness"><li><b>Brightness</b></li></a>
        <ul>
            <li><b>Raise or Lower Brightness</b> - Raises or lowers the screen brightness from 0 to 10 (this option works only on devices with a single connected screen and that allow it)</li>
        </ul>
    </ul>
    <ul>
        <a href="#Audio"><li><b>Audio</b></li></a>
        <ul>
            <li><b>Volume Up or Down</b> - Increases or decreases the volume in a radius from 0 to 10</li>
            <li><b>Mute Sound</b> - ¡<i>This script is still under development</i> ! Mute and unmute the sound of the Master (from your pc)</li>
        </ul>
    </ul>
    <ul>
        <a href="#Lock"><li><b>Lock your Screen</b></li></a>
    </ul>
    <ul>
        <a href="#Status"><li><b>Device Status</b></li></a>
        <ul>
            <li><b>Shutdown</b> - Turn Off the Device</li>
            <li><b>Reboot</b> - Reboot the Device</li>
            <li><b>Log Out</b></li>
        </ul>
    </ul>
    <ul>
        <a href="#other"><li><b>Other Scripts</b></li></a>
        <ul>
            <ul>
                <li><b>More Settings</b> - This script automatically opens (after configuring) your settings application; gnome-control-center, tukedo, ..</li>
                <p>If you don't have a cc, you can install gnome-control-center from here: <a href="https://howtoinstall.co/es/gnome-control-center">Gnome Control Center Installation Steps</a></p>
            </ul>
            <ul>
                <li><b>Battery Percentage</b></li>
                <li><b>Now</b> - Day of the week, Month, day of the month (in number), current time (hour, min, sec) and year</li>
            </ul>            
        </ul>
    </ul>


<h2>How do we work?</h2>
<p>Find the codes used for this script individually, classified by utilities to be able to use only the ones that interest you</p>
<ul>
    <div id="Wifi">
        <details>
        <summary><b>Wi-Fi</b>: Codes & Scripts</summary>
            <h3>
                <b>Wi-Fi</b>
            </h3>
            <ul>
                <a href="scripts/wifi/wifi_turnon_turnoff.py"><li>Turn Wi-Fi On or Off: Code</li></a>
            </ul>
            <ul>
                <a href="scripts/wifi/wifi_set_up.py"><li>Wi-Fi Setup: Code </li></a>
            </ul>
            <ul>
                <a href="scripts/wifi/wifi_set_ip.py"><li>IPv4 Setting: Code</li></a>
            </ul>
        </details>
    </div>
    <div id="Bluetooth">
        <details>
            <summary><b>Bluetooth</b>: Codes && Scripts</summary>
            <h3>
                <b>Bluetooth</b>
            </h3>
            <p>The Bluetooth module is still under development, a new version will be published soon. If you decide to use the script regularly, check for updates regularly in order to enjoy all the features</p>
            <ul>
                <a href="scripts/bluetooth/start_stop-bluetooth.py"><li>Turn Wi-Fi On or Off: Code</li></a>
            </ul>
            <ul>
                <a href="scripts/bluetooth/connect-bluetooth-device.py"><li>Wi-Fi Setup: Code</li></a>
            </ul>
            <ul>
                <a href="scripts/bluetooth/disconnect-bluetooth-device.py"><li>IPv4 Setting: Code</li></a>
            </ul>
        </details>
    </div>
    <div id="Brightness">
        <details>
            <summary><b>Brightness</b>: Codes && Scripts</summary>
            <h3>
                <b>Brightness</b>
            </h3>
            <ul>
                <a href="scripts/brightness/level-brightness.py"><li>Raise or Lower Brightness: Code</li></a>
            </ul>
        </details>
    </div>
    <div id="Audio">
        <details>
            <summary><b>Audio</b>: Codes && Scripts</summary>
            <h3>
                <b>Audio</b>
            </h3>
            <p>The Mute / Unmute Volume module is still under development, a new version will be published soon. If you decide to use the script regularly, check for updates regularly in order to enjoy all the features</p>
            <ul>
                <a href="scripts/audio/level-Volume.py"><li>Raise or Lower Volume: Code</li></a>
                <a href="scripts/audio/mute.py"><li>Mute or Unmute Volume: Code</li></a>
            </ul>
        </details>
    </div>
    <div id="Lock">
        <details>
            <summary><b>Lock</b>: Codes && Scripts</summary>
            <h3>
                <b>Lock</b>
            </h3>
            <ul>
                <a href="scripts/lock/lock.py"><li>Lock your Screen: Code</li></a>
            </ul>
        </details>
    </div>
    <div id="Status">
        <details>
            <summary><b>Device Status</b>: Codes && Scripts</summary>
            <h3>
                <b>Device Status</b>
            </h3>
            <p></p>
            <ul>
                <a href="scripts/status/shutdown.py"><li>Turn Off the Device: Code</li></a>
                <a href="scripts/status/reboot.py"><li>Reboot the Device: Code</li></a>
                <a href="scripts/status/loggout.py"><li>Log Out: Code</li></a>
            </ul>
        </details>
    </div>
    <div id="other">
        <details>
            <summary><b>Other Scripts</b>: Codes && Scripts</summary>
            <h3>
                <b>Other Scripts </b>
            </h3>
            <p></p>
            <ul>
                <a href="scripts/other/more-settings.py"><li>More Settings: Code</li></a>
                <a href="scripts/other/battery.py"><li>Battery Percentage: Code</li></a>
                <a href="scripts/other/now.py"><li>Current Date and Time: Code</li></a>
            </ul>
        </div>
        </details>
</ul>

<h2>Version</h2>
<p><b>Current Version</b>: 1.05</p>
<p><b>Version Updates</b>: README.md Updated</p>

<h2>Frequently Asked Questions (FAQ)</h2>
