import os
import colorama

from colorama import Fore,Style

colorama.init(autoreset=True)
w = Fore.WHITE+Style.BRIGHT
g = Fore.GREEN+Style.BRIGHT
os.system('cls')
while True:
    user = input(f"{w}"+"[user@user]~$ "+f"{g}")
    if user == 'clear':
        os.system('cls')
    elif user == 'exit':
        exit()
