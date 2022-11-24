#------------------------------IMPORT------------------------------
import os
import subprocess
from tqdm.auto import tqdm
import sys
from sys import stdout
import requests
import time
#import wireless
from bullet import Password
import network
import psutil 

#------------------------------PRINT_COLORS------------------------------
def red():
    RED = "\033[1;31m"
    stdout.write(RED)
def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)
def white():
    WHITE = "\033[1;37m"
    stdout.write(WHITE)
def green():
    GREEN = "\033[1;32m"
    stdout.write(GREEN)

#------------------------------WIFI_ADAPTERS------------------------------
def current_ip():

    global cur_ip
    process = subprocess.check_output("hostname -I", shell=True)
    encoding = sys.getdefaultencoding()
    cur_ip = process.decode(encoding)

#------------------------------WIFI_SETTINGS------------------------------
def wifi_turnon_turnoff():

    os.system("clear")
    timeout = 1

    try:
        print("Checking Connection")
        requests.head("https://google.es",timeout=timeout)

        wifi = True

        if wifi == True:

            green();print("Connection Enabled")
            blue();print("Disabling Connection")

            for i in tqdm(range(5)):
                print("",end='\r')
                time.sleep(0.09)

            os.system("nmcli radio wifi off")
            os.system(("nmcli radio wifi"))
            green();print("Connection Disabled")

        else:red();print("An unexpected error has occurred [error code: 121]")

    except:

        wifi = False
        green();print("Connection Disabled")

        if wifi == False:

            blue();print("Enabling connection")

            for i in tqdm(range(5)):
                print("",end='\r')
                time.sleep(0.09)

            os.system("nmcli radio wifi on")
            os.system(("nmcli radio wifi"))
            green();print("Connection Enabled")

        else: red();print("An unexpected error has occurred [error code: 122]")

    time.sleep(2)
    os.system("clear")
    apiconfig()

def wifi_set_ip():

    os.system("clear")
    blue();print("Choice")

    white();print("\
        \n[1] | Renew IP \
        \n[2] | [Static/DHCP] | Set up Wi-Fi\
        \n\n[3] | Help")

    blue();choice = int(input("Select an option: "))

    while choice < 0 or choice > 3: 

        os.system("clear")
        red();print(f"[{choice}] It's a wrong choice\nPlease select a correct option")

        white();print("\
            \n[1] | Renew IP \
            \n[2] | [Static/DHCP] | Set up Wi-Fi\
            \n\n[3] | Help")

        blue();choice = int(input("Select an option: "))

    if choice == 1:

        white();print("Dropping current IP")
        os.system("sudo dhclient -r")

        green();print("Success: current IP removed\nCorrect: current IP dropped")
        white();print("Renewing IP")

        os.system("sudo dhclient -v")
        green();print("Correct: current IP renewed")

        for i in tqdm(range(6)):
                print("",end='\r')
                time.sleep(0.03)

        current_ip()
        global cur_ip

        green();print(f"Excellent!, your new IP is {cur_ip}")

    elif choice == 2:

        os.system("iwconfig;ip link sho | grep w")
        red();print("Correctly write your Network Interface")

        network_interface = input("Network Interface: ")
        os.system(f"sudo iwconfig {network_interface}")

        time.sleep(0.05)

        adress = input("Adress: ")
        netmask = input("Netmask: ")
        gateway = input("Gateway: ") 
        network = input("Network: ") 
        broadcast = input("Broadcast: ") 

        choice_dns = input("[y/n] | Want to add nameservers: ")

        if choice_dns == "y" or choice_dns == "Y":
            
            nameserver1 = input("Nameserver 1: ")
            nameserver2 = input("Nameserver 2: ")

        else:

            print("")

        interfaces = "config/interfaces"

        file = open(interfaces, "w")

        file.write(f"auto {network_interface} " + os.linesep)
        file.write("address " + adress + os.linesep)
        file.write("netnetmask " + netmask + os.linesep)
        file.write("network " + network + os.linesep)
        file.write("broadcast  " + broadcast + os.linesep)
        file.write("gateway " + gateway + os.linesep)

        if choice_dns == "y " or choice_dns == "Y":

            file.write("dns-nameservers " + nameserver1 + os.linesep)
            file.write("dns-nameservers " + nameserver2 + os.linesep)
            
        green();print("File Viewer")

        blue();print("address " + adress + "\n" 
        "netnetmask " + netmask + "\n"
        "network " + network + "\n"
        "broadcast  " + broadcast + "\n"
        "gateway " + gateway + "\n")

        file.close()

        os.system(f"sudo cp {interfaces} /etc/network/interfaces")
        os.system("sudo /etc/init.d/networking restart")
        os.system("sudo ifconfig eth0 down")

        for i in tqdm(range(26)):
                print("",end='\r')
                time.sleep(0.02)

        os.system("sudo ifconfig eth0 up")
        
        num = 3
        for i in range(3):
            red();print("Waiting...")
            print(num)
            print("",end="\r")
            num =-1
            time.sleep(1)

        os.system(f"ping -c 1 {gateway}")
        os.system(f"ping -c 1 https://google.es/")

    elif choice == 3:

        white();print("[Renew IP]")

        blue();print("When you release your IP address, your router address is released and your Internet connection is interrupted.\
        \nRenewing your IP address either reassigns your current address (if it's still available) or assigns a new address\
        \nto your computer, allowing you to reconnect to the Internet.")
        white();print("[Set up Wi-Fi - [Static/DHCP]")
        blue();print("When you release your IP address, your router address is released and your Internet connection is interrupted.\
        \nRenewing your IP address either reassigns your current address (if it's still available) or assigns a new address\
        \nto your computer, allowing you to reconnect to the Internet.")

        continue_input = input("[y/n] | Continue: ")

        while continue_input != "y" and continue_input != "Y" and continue_input != "n" and continue_input != "N":

            red();print(f"[{continue_input}] It's a wrong choice\nPlease select a correct option")
            white();continue_input = input("[y/n] | Continue: ")

        if continue_input == "y" or continue_input == "Y":

            wifi_set_ip()

        else:

            exit()

    elif choice == 4:

        apiconfig()

    else:

        red();print("An unexpected error has occurred [error code: 131]")

    time.sleep(2)
    os.system("clear")
    apiconfig()

def wifi_set_up(ssid,ssidpwd):

    time.sleep(1)
    print("\n")

    #wireless = Wireless()
    #wireless.interface()
    #wireless.connect(ssid=ssid,password=ssidpwd)


    net = network.WLAN(network.STA_IF)

    net.active (True) 
    net.connect (f"{ssid}", f"{ssidpwd}")

    for x in tqdm(range(5)):
        print("",end='\r')
        time.sleep(0.1)

    timeout = 1

    try:

        print("Checking Connection")
        requests.head("https://google.es",timeout=timeout)

        wifi = True

        if wifi == True:

            green();print(f"Connection established with {ssid}")

    except:

        red();print(f"Unable to connect to the network {ssid}")

    time.sleep(2)
    os.system("clear")
    apiconfig()

#------------------------------BRIGHTNESS_ADAPTERS------------------------------
def brightness_adapter():
    
    global bri_adapter
    process = subprocess.check_output("xrandr | grep \" connected\" | cut -f1 -d \" \"", shell=True)
    encoding = sys.getdefaultencoding()
    bri_adapter = process.decode(encoding)


#------------------------------BRIGHTNES_SETTINGS------------------------------
def brightness(leveĺ_brightness):
    
    brightness_adapter()
    global bri_adapter

    for i in tqdm(range(1)):
            print("",end='\r')
            time.sleep(0.07)

    os.system(f"xrandr --output {bri_adapter[:-1]} --brightness {leveĺ_brightness}")
    green();print("Brightness set correctly.")

    time.sleep(2)
    os.system("clear")
    apiconfig()

#------------------------------BLUETOOHT_SETTINGS------------------------------
def bluetooth():

    os.system("clear")

    print("[1] | Start/Stop Bluethooth Service\
        \n[2] | Connect Device\
        \n[3] | Disconnect Device")

    choice = int(input("Select: "))

    while choice < 1 or choice > 3:

        choice = int(input("Select: "))

    if choice == 1:

        process = subprocess.check_output("bluetoothctl status", shell=True)
        encoding = sys.getdefaultencoding()
        blue_status = process.decode(encoding)

        print(blue_status)

        try:

            os.system("rfkill block bluetooth")
            os.system("bluetoothctl power off")

        except:

            os.system("bluetoothctl power on")
            os.system("rfkill unblock bluetooth")

    elif choice == 2:

        os.system("rfkill unblock bluetooth")
        os.system("sudo service bluetooth start")
        white();print("Listing available Bluetooth devices")

        red();

        os.system("bluetoothctl scan on")
        blue();device = input("Write the name of your device")
        print("Connecting to the device...")

        os.system(f"bluetoothctl pair \"{device}\"")

        for i in tqdm(range(7)):
            print("",end='\r')
            time.sleep(0.05)

        green();print("Successfully connected")

        time.sleep(2)
        os.system("clear")
        apiconfig()

    elif choice == 3:

        print("Disconnecting from the device")
        os.system(f"bluetoothctl disconnect {device}")

        for i in tqdm(range(3)):
            print("",end='\r')
            time.sleep(0.03)

        green();print("Disconnected successfully")

        time.sleep(2)
        os.system("clear")
        apiconfig()

#------------------------------LOCK_SETTINGS------------------------------
def lock():

    sure = input("[y/n] Are you sure you want to lock your computer?: ")

    while sure != "Y" and sure != "y" and sure != "N" and sure != "n":

        red();print(f"[{sure}] It's a wrong choice\nPlease select a correct option")
        white();sure = input("[y/n] Are you sure you want to lock your computer?: ")

    if sure == "N" or sure =="n":

        apiconfig()

    elif sure == "Y" or sure =="y":
        
        print("Locking your screen...")
        time.sleep(0.5)
        os.system("gnome-screensaver-command --lock")

#------------------------------CONDITION_SETTINGS------------------------------
def condition(num_condition):

    if num_condition == 1:

        sure = input("[y/n] Are you sure you want to turn off your computer?: ")

        while sure != "Y" and sure != "y" and sure != "N" and sure != "n":

            red();print(f"[{sure}] It's a wrong choice\nPlease select a correct option")
            white();sure = input("[y/n] Are you sure you want to turn off your computer?: ")

        if sure == "N" or sure =="n":

            apiconfig()

        elif sure == "Y" or sure == "y":

            print("Shutdown of")

            num = 3
            for e in range(3):
                print(f"{num}" + "...",end="\r")
                num -= 1
                time.sleep(1)

            os.system("sudo shutdown now")

    elif num_condition == 2:

        sure = input("[y/n] Are you sure you want to reboot your computer?: ")

        while sure != "Y" and sure != "y" and sure != "N" and sure != "n":

            red();print(f"[{sure}] It's a wrong choice\nPlease select a correct option")
            white();sure = input("[y/n] Are you sure you want to reboot your computer?: ")

        if sure == "N" or sure =="n":

            apiconfig()

        elif sure == "Y" or sure == "y":

            print("Rebooting of")

            num = 3
            for e in range(3):
                print(f"{num}" + "...",end="\r")
                num -= 1
                time.sleep(1)

            os.system("sudo reboot now")

    elif num_condition == 3:

        sure = input("[y/n] Are you sure you want to log out your computer?: ")

        while sure != "Y" and sure != "y" and sure != "N" and sure != "n":

            red();print(f"[{sure}] It's a wrong choice\nPlease select a correct option")
            white();sure = input("[y/n] Are you sure you want to log out your computer?: ")

        if sure == "N" or sure =="n":

            apiconfig()

        elif sure == "Y" or sure == "y":

            print("Logging out of")

            num = 3
            for e in range(3):
                print(f"{num}" + "...",end="\r")
                num -= 1
                time.sleep(1)

            os.system("kill -9 -1")

    else:red();print("An unexpected error has occurred [error code: 212]")

#------------------------------SOUND_SETTINGS------------------------------
def mute():

    process = subprocess.check_output("amixer sget Master", shell=True)
    encoding = sys.getdefaultencoding()
    get_sound = process.decode(encoding)

    print(get_sound)

    try:
        
        os.system("amixer set Master mute")

    except:

        os.system("amixer set Master unmute")
    

    time.sleep(2)
    os.system("clear")
    apiconfig()

def sound_level(level_sound):
    
    per_sound = level_sound * 10
    print(per_sound)

    os.system(f"amixer set Master {per_sound}")

    for i in tqdm(range(9)):
            print("",end='\r')
            time.sleep(0.01)

    green;print(f"Volume to {per_sound}%")
    
    time.sleep(2)
    os.system("clear")
    apiconfig()
    
#------------------------------INDEX------------------------------
def apiconfig():

    red();print("Python Control Center (For Linux)\n    Code by WUAL\n")

    now = time.strftime("%c")
    blue();print("%s" %now)

    battery = psutil.sensors_battery() 
    print("Battery", int(battery.percent), "%")

    green();print("\n[1] | 直 Wifi Setting\
        \n[2] |  Bluetooth Settings\
        \n[3] |  Brightness Setting\
        \n[4] |  Sound \ Audio\
        \n[5] |  Lock Screen\
        \n[6] |  Shutdown \ Restart \ Logout\
        \n[7] |  More Settings\
        \n\n[8] | (?) Help \
        \n[9] |  Exit")

    section = int(input("Elige un "))

    while section < 1 or section > 8:

        red();print(f"[{section}] It's a wrong choice\nPlease select a correct option")
        section = int(input("Elige un "))

    #wifi
    if section == 1:

        os.system("clear")
        blue();print("Choice")

        white();print("\
            \n[1] | Turn Wi-Fi ON or OFF\
            \n[2] | Set up Wi-Fi\
            \n[3] | Configure IPv4\
            \n\n[4] Go back")

        blue();choice = int(input("Select an option: "))

        while choice < 0 or choice > 4: 

            os.system("clear")

            red();print(f"[{choice}] It's a wrong choice\nPlease select a correct option")

            white();print("\
                \n[1] | Turn Wi-Fi ON or OFF\
                \n[2] | Set up Wi-Fi\
                \n\n[3] | Configure IPv4\
                \n[4] Go back")

            blue();choice = int(input("Select an option: "))

        if choice == 1:

            wifi_turnon_turnoff()

        elif choice == 2:

            blue();print("Showing Available Wi-Fi Networks")
            os.system("nmcli dev wifi")

            global ssid;global ssidpwd
            ssid = input("\nWrite the SSID: ")
            ssidpwd = Password("Write the password: ")
            p = ssidpwd.launch()

            wifi_set_up(ssid,ssidpwd)

        elif choice == 3:

            wifi_set_ip()

        elif choice == 4:

            apiconfig()  
    
    #Bluethooth
    elif section == 2:

        bluetooth()  

    #brightness
    elif section == 3:

        white();brightness_input = float( input("Brightness Level: "))

        while brightness_input > 10 or brightness_input < 0:

            red();print("Set a brightness level between 0 and 10");white()
            brightness_input = float(input("Brightness Level: "))

        brightness_level = brightness_input/10

        brightness(brightness_level)
    
    #Sound
    elif section == 4:

        os.system("clear")

        print("[1] | Mute / Unmuted\
            \n[2] | Sound Level\
            \n\n[3] | Go Back")

        choice = int(input("Select: "))

        while choice < 1 or choice > 3:

            choice = int(input("Select: "))

        if choice == 1:

            mute()

        elif choice == 2:

            level_sound = int(input("(0-10) | Sound Level: "))

            while level_sound < 0 or level_sound > 10:

                red();print(f"[{level_sound}] It's a wrong choice\nPlease select a correct option")
                white();level_sound = int(input("(0-10) | Sound Level: "))

            sound_level(level_sound)
            

        elif choice == 3:
            apiconfig()
    
    #Lock Screen    
    elif section == 5:

        lock()

    #Shutdown Restart Logout
    elif section == 6:

        os.system("clear")

        blue();print("[1] | Shutdown\
            \n[2] | Restart\
            \n[3] | Logout")  

        white();num_condition = int(input("\nChoose your state: "))

        while num_condition > 3 or num_condition < 1:

            red();print(f"{num_condition} It is an Incorrect Option.\nWrite a correct option")
            white();num_condition = int(input("\nChoose your state: "))

        condition(num_condition)

    #More Configuration 
    elif section == 7:

        os.system("clear")

        control_center_r = open('config/control-center','r')
        control_center = control_center_r.read()
        control_center_r.close()

        green();print("Opening configuration APP")

        os.system(f"{control_center}")

        time.sleep(2)
        os.system("clear")
        apiconfig()
    
    elif section == 8:

        print("")

    elif section == 9:

        exit()

    else:red();print("An unexpected error has occurred [error code: 011]")

if __name__ == '__main__':
    apiconfig()
