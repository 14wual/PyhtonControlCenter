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
import wmi
import subprocess
import win32com.client
import platform

# --------------------VAR & CONS--------------------
TIMEOUT = 1

def check_bluethooth_connected_label():
    wmi_obj = wmi.WMI()
    adapter = wmi_obj.query("SELECT * FROM Win32_PnPEntity WHERE ClassGuid='{e0cbf06c-cd8b-4647-bb8a-263b43f0f974}' AND Status='OK'")[0]
    status = adapter.Status

    if status == "OK":
        value = "The Bluetooth is enabled"
    else:
        value = "The Bluetooth is disabled"
    return value

current_bluethooth_connected = check_bluethooth_connected_label()
dark_color = "#2b2b2b"

# --------------------APP--------------------
def main(self):
    bluethooth(self)
   
def bluethooth(self):

    self.bluethooth_image = customtkinter.CTkImage(light_image=Image.open("images/bluetooth.png"),
                                  dark_image=Image.open("images/bluethooth-light.png"),
                                  size=(15, 15))

    self.bluethooth_label_image = customtkinter.CTkLabel(self.main_frame,image=self.bluethooth_image,text="")
    self.bluethooth_label_image.grid(row=4,column=0,padx=5,pady=5)
    self.bluethooth_combobox = customtkinter.CTkOptionMenu(master=self.main_frame,
                                       values=["Bluethooth Connect", "Set Up Bluethooth","Turn ON/OFF bluethooth"],
                                       command=lambda option:bluethooth_optionmenu_callback(self,option),
                                       fg_color=(dark_color),button_color=(dark_color),hover=False,
                                       state="disabled")
    self.bluethooth_combobox.grid(row=4,column=1,padx=5,pady=5,)
    self.bluethooth_combobox.set(current_bluethooth_connected)

def bluethooth_optionmenu_callback(self,choice):
    print("optionmenu dropdown clicked:", choice)

    if choice == "Set Up Bluethooth":
        subprocess.run(["fsquirt.exe"])
    elif choice == "Turn ON/OFF bluethooth":
        turn_bluethooth()
    elif choice == "Bluethooth Connect":
        pass

def check_sys_os():    
    os = platform.system()
    return os

def scan_bluethooth_devices():

    checked_os = check_sys_os()

    if checked_os == "Windows":
        pass
    elif checked_os == "Linux":

        subprocess.run(["bluetoothctl", "scan", "on"])
        output = subprocess.run(["bluetoothctl", "devices"], capture_output=True)

#    print(output.stdout)

def turn_bluethooth():

    checked_os = check_sys_os()

    if checked_os == "Windows":
    
        checked_status = check_bluethooth_connected_label()
        status_bluethooth = win32com.client.Dispatch("BluetoothAutoConnect.BluetoothAutoConnect")

        if checked_status == "The Bluetooth is enabled":
            status_bluethooth.SetPower(0)
        elif checked_status == "The Bluetooth is disabled":
            status_bluethooth.SetPower(1)
        
    elif checked_os == "Linux":

        try:subprocess.run(["bluetoothctl", "power", "off"])
        except:subprocess.run(["bluetoothctl", "power", "on"])
