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
def apiconfig():

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

if __name__ == '__main__':
    apiconfig()