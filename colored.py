import os
import platform
from datetime import datetime

from colorama import Back, Fore, Style, init


def info(item):
    '''
    Bright green output for normal information
    '''
    item = str(item)
    print(Style.BRIGHT + Fore.GREEN + '[Info] ' + item + Style.RESET_ALL)


def debugInfo(item):
    '''
    Bright red output for debug information
    '''
    item = str(item)
    print(Style.BRIGHT + Fore.RED + '[Debug] ' + item + Style.RESET_ALL)


def stateInfo(item):
    '''
    Bright output for state information
    '''
    item = str(item)
    print(Style.BRIGHT + Fore.MAGENTA + '[State] ' + item + Style.RESET_ALL)


def commandInfo(item):
    '''
    Bright blue output for movement information
    '''
    item = str(item)
    print(Style.BRIGHT + Fore.BLUE + '[Command] ' + item + Style.RESET_ALL)


def detectedInfo(item):
    '''
    Bright yellow output for detected object information
    '''
    item = str(item)
    print(Style.BRIGHT + Fore.YELLOW + '[Detected] ' + item + Style.RESET_ALL)


def clock():
    '''
    return now time in format of hour:minute:second
    '''
    return 'time: ' + datetime.utcnow().strftime('%H:%M:%S.%f')
