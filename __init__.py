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
from pages import main

# --------------------APP--------------------
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Python Control Center")
        self.wm_attributes("-topmost", 1)
        self.resizable(0, 0)

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3), weight=0)

        main.main(self)

    #... program methods ...

if __name__ == '__main__':
    app = App()
    app.mainloop()