import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

format = figlet_format('10 x 10', font='doh', width = 100)

cprint(format, 'blue', 'on_red', attrs=['bold'])
