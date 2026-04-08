#!/usr/bin/env python3

import os
import sys

from pyfiglet import Figlet
from rich.console import Console

from functions import Functions, clear
from options import Options
from pages.generator import Generator
from pages.helperPage import Helper
from pages.list import ListPage
from vocabulary import *

clear()

fgl = Figlet(font="slant", justify="center")  # initialization Figlet
cls = Console()  # initialization rich.console

opt_obj = Options()  # for options
func_obj = Functions()  # for functions
pwgen_obj = Generator()  # for generator
view_obj = ListPage()  # for list
helper_obj = Helper()  # for helper


class Menu:
    def menu_page(self):
        title_text = fgl.renderText(TITLES[0])
        print(title_text)  # displays title text

        opt_obj.title_display()  # displays options
        choose_option_inv = cls.input(INVITATIONS[0])  # invitation

        # checks if the user entered a valid option
        if choose_option_inv in ["1", "2", "3", "4"]:
            if choose_option_inv == "1":  # if the user entered 1, open the generator
                func_obj.open_generator()
                pwgen_obj.generate_password()
                pwgen_obj.ask_user()
            elif choose_option_inv == "2":  # if the user entered 2, open the list
                func_obj.open_list()
                view_obj.output_list()
                view_obj.ask_action()
            elif choose_option_inv == "3":  # if the user entered 3, open the helper
                func_obj.open_helper()
                helper_obj.output_help()
            elif choose_option_inv == "4":  # if the user entered 4, exit the program
                sys.exit()
            else:
                cls.print(OPTION_ERROR)  # if a user wrote anything other than 1, 2 or 3


# main loop
if __name__ == "__main__":
    while True:  # infinite loop
        # creates a new Menu object and displays the menu page
        menu_obj = Menu()
        menu_obj.menu_page()  # displays the menu page
        cls.input(ENDING)  # waits for the user to press ENTER to continue
        clear()  # clears the console
