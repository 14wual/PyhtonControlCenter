'''
██╗    ██╗██╗   ██╗ █████╗ ██╗     
██║    ██║██║   ██║██╔══██╗██║     
██║ █╗ ██║██║   ██║███████║██║     (code by WUAL)          
██║███╗██║██║   ██║██╔══██║██║     
╚███╔███╔╝╚██████╔╝██║  ██║███████╗
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝
'''

#------------------------------IMPORT------------------------------
from sys import stdout
import subprocess

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
    red();print("This script is currently under development, you can try it from the main script but it may fail")

    white();sure = input("[y/n] Want to try it: ")

    while sure != "Y" and sure != "y" and sure != "N" and sure != "n":

        red();print(f"[{sure}] It's a wrong choice\nPlease select a correct option - y/n")
        white();sure = input("[y/n] Want to try it: ")
    
    if sure == "y" or sure == "Y":

        subprocess.call("python3 control-center.py",shell=True)
    
    elif sure == "n" or sure == "N":

        exit()

if __name__ == '__main__':
    apiconfig()