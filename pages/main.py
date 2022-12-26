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

# --------------------Internal Imports--------------------
from pages import volume
from pages import brightness
from pages import wifi
from pages import bluetooth
from pages import batery
from pages import lock
from pages import device_status
from pages import conf
from pages import separator

# --------------------APP--------------------
def main(self):

    self.main_frame = customtkinter.CTkFrame(self)
    self.main_frame.pack(padx=5, pady=5)

    volume.main(self)
    brightness.main(self)

    wifi.main(self)
    bluetooth.main(self)
    batery.main(self)

    lock.main(self)
    device_status.main(self)

    conf.main(self)

    separator.main(self)