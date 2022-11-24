'''
██╗    ██╗██╗   ██╗ █████╗ ██╗     
██║    ██║██║   ██║██╔══██╗██║     
██║ █╗ ██║██║   ██║███████║██║     (code by WUAL)          
██║███╗██║██║   ██║██╔══██║██║     
╚███╔███╔╝╚██████╔╝██║  ██║███████╗
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝
'''

#------------------------------IMPORT------------------------------
import os
import subprocess
from tqdm.auto import tqdm
import sys
from sys import stdout
import requests
import time
from bullet import Password
import network

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

#------------------------------SCRIPT------------------------------

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

    else:

        red();print("An unexpected error has occurred [error code: 131]")


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


if __name__ == '__main__':
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