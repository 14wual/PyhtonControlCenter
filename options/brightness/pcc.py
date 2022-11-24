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

if __name__ == '__main__':

    white();brightness_input = float( input("Brightness Level: "))

    while brightness_input > 10 or brightness_input < 0:

        red();print("Set a brightness level between 0 and 10");white()
        brightness_input = float(input("Brightness Level: "))

    brightness_level = brightness_input/10

    brightness(brightness_level)