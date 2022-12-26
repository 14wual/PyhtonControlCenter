# PyhtonControlCenter - PCC V 2.0.0
Python Control Center is a control center for linux & windows with GUI designed for "bspwm" environments where we don't find the classic xorg or gnome cc as in common graphical environments.

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

<p>This script has been <b>tested on the following operating systems</b>: <b>Ubuntu</b> Xorg, Ubuntu Bspwm, Kali Gnome, <b>Kali</b>, Kali Bspwm, and <b>Parrot OS</b> Bspwm</p>


<h2>Installation</h2>

<p>Remember that it is very important that you install everything correctly for the proper functioning of the script</p>

<p>Instructions</p>

```
git clone https://github.com/14wual/PyhtonControlCenter
cd PyhtonControlCenter
chmod +x setup.sh
./setup.sh
```

## Usage

Soon...

<h2>Version</h2>
<p><b>Current Version</b>: 1.25</p>
<ul>
    <p><b>Version Updates</b>:</p>
    <ul>
        <details>
            <summary>Commits Updates - 1.X:</summary>
            <ul>
                <details>
                    <summary>Version 1.01</summary>
                    <ul>
                        <li>03-nov-22 / 20-nov-22 </li>
                        <ul>
                            <li>Scheduled Script Modules</li>
                            <ul>
                                <li>Wifi module with their respective options</li>
                                <li>Bluetooth module with their respective options</li>
                                <li>Status module with their respective options</li>
                                <li>Lock module</li>
                                <li>Sound module with their respective options</li>
                                <li>Brightness module</li>
                            </ul>
                        </ul>
                    </ul>
                </details>
            </ul>
            <ul>
                <details>
                    <summary>Version 1.05</summary>
                    <ul>
                        <li>23-nov-22 </li>
                        <ul>
                            <li>Creation of the repository: <a href="https://github.com/14wual/PyhtonControlCenter"></a><b>PCC</b></li>
                            <li><b>Main Script Post</b></li>
                            <li>Version V1 of the README.md file (<i>RDME-V01</i>)</li>
                        </ul>
                    </ul>
                </details>
            </ul>
            <ul>
                <details>
                    <summary>Version 1.08</summary>
                    <ul>
                        <li>23-nov-22</li>
                        <ul>
                            <li>Posted the code and scripts py of the <b>scripts individually</b>. Find them <a href="scripts">here</a></li>
                            <li>Updated installation and requirements file</li>
                            <li>Updated README.md file (<i>RDME-V05</i>)</li>
                        </ul>
                    </ul>
                </details>
            </ul>
            <ul>
                <details>
                    <summary>Version 1.10</summary>
                    <ul>
                        <li>24-nov-22 </li>
                        <ul>
                            <li><b>Terminal command created</b></li>
                            <li>PCC file (<i>sh</i>) upload (command)</li>
                            <li>Updated README.md file (<i>RDME-V09</i>)</li>
                            <li><b>Posted PCC Options</b> Dirs && Scripts</li>
                        </ul>
                    </ul>
                </details>
            </ul>
            <ul>
                <details>
                    <summary>Version 1.30</summary>
                    <ul>
                        <li>27-nov-22</li>
                        <ul>
                            <li><b>Setup file</b> (setup.py) <b>bugs fixed</b></li>
                            <li>Check file for "options" <b> folder posted</b></li>
                            <li>Updated README.md file</li>
                        </ul>
                    </ul>
                </details>
            </ul>
        </details>
        <details>
            <summary>Commits Updates - 2.X:</summary>
            After a small stagnation in the work of the script, PCC returns in its most complex version and with this, its latest version, or at least on December 1, 2023.

PCC returns in all its splendor, and it is that a way has been found to have a simple and functional graphical interface, with complete backward compatibility between Windows and Linux systems, and of course, compatible with the environment for which it was created, "BSPWM".

What does this new version add?

PCC has been programmed from scratch, this time making use of pages in python scripts for more efficient code reading and scripting.

Improvements:

[Wifi]
  - In the label where the Wi-Fi functionalities are chosen, a message will be displayed depending on whether the Wi-Fi is connected or not, and to which SSID it is connected.
  - Fixed bugs that wouldn't let you connect to a specific SSID. Now, when choosing this functionality, a pop-up window will appear with all the Wi-Fi in button mode, with a text entry to write the password and finally, a button that will execute a function to connect to that access point.
  - The function will open (as is done as a general rule in all control centers) the Wi-Fi configuration window, regardless of whether it is a Windows or Linux Operating System.
  - The "Turn ON/OFF Wifi" function has not undergone many changes if we refer to the user or the developer

[Drums]
  - This has been my favorite module in the update, and it is that this is simply made up of two labels, the image and the text. The image is made up of three images depending on the state it is in (normal, low battery, charging). The texts are formed as follows: "MESSAGE + Battery Percentage". The message, like the image, varies between states, which are: normal, low battery, high battery, charging.

[Bright]
  - This functionality has been improved. Like the rest of the project, it is compatible with linux and windows and as an improvement, the brightness control is independent of the screen you are using, now it can be used with several screens at the same time. But speaking about the user, now it is a "Slide Bar", which works like the common cc.

[Device-Mode]
  - Here we talk about 4 modes (lock screen, power off, restart and log out). These have not changed in algorithm, the new thing apart from the GUI, is that now when "clicking" on any of the options, a confirmation pop-up window appears.

[Other-GUI]
  - The program is not scalable.
  - This also has a function that makes it always stay at the top, since this program is designed to execute the action and close it.

[Bluetooth]
  - In the label where the Bluetooth functionalities are chosen, a message will be displayed depending on whether the Wi-Fi is enabled or not.

[SETUP]
  - Once again, the requirements must be installed, since this script brings many new libraries. There is a new way to install them (read README.md)

To ADD (For version 3.0)

[Bluetooth]
  - Bugs that did not allow connecting to a specific Device have been fixed. Now, when choosing this functionality, a pop-up window will appear with all the devices in button mode that, when clicked, will execute a function to connect to that device.
  - The function will open (as is done as a general rule in all control centers) the Bluetooth configuration window, regardless of whether it is a Windows or Linux Operating System.
  - The "Turn ON/OFF Bluetooth" function has not undergone many changes if we refer to the user or the developer

[AUDIO]
  - Currently, the "Slide Bar" is added, but like the bluethooth function, it is disabled, waiting for the third update.
    </ul>
    
</ul>


Copyright © 2023 Carlos Padilla.

This project is GPL licensed.
