import keyboard

def mywait():
    keyboard.read_key()

def my_function():
    print("hello")

def my_exit():
    quit()

keyboard.add_hotkey('h', my_function)
keyboard.add_hotkey('esc', my_exit)

while True:
    mywait()