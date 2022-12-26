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
import requests
import subprocess
import platform
import wmi
import tkinter as tk

# --------------------VAR & CONS--------------------
TIMEOUT = 1
dark_color = "#2b2b2b"

def check_sys_os():    
    os = platform.system()
    return os

def check_wifi_connected_label():
    
    checked_os = check_sys_os()
    
    if checked_os == "Windows":

        result = subprocess.run(["netsh", "wlan", "show", "interfaces"], stdout=subprocess.PIPE)
        output = result.stdout.decode("utf-8").strip().split("\n")

        ssid = "" 
        list_ssid = ""

        for line in output:

            if "SSID" in line:
                ssid = line.split(":")[1].strip()    
                
        if ssid == "":
            value = "Not connected to any network"
        else:
            value = f"Connected to {ssid}"

        return value

    elif checked_os == "Linux":

        result = subprocess.run(["iwgetid"], stdout=subprocess.PIPE)
        ssid = result.stdout.decode().strip()
        access_point = ssid
        value = f"Connected to {access_point}"

    return value

current_wifi_connected = check_wifi_connected_label()

# --------------------APP--------------------
def main(self):
    wifi(self)
   
def wifi(self):

    self.wifi_image = customtkinter.CTkImage(light_image=Image.open("images/wifi.png"),
                                  dark_image=Image.open("images/wifi-light.png"),
                                  size=(15, 15))

    self.wifi_label_image = customtkinter.CTkLabel(self.main_frame,image=self.wifi_image,text="")
    self.wifi_label_image.grid(row=3,column=0,padx=5,pady=5)

    self.wifi_combobox = customtkinter.CTkOptionMenu(master=self.main_frame,
                                       values=["Wifi Connect", "Set Up Wi-Fi","Turn ON/OFF Wifi"],
                                       command=lambda option:wifi_optionmenu_callback(self,option),
                                       fg_color=(dark_color),button_color=(dark_color),hover=False,)
    self.wifi_combobox.grid(row=3,column=1,padx=5,pady=5,columnspan=2)
    self.wifi_combobox.set(current_wifi_connected)

def wifi_optionmenu_callback(self,choice):

    if choice == "Turn ON/OFF Wifi":

        status = check_wifi_status()
        if status == "habilitado" or status == "enabled":
            toggle_wifi(False)
        elif status == "deshabilitado" or status == "disabled":
            toggle_wifi(True)

    elif choice == "Set Up Wi-Fi":

        checked_os = check_sys_os()

        if checked_os == "Windows":
            try:subprocess.run(["control", "/name", "Microsoft.NetworkAndSharingCenter"])
            except:subprocess.run(["control", "/name", "Microsoft.NetworkAndInternetSettings"])
        elif checked_os == "Linux":
            subprocess.run(["nm-connection-editor"])
        
    elif choice == "Wifi Connect":
        wifi_connect_dialog(self)

def wifi_connect_dialog(self):

    self.window = customtkinter.CTkToplevel(self)
    self.window.wm_attributes("-topmost", 1)
    self.window.title("Wifi Connect")
    self.window.resizable(0, 0)

    self.label = customtkinter.CTkLabel(self.window, text="Wifi Avilable",font=customtkinter.CTkFont(weight="bold",size=16))
    self.label.pack(side="top", fill="both", expand=True, padx=10, pady=10)

    result = subprocess.run(["netsh", "wlan", "show", "networks"], stdout=subprocess.PIPE)
    output = result.stdout.decode("utf-8").strip().split("\n")
    ssids = []
    for line in output:
        if "SSID" in line:
            ssid = line.split(":")[1].strip()
            ssids.append(ssid)

    self.frame_ssid = customtkinter.CTkFrame(self.window)
    self.frame_ssid.pack()

    self.selected_ssid = tk.StringVar()

    row = 0 
    for x in ssids:

        if len(x) == 0:
            pass
        else:
            self.label_ssid = customtkinter.CTkRadioButton(self.frame_ssid,variable=self.selected_ssid, text=x, command=lambda ssid=x: select_ssid(self,ssid),value=x)
            self.label_ssid.grid(row=row,column=0,padx=10,pady=10)
            row+=1

    self.password_entry = customtkinter.CTkEntry(self.frame_ssid,show="*",placeholder_text="password")
    self.password_entry.grid(row=row,column=0,padx=10,pady=10)

    self.connect_button = customtkinter.CTkButton(self.frame_ssid,text="Connect",fg_color=dark_color, border_width=1, text_color=("gray10", "#DCE4EE"),hover=False,border_color="#fff",command=lambda:wifi_connect_dialog_event(self))
    self.connect_button.grid(row=row+1,column=0,padx=10,pady=10)

def select_ssid(self,ssid):
    return ssid

def wifi_connect_dialog_event(self):
    ssid = self.selected_ssid.get()
    password = self.password_entry.get()
    connect_to_wifi(ssid,password)

def connect_to_wifi(ssid, password):
    subprocess.run(["netsh", "wlan", "add", "profile", f"filename=\\\"{ssid}.xml\\\""])
    subprocess.run(["netsh", "wlan", "connect", "name=\\\"{ssid}\\\"", f"password=\\\"{password}\\\""])

def check_wifi_status():

    result = subprocess.run(["netsh", "wlan", "show", "interfaces"], stdout=subprocess.PIPE)
    output = result.stdout.decode("utf-8").strip().split("\n")

    status = ""

    for line in output:
        if "Estado" in line or "Status" in line:
            status = line.split(":")[1].strip()
            break
    
    return status

def toggle_wifi(on):
    if on:
        subprocess.run(["netsh", "wlan", "start", "hostednetwork"])
    else:
        subprocess.run(["netsh", "wlan", "stop", "hostednetwork"])