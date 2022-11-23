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
from tqdm.auto import tqdm
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
def apiconfig(ssid,ssidpwd):

    os.system("clear")

    time.sleep(1)
    print("\n")

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

    blue();print("Showing Available Wi-Fi Networks")
    os.system("nmcli dev wifi")

    ssid = input("\nWrite the SSID: ")
    ssidpwd = Password("Write the password: ")
    p = ssidpwd.launch()

    apiconfig(ssid,ssidpwd)