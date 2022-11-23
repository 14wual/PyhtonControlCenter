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
from wireless import Wireless
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

#------------------------------SCRIPT------------------------------
def apiconfig():
    pass

if __name__ == '__main__':
    apiconfig()