from setuptools import setup

setup(
    name='PythonControlCenter',
    version='2.0.0',
    description='Python Control Center is a control center for linux & windows with GUI designed for "bspwm" environments where we dont find the classic xorg or gnome cc as in common graphical environments',
    url='https://github.com/14wual/PyhtonControlCenter',
    author='Carlos Padilla Labella',
    author_email='cpadlab@gmail.com',
    license='GPL',
    install_requires=[
        'customtkinter',
        'pillow',
        'psutil',
        'wmi',
        'screen_brightness_control',
        'requests'
    ],
    project_urls={
        'Bug Reports': 'https://github.com/14wual/PyhtonControlCenter/issues',
        'Source': 'https://github.com/14wual/PyhtonControlCenter/blob/main/__init__.py',
    },
)
