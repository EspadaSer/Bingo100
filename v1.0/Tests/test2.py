import keyboard
import sys
from time import sleep

def kb():
    while True:
        if keyboard.is_pressed("a"):
            print("A key was pressed")
            sys.exit(0)
        



def main():

    kb()

if __name__ == "__main__":

    main()