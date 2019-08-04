import time
import random
import os
import platform

#Clears output to make it easier to read
def clear():
    if platform.system() == "Linux":
        os.system('clear')
    elif platform.system() == "Windows":
        os.system('cls')
