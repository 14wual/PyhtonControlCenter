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
def lock():

    sure = input("[y/n] Are you sure you want to lock your computer?: ")

    while sure != "Y" and sure != "y" and sure != "N" and sure != "n":

        red();print(f"[{sure}] It's a wrong choice\nPlease select a correct option")
        white();sure = input("[y/n] Are you sure you want to lock your computer?: ")

    if sure == "N" or sure =="n":

        exit()

    elif sure == "Y" or sure =="y":
        
        print("Locking your screen...")
        time.sleep(0.5)
        os.system("gnome-screensaver-command --lock")

if __name__ == '__main__':
    lock()