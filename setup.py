from setuptools import setup

setup(
    name='PythonControlCenter',
    version='2.0.0',
    description='Python Control Center is a control center for linux & windows with GUI designed for "bspwm" environments where we dont find the classic xorg or gnome cc as in common graphical environments',
    install_requires=[
        'customtkinter',
        'PIL.Image',
        'psutil',
        'tkinter',
        'wmi',
        'subprocess'
        'win32com.client',
        'platform',
        'screen_brightness_control',
        'ctypes',
        'os'
        'requests'
    ],
)
