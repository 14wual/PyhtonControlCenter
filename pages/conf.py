# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# PyhtonControlCenter - PCC - V2.0.0
# See proyect >> https://github.com/14wual/PyhtonControlCenter
# Follow Me >> https://twitter.com/codewual

# --------------------External Imports--------------------
import customtkinter
from PIL import Image
import subprocess
import platform
import subprocess
    
# --------------------VAR & CONS--------------------
dark_color = "#2b2b2b"

# --------------------APP--------------------
def main(self):
    conf(self)

def check_sys_os():    
    os = platform.system()
    return os   
   
def conf(self):    

    self.conf_image = customtkinter.CTkImage(light_image=Image.open("images/conf.png"),
                                  dark_image=Image.open("images/conf-light.png"),
                                  size=(15, 15))

    self.lock_image = customtkinter.CTkLabel(self.main_frame,image=self.conf_image,text="")
    self.lock_image.grid(row=10,column=0,padx=5,pady=5)

    self.lock_label = customtkinter.CTkButton(self.main_frame,text="More Settings",command=conf_event,fg_color=dark_color, border_width=1, text_color=("gray10", "#DCE4EE"),hover=False,border_color="#fff",width=200)
    self.lock_label.grid(row=10,column=1,padx=5,pady=5,columnspan=2)

def conf_event():

    checked_os = check_sys_os()
    
    if checked_os == "Windows":
        subprocess.run(['start', 'ms-settings:'], shell=True)
    elif checked_os == "Linux":
        try:subprocess.run(['gnome-control-center'])
        except:subprocess.run(['kcontrol'])