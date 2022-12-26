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

def main(self):
    separator(self)

def separator(self):

    
    self.separator_image = customtkinter.CTkImage(light_image=Image.open("images/separator.png"),
                                    dark_image=Image.open("images/separator-light.png"),
                                    size=(250, 15))

    self.label_image = customtkinter.CTkLabel(self.main_frame,image=self.separator_image,text="")
    self.label_image.grid(row=2,column=0,padx=5,pady=0,columnspan=3)

    self.label_image = customtkinter.CTkLabel(self.main_frame,image=self.separator_image,text="")
    self.label_image.grid(row=6,column=0,padx=5,pady=0,columnspan=3)

    self.label_image = customtkinter.CTkLabel(self.main_frame,image=self.separator_image,text="")
    self.label_image.grid(row=9,column=0,padx=5,pady=0,columnspan=3)