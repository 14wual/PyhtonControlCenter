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
import screen_brightness_control as sbc

# --------------------VAR & CONS--------------------
screen_current_brightness = sbc.get_brightness()
current_brightness =  screen_current_brightness[0]

# --------------------APP--------------------
def main(self):
    brightness(self)
   
def brightness(self):

    self.brightness_image = customtkinter.CTkImage(light_image=Image.open("images/brightness.png"),
                                  dark_image=Image.open("images/brightness-light.png"),
                                  size=(15, 15))

    self.brightness_label_image = customtkinter.CTkLabel(self.main_frame,text="",image=self.brightness_image)
    self.brightness_label_image.grid(row=1,column=0,padx=5,pady=5)

    self.brightness_slider_var = tkinter.IntVar(value=current_brightness)

    self.brightness_slider = customtkinter.CTkSlider(self.main_frame, from_=0, to=100, command=brightness_slider_event,variable=self.brightness_slider_var)
    self.brightness_slider.grid(row=1,column=1,columnspan=2,padx=5,pady=5)

def brightness_slider_event(value):

    sbc.set_brightness(value)