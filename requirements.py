from sys import stdout
import os

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

def introduction():
    green();print("Before you can use the control center you must install several requirements (pips, apts, ..)\
    \nand configure certain parameters to be able to use the script correctly.")

def pip():
    pips = ("os","subprocess","tqdm","tqdm.auto","sys","requests","time","Wireless","bullet","pybluez")
    for i in pips:
        blue();print(f"Installing {i}")
        white();os.system(f"sudo pip install {i}")
        white();os.system(f"pip install {i}")
        green();print(f"[{i}] | Install sucessfull")
    print("\n")
    for i in pips:
        green();print(f"You have installed {i}")

def apt():
    pass

def conf():
    pass

def installall():
    pip()
    apt()
    conf()

def helps():
    pass

def api():
    red();print("REMEMBER THAT YOU MUST INSTALL EVERYTHING FOR GOOD OPERATION")
    blue();print("What do you want to install?")

    green();print("\n     [1] | INSTALL All\n")
    blue();print("      [2] | PIP Installers\
                \n      [3] | APT Installer\
                \n      [4] | Required Settings\
                \n\n      [5] | Help (?)\
                \n      [6] | Exit")
                
    
    white();choice = int(input("\nChoose an option: "))

    while choice < 1 or choice > 6:
        red();print(f"{choice} It is an Incorrect Option.\nWrite a correct option")
        white();choice = int(input("Choose an option: "))

    if choice == 1:
        installall()
    elif choice == 2:
        pip()
    elif choice == 3:
        apt()
    elif choice == 4:
        conf()
    elif choice == 5:
        helps()
    elif choice == 6:
        exit()

if __name__ == '__main__':
    introduction()
    api()
