route = $pwd
croute = $HOME/.config

if route == $pwd
do
    launch()
done

launch() {
    banner()
    config()
    pip()
    apt()
}

banner() {
    echo '''
    ██╗    ██╗██╗   ██╗ █████╗ ██╗     
    ██║    ██║██║   ██║██╔══██╗██║     
    ██║ █╗ ██║██║   ██║███████║██║     (code by WUAL)          
    ██║███╗██║██║   ██║██╔══██║██║     
    ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝
    '''
    
    echo 'Welcome $whoami, thank you for trusting in PCC'
    echo 'Next, the repository will be installed'
}

config() {

    #We update the system
    sudo apt update -y
    sudo apt-get update -y
    sudo apt upgrade -y

    #We install pip, in case it is not installed
    sudo apt-get install python3-pip -y
    sudo apt install pip pip3 -y

    echo 'You will need to modify the following files manually by typing your default control center at the end of the installation'

    #We copy the options of the script
    sudo mkdir $config_route/.config
    sudo cp ./options $croute/.config/pcc -r

    #We copy the command in /bin/
    sudo cp ./pcc /bin/
    sudo chmod +x /bin/pcc
}

pip() {

    #We install the pip
    installer = ("tqdm","bullet","psutil","network")

    for x in installer
    do
        pip install $x
        pip3 install $x

        python3 -m pip show $x
    done
}

apt() {

    #We install the apt
    installer = ("gnome-screensaver","git","python3")

    for x in installer
    do
        sudo apt install $x
        sudo apt-get install $x

        apt-cache policy $x
    done
}
