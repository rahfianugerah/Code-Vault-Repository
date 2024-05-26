import os # Import os
import colorama # Import colorama

from colorama import Fore, Style

colorama.init(autoreset=True)
w = Fore.WHITE+Style.BRIGHT
g = Fore.GREEN+Style.BRIGHT

os.system('cls') # Clear out terminal

while True:
    user = input(f"{w}"+"[user@user]~$ "+f"{g}")
    if user == 'clear': # Clear out terminal
        os.system('cls')
    elif user == 'exit':
        exit() # Exit progream
