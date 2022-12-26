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
import tkinter
from PIL import Image
import os
import platform

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# --------------------VAR & CONS--------------------
current_volume = 0

# --------------------APP--------------------
def main(self):
    volume(self)
   
def volume(self):

    self.volume_image = customtkinter.CTkImage(light_image=Image.open("images/volumen.png"),
                                  dark_image=Image.open("images/volumen-light.png"),
                                  size=(15, 15))

    self.volume_label_image = customtkinter.CTkLabel(self.main_frame,text="",image=self.volume_image)
    self.volume_label_image.grid(row=0,column=0,padx=5,pady=5)

    self.volume_slider_var = tkinter.IntVar(value=current_volume)

    self.volume_slider = customtkinter.CTkSlider(self.main_frame, from_=0, to=100, command=volume_slider_event,variable=self.volume_slider_var,state="disabled")
    self.volume_slider.grid(row=0,column=1,columnspan=2,padx=5,pady=5)


def check_sys_os():    
    os = platform.system()
    return os

def volume_slider_event(value):

    decibels = int(value) / 100
    print(decibels)

    checked_os = check_sys_os()
    
    if checked_os == "Windows":

        pass

    elif checked_os == "Linux":
        
        pass


