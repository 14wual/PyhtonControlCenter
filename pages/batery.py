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
import tkinter
import psutil


# --------------------VAR & CONS--------------------
def check_battery_psutil():
    battery = psutil.sensors_battery() 

    if battery.power_plugged:
        return True, int(battery.percent)
    else:
        return False, int(battery.percent)

# --------------------APP--------------------
def main(self):
    battery(self)
   
def battery(self):

    check_battery_image_var(self)                           

    self.battery_label_var = tkinter.IntVar(value=check_battery_label_var())

    self.battery_label = customtkinter.CTkLabel(self.main_frame,textvariable=self.battery_label_var)
    self.battery_label.grid(row=5,column=1,padx=5,pady=5)

def check_battery_label_var():

    checked_battery_psutil = check_battery_psutil()

    if checked_battery_psutil[0] == True:
        value = f"Battery Charging: {checked_battery_psutil[1]}%"
    else:
        if checked_battery_psutil[1] <= 20:
            value = f"Battery Low: {checked_battery_psutil[1]}%"
        if checked_battery_psutil[1] >= 90:
            value = f"Battery High: {checked_battery_psutil[1]}%"
        else:
            value = f"Battery Level: {checked_battery_psutil[1]}%"
    
    return value

def check_battery_image_var(self):

    checked_battery_psutil = check_battery_psutil()

    if checked_battery_psutil[0] == True:
        self.battery_image = customtkinter.CTkImage(light_image=Image.open("images/battery-charg.png"),
                                    dark_image=Image.open("images/battery-charg-light.png"),
                                    size=(15, 15))
    else:
        if checked_battery_psutil[1] >= 20:
            self.battery_image = customtkinter.CTkImage(light_image=Image.open("images/battery.png"),
                                    dark_image=Image.open("images/battery-light.png"),
                                    size=(15, 15))
        else:
            self.battery_image = customtkinter.CTkImage(light_image=Image.open("images/battery-low.png"),
                                    dark_image=Image.open("images/battery-low-light.png"),
                                    size=(15, 15))

    self.battery_label_image = customtkinter.CTkLabel(self.main_frame,image=self.battery_image,text="")
    self.battery_label_image.grid(row=5,column=0,padx=5,pady=5)