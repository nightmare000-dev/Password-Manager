#!/usr/bin/env python3

"""This is a file for all the functions"""

import os

from pyfiglet import Figlet

from vocabulary import *

fgl = Figlet(font="slant", justify="center")  # initialization Figlet


def clear():
    os.system("cls" if os.name == "nt" else "clear")


class Functions:
    @staticmethod
    def open_generator():  # directs to the Generator page and clears terminal
        clear()
        print(fgl.renderText(TITLES[1]))

    @staticmethod
    def open_list():  # directs to the List page and clears terminal
        clear()
        print(fgl.renderText(TITLES[3]))

    @staticmethod
    def open_helper():  # directs to the Helper page and clears terminal
        clear()
        print(fgl.renderText(TITLES[2]))
