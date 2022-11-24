
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
import time

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

    elif choice == 3:

        print("Disconnecting from the device")
        os.system(f"bluetoothctl disconnect {device}")

        for i in tqdm(range(3)):
            print("",end='\r')
            time.sleep(0.03)

        green();print("Disconnected successfully")

if __name__ == '__main__':
    bluetooth()