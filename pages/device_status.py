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
import platform
import os
import subprocess
from ctypes import windll

# --------------------VAR & CONS--------------------
dark_color = "#2b2b2b"
EWX_REBOOT = 0x00000002
EWX_LOGOFF = 0

# --------------------APP--------------------
def main(self):
    device_status(self)
   
def device_status(self):

    self.device_status_image = customtkinter.CTkImage(light_image=Image.open("images/device-status.png"),
                                  dark_image=Image.open("images/device-status-light.png"),
                                  size=(15, 15))

    self.device_status_label_image = customtkinter.CTkLabel(self.main_frame,image=self.device_status_image,text="")
    self.device_status_label_image.grid(row=8,column=0,padx=5,pady=5)

    self.device_status_combobox = customtkinter.CTkOptionMenu(master=self.main_frame,
                                       values=["Shutdown", "Reboot", "Sign Out"],
                                       command=lambda option:device_status_optionmenu_callback(self,option),
                                       fg_color=(dark_color),button_color=(dark_color),hover=False,)
    self.device_status_combobox.grid(row=8,column=1,padx=5,pady=5,columnspan=2)
    self.device_status_combobox.set("Device Options (shutdown,..)")

def device_status_optionmenu_callback(self,option):

    if option == "Shutdown":
        sure(self,option)
    elif option == "Reboot":
        sure(self,option)
    elif option == "Sign Out":
        sure(self,option)

def sure(self,option):
    
    self.device_status_dialog_window = customtkinter.CTkToplevel(self)
    self.device_status_dialog_window.title("Lock Screen?")
    self.device_status_dialog_window.wm_attributes("-topmost", 1)
    self.device_status_dialog_window.resizable(0, 0)

    self.device_status_dialog_window_frame = customtkinter.CTkFrame(self.device_status_dialog_window)
    self.device_status_dialog_window_frame.grid(row=0, column=0)

    self.device_status_dialog_window_label = customtkinter.CTkLabel(self.device_status_dialog_window_frame, text=f"Are you sure to {option}?",font=customtkinter.CTkFont(weight="bold",size=16))
    self.device_status_dialog_window_label.grid(row=1,column=0,padx=5,pady=5,columnspan=2)

    self.device_status_button_1 = customtkinter.CTkButton(self.device_status_dialog_window_frame,text="Cancel",command=self.device_status_dialog_window.destroy,fg_color=dark_color, border_width=1, text_color=("gray10", "#DCE4EE"),hover=False,border_color="#fff",width=200)
    self.device_status_button_1.grid(row=2,column=0,padx=5,pady=5)

    self.device_status_button_2 = customtkinter.CTkButton(self.device_status_dialog_window_frame,text=option,fg_color=dark_color, border_width=1, text_color=("gray10", "#DCE4EE"),hover=False,border_color="#fff",width=200,command=lambda option:device_status_optionmenu_callback_event(option))
    self.device_status_button_2.grid(row=2,column=1,padx=5,pady=5)

def check_sys_os():    
    os = platform.system()
    return os


def device_status_optionmenu_callback_event(option):
    
    checked_os = check_sys_os()
    
    if checked_os == "Windows":

        if option == "Shutdown":
            try:os.system("shutdown /s /t 1")
            except:subprocess.run("shutdown -s")
        elif option == "Reboot":
            try:subprocess.run("shutdown -r")
            except:windll.user32.ExitWindowsEx(EWX_REBOOT, 0)
        elif option == "Sign Out":
            try:subprocess.run("shutdown -r")
            except:windll.user32.ExitWindowsEx(EWX_LOGOFF, 0)

    if checked_os == "Linux":

        if option == "Shutdown":
            try:subprocess.run("shutdown -h now", shell=True)
            except:subprocess.run("shutdown -h")
        elif option == "Reboot":
            try:subprocess.run("shutdown -r now", shell=True)
            except:os.system("reboot now")
        elif option == "Sign Out":
            try:subprocess.run("gnome-session-quit")
            except:os.system("kill -9 -1")