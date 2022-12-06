import sys
import keyboard
import random
import time
from numpy.random import seed
from numpy.random import randint
from colorama import init
from termcolor import cprint 
from pyfiglet import figlet_format

seed(1)
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected

lista = []

def kb():
    print("Bienvenido al Bingo de las multiplicaciones")
    print("Pulsa a para mostrar todo")
    print("Pulsa n para mostrar una operación")
    print("Pulsa l para mostrar la lista de resulados")
    while True:
        if keyboard.is_pressed("a"):
            #print("A key was pressed")
            print("******************")
            for _ in range(1):
                #num = num + 1
                value1 = random.randint(1, 10)
                value2 = random.randint(1, 10)
                value3 = value1 * value2
                while value3 in lista:
                    value1 = random.randint(1, 10)
                    value2 = random.randint(1, 10)
                    value3 = value1 * value2
                else:
                    #print("not exist")
                    lista.append(value3)
                    lista.sort()
                    print(value1, "x", value2)
                    print("=", value3)
                    print(lista)
                    time.sleep(1)

        elif keyboard.is_pressed("n"):
            print("******************")
            for _ in range(1):
                #num = num + 1
                value1 = random.randint(1, 10)
                value2 = random.randint(1, 10)
                value3 = value1 * value2
                while value3 in lista:
                    value1 = random.randint(1, 10)
                    value2 = random.randint(1, 10)
                    value3 = value1 * value2
                else:
                    #print("not exist")
                    lista.append(value3)
                    lista.sort()
                    #print(value1, "x", value2)
                    strresult = str(value1) + " x " + str(value2)
                    figletresult = figlet_format(strresult, font='doh', width = 100)
                    cprint(figletresult, 'yellow', 'on_red', attrs=['bold'])
                    #print("=", value3)
                    #print(lista)
                    time.sleep(1)  

        elif keyboard.is_pressed("l"):
            for _ in range(1):
                print(lista)
                time.sleep(1)  


        #sys.exit(0)
        



def main():

    kb()

if __name__ == "__main__":

    main()


