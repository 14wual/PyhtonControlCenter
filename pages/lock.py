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
import os
import ctypes
    
# --------------------VAR & CONS--------------------
dark_color = "#2b2b2b"

# --------------------APP--------------------
def main(self):
    lock(self)
   
def lock(self):

    self.lock_image = customtkinter.CTkImage(light_image=Image.open("images/lock.png"),
                                  dark_image=Image.open("images/lock-light.png"),
                                  size=(15, 15))
    
    self.lock_image = customtkinter.CTkLabel(self.main_frame,image=self.lock_image,text="")
    self.lock_image.grid(row=7,column=0,padx=5,pady=5)

    self.lock_label = customtkinter.CTkButton(self.main_frame,text="Lock Screen",command=lambda:sure(self),fg_color=dark_color, border_width=1, text_color=("gray10", "#DCE4EE"),hover=False,border_color="#fff",width=200)
    self.lock_label.grid(row=7,column=1,padx=5,pady=5,columnspan=2)

def sure(self):

    self.lock_dialog_window = customtkinter.CTkToplevel(self)
    self.lock_dialog_window.title("Lock Screen?")
    self.lock_dialog_window.wm_attributes("-topmost", 1)
    self.lock_dialog_window.resizable(0, 0)

    self.lock_dialog_window_frame = customtkinter.CTkFrame(self.lock_dialog_window)
    self.lock_dialog_window_frame.grid(row=0, column=0)

    self.lock_dialog_window_label = customtkinter.CTkLabel(self.lock_dialog_window_frame, text="Are you sure to lock screen?",font=customtkinter.CTkFont(weight="bold",size=16))
    self.lock_dialog_window_label.grid(row=1,column=0,padx=5,pady=5,columnspan=2)

    self.lock_button_1 = customtkinter.CTkButton(self.lock_dialog_window_frame,text="Cancel",command=self.lock_dialog_window.destroy,fg_color=dark_color, border_width=1, text_color=("gray10", "#DCE4EE"),hover=False,border_color="#fff",width=200)
    self.lock_button_1.grid(row=2,column=0,padx=5,pady=5)

    self.lock_button_2 = customtkinter.CTkButton(self.lock_dialog_window_frame,text="Lock Screen",fg_color=dark_color, border_width=1, text_color=("gray10", "#DCE4EE"),hover=False,border_color="#fff",width=200,command=lock_screen_event)
    self.lock_button_2.grid(row=2,column=1,padx=5,pady=5)

def check_sys_os():    
    os = platform.system()
    return os

def lock_screen_event():
    
    checked_os = check_sys_os()
    
    if checked_os == "Windows":

        try:
            ctypes.windll.user32.LockWorkStation()
        except:
            cmd='rundll32.exe user32.dll, LockWorkStation'
            subprocess.call(cmd)

    elif checked_os == "Linux":
        try:subprocess.run(["gnome-screensaver-command", "-l"])
        except:os.system("gnome-screensaver-command --lock")