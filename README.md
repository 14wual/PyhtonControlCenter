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
            <li><b>Turn Wi-Fi On or Off</b>  - This script checks if you have an internet connection by <br>pinging google, if so it unplugs the Wi-Fi adapter, and if not, turns it on</li>
            <li><b>Wi-Fi Setup</b> - Type the SSID of the router you want to connect to, type the password <br>of the access point and YOU'RE CONNECTED!</li>
            <li><b>IPv4 Setting</b> - This script has two options (3 if we count the help module), one of them <br>renews your ip and the other creates the <i>"interfaces"</i> file (file that configures a static IP) to later copy it to <i>/etc/network/interfaces</i> and give you a static IP</li>
        </ul>
    </ul>
    <ul>
        <a href="#"><li>Bluetooth</li></a>
        <ul>
            <li>Turn Bluetooth On or Off</li>
            <li>Connect Bluetooth Device</li>
            <li>Disconnect Bluetooth Device</li>
        </ul>
    </ul>
    <ul>
        <a href="#"><li>Brightness</li></a>
        <ul>
            <li>Raise or Lower Brightness of your screen</li>
        </ul>
    </ul>
    <ul>
        <a href="#"><li>Audio</li></a>
        <ul>
            <li>Volume Up or Down</li>
        </ul>
    </ul>
    <ul>
        <a href="#"><li>Lock your Screen</li></a>
    </ul>
    <ul>
        <a href="#"><li>Device Status</li></a>
        <ul>
            <li>Turn Off the Device</li>
            <li>Reboot the Device</li>
            <li>Log Out</li>
        </ul>
    </ul>


<h2>How do we work?</h2>

<ul>
    <div id="Wifi">
        <h3>
            <b>Wi-Fi</b>
        </h3>
        <p>Explica</p>
        <ul>
            <a href="scripts/wifi/wifi_turnon_turnoff.py"><li>Turn Wi-Fi On or Off: Code | Script</li></a>
        </ul>
        <ul>
            <a href="scripts/wifi/wifi_set_up.py"><li>Wi-Fi Setup: Code | Script</li></a>
        </ul>
        <ul>
            <a href="scripts/wifi/wifi_set_ip.py"><li>IPv4 Setting: Code | Script</li></a>
        </ul>
    </div>
</ul>
