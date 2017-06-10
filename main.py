#__author__='Hussam Ashraf'
#! /usr/bin/env

import colorama
from colorama import Fore, Back, Style
import subprocess
import os
from commandLine import *
from gui import *

def mainScript():
    colorama.init()
    print(Fore.GREEN + \
        "_____________________________________________________\n"
        "       __               _                        _   \n"
        "      /  \    _ __  ___| |     ___ _    _  ___ _' '_ \n"
        "     / /\ \  | '__|/ __| |___ / __| |  | |/ __|__ __|\n"
        "    / /__\ \ | |  | (__| / \ \ (__| |  | |\__ \ | |  \n"
        "   /_/    \_\|_|   \___|_| |_|\___\_\__/_/|___/ |_|  \n"
    )
    print('________________Arch Linux Customizer________________ ')
    print("_____________________________________________________ \n")
    print(Style.RESET_ALL)


    version = str(subprocess.check_output('python --version', shell=True))

    if '3.6' in version:
        pass
    else:
        pythonVr = input(

            '==> Do you want to install Python3.6 and make it default? [y/n]\n'
            '==> -----------------------------------------------------------\n'
            '==> ').lower()

        if userChoice == 'y':
            subprocess.check_output('yaourt -S python', shell=True)
        else:
            print('==> Keeping your current version of Python which is "%s"' %version[2:-3])

    chckDistro = str(subprocess.check_output('cat /etc/*-release', shell=True)).lower()

    if 'manjaro' in chckDistro:

        while True:

            usrInpt = input('==> Do you want to set ScreenShot shortcut?! [Y/n]').lower()

            if usrInpt == 'y':

                subprocess.check_output('xset b off', shell=True)
                usrName = str(subprocess.check_output('whoami', shell=True))
                usrNme = usrName[2:-3]

                os.chdir('/home/{}/.config/xfce4/xfconf/xfce-perchannel-xml'.format(usrNme))

                config = open('xfce4-keyboard-shortcuts.xml', 'r')
                configTxt = config.read()

                SCPostion = configTxt.find('"xfce4-terminal"/>')
                SCPostionTxt = configTxt[:SCPostion+18] +'\n'+'      '+'<property name="Print" type="string" value="xfce4-screenshooter -f"/>'+configTxt[SCPostion+18:]

                config = open('xfce4-keyboard-shortcuts.xml', 'w')
                config.write(SCPostionTxt)
                config.close()
                print('==> ' + Fore.BLUE + Back.WHITE + ' Done, Please reboot your machine to use it. ' + Style.RESET_ALL + '\n')
                break
            elif usrInpt == 'n':
                break
            else:
                print('==> Please Enter only Y or N')

    elif 'arch' in chckDistro:
        print('Arch Linux')
    else:
        OSError

    guiCmd = input(
        '==> Do you want to continue using Command Line or Gui? [C/G]\n'
        '==> -----------------------------------------------------------\n'
        '==> ').lower()

    if guiCmd == 'c':
        try:
            install()
        except:
            pass


    elif guiCmd == 'g':
        try:
            if __name__ == '__main__':
                app = QApplication(sys.argv)
                window = gui()
                window.show()
                sys.exit(app.exec_())
        except:
            pass

if __name__ == '__main__':
    mainScript()
    

