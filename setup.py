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
from sys import stdout

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

installs = ("confg","commands","pip","apt")
pip = ("tqdm","bullet","psutil","network")
apt = ("gnome-screensaver","git","python3")

def apiconfig():

    os.system("sudo apt update")
    os.system("sudo apt install pip")

    white()
    for i in installs:

        if i == "confg":

            blue;print("To finish the configuration; type the name of the command to run your setup")
            green();print("[ Example ] gnome-control-center");white()

            cc = input("Write: ")

            files = ("./scripts/other/config/control-center","./options/settings/config/control-center","config/control-center")   

            for z in files:

                file=open(f"{z}","w")

                try:

                    file.write(f"{cc}")

                finally:

                    file.close()
        
        elif i == "commands":

            os.system("sudo cp options/ $HOME/.config/pcc -r")

            try:

                green();os.system("cat $HOME/.config/pcc/options/tests-python/test.txt")
            
            except FileNotFoundError:
                
                red;("[ x ] File not copied correctly")
                white();os.system("sudo cp ./options $HOME/.config/pcc")

            os.system("sudo cp ./pcc /bin/")

            test2 = os.path.exists('/bin/pcc')

            if test2 == True:

                green();print("[ ✓ ] Command Created Successfully");white()

            else:

                red();print("[ x ] Command NOT Created Successfully");white()

            os.system("sudo chmod +x /bin/pcc")
            
        elif i == "pip":

            for x in pip:
                
                try:

                    os.system(f"pip install {x}")

                except:

                    os.system(f"sudo pip install {x}")


                test3 = os.system(f"python3 -m pip show {x}")

                if test3 == 0:
                    green();print("[ ✓ ] Pip Package Installed Successfully")
                else:
                    red();print("[ x ] Pip Package Installed Incorrectly");white()
        
        elif i == "apt":
            
            for y in apt:
                
                try:

                    os.system(f"sudo apt install {y}")

                except:

                    red();(f"Automatically install the package {y}, sorry for the inconvenience");white()

                test3 = os.system(f"apt-cache policy {y}")
            
        else:

            green();print("Thanks for using PCC!")

            os.system("pcc -h")




if __name__ == '__main__':
    apiconfig()
