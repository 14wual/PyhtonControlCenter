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
def apiconfig(level_sound):
    
    per_sound = level_sound * 10
    print(per_sound)

    os.system(f"amixer set Master {per_sound}")

    for i in tqdm(range(9)):
            print("",end='\r')
            time.sleep(0.01)

    green;print(f"Volume to {per_sound}%")
    

if __name__ == '__main__':
    
    level_sound = int(input("(0-10) | Sound Level: "))

    while level_sound < 0 or level_sound > 10:

        red();print(f"[{level_sound}] It's a wrong choice\nPlease select a correct option")
        white();level_sound = int(input("(0-10) | Sound Level: "))

    apiconfig(level_sound)