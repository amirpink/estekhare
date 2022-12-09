import random
from colorama import Fore
import os
import colorama

os.system("cls")


baner = (Fore.YELLOW+"""

  ______  _____ _______ ______ _  ___    _          _____  ______ 
 |  ____|/ ____|__   __|  ____| |/ / |  | |   /\   |  __ \|  ____|
 | |__  | (___    | |  | |__  | ' /| |__| |  /  \  | |__) | |__   
 |  __|  \___ \   | |  |  __| |  < |  __  | / /\ \ |  _  /|  __|  
 | |____ ____) |  | |  | |____| . \| |  | |/ ____ \| | \ \| |____ 
 |______|_____/   |_|  |______|_|\_\_|  |_/_/    \_\_|  \_\______|
""")

print(baner)

a = [Fore.GREEN+"\n                      <----khobe---->",Fore.RED+"\n                       <----bade---->" ]

estekhare = random.choice(a)

print(estekhare)
print(     )

while True:

    print(Fore.GREEN+"[1]" +Fore.WHITE+ " ===> Again " "\n" +Fore.GREEN+ "[2]" +Fore.WHITE +" ===> Exit")

    one = "1"
    tuw = "2"

    javab = input("1 or 2? :")


    if javab == one:
        os.system("python estekhare.py")

    if javab == tuw:
        os.system("cls")
        os.system("cmd")
    else:
        print( Fore.RED+ "Please select 1 or 2 ! ! !")   

