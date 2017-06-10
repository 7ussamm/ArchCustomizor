#!/usr/bin/python

import subprocess
import os
import colorama
from colorama import Back, Fore, Style

colorama.init()

def changeTerminal(): #changes the Terminal command prompt


    with open ('bashrc', 'r') as file:
        bachrc = file.read()

    usrName = str(subprocess.check_output('whoami', shell=True))
    usrName = usrName[2:-3]
    os.chdir('/home/{}/'.format(usrName))

    filee = open('.bashrc', 'w')
    filee.write(bachrc)
    file.close()

def themes():

    commands = [

        'yaourt -S vertex-themes --noconfirm',

        'yaourt -S arc-cyberfox-theme --noconfirm'
    ]
    for command in commands:
        subprocess.check_output(command, shell=True)

def icons():
    comnds = [

        'yaourt -S arc-icon-theme-git --noconfirm',
        'yaourt -S buuf-icon-theme --noconfirm',
        'yaourt -S oranchelo-icon-theme --noconfirm'

    ]
    for cmd in comnds:
        subprocess.check_output(cmd, shell=True)

def install():
    while True:
        print('==> What Do You Wanna do?\n')

        print('',

            Back.GREEN + '1-' + Style.RESET_ALL + ' Install Themes\n',
            Back.GREEN + '2-' + Style.RESET_ALL + ' Install Icons\n',
            Back.GREEN + '3-' + Style.RESET_ALL + ' Customize Terminal\n'
        )
        print(
            '==> Enter n° of package to be installed,(default All, "q" to quit)\n'
            '==> ---------------------------------------------------------------'
        )

        userChoice = input('==> ')

        if userChoice == '':
            changeTerminal()
            themes()
            icons()
            print('==>' + Fore.BLUE + Back.WHITE + ' Finished Installing ' + Style.RESET_ALL + '\n')
        elif userChoice == '1':
            themes()
            print('==>' + Fore.BLUE + Back.WHITE + ' Finished Installing ' + Style.RESET_ALL + '\n')
        elif userChoice == '2':
            icons()
            print('==>' + Fore.BLUE + Back.WHITE + ' Finished Installing ' + Style.RESET_ALL + '\n')
        elif userChoice == '3':
            changeTerminal()
            print('==>' + Fore.BLUE + Back.WHITE +' Finished Installing ' + Style.RESET_ALL + '\n')
        elif userChoice == 'q':
            break
        else:
            print('==> Please Enter Valid number!!')
