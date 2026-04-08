#!/usr/bin/env python3

"""The generator file is going to generate a password based on the user's expression"""

import json
import os
import string
from random import *

import pyperclip
from rich.console import Console

from functions import clear
from vocabulary import *


# reads file
def readDB():
    # if the file doesn't exist, create it with an empty dictionary
    if not os.path.exists("db.json"):
        with open("db.json", "w", encoding="utf-8") as f:
            json.dump({}, f)

    with open("db.json", "r", encoding="utf-8") as f:
        return json.load(f)


# uploads data
def uploadDB(data):
    with open("db.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


class Generator:
    def __init__(self):
        self.cls = Console()

    def generate_password(self):
        alphabet_upper = string.ascii_uppercase  # uppercase letters
        alphabet_lower = string.ascii_lowercase  # lowercase letters
        nums = "1234567890"  # figures
        symbols = "!?/,._-+*%$#&()[]<>~"  # symbols
        password = ""  # will be filled with random characters

        # generate random characters for the password
        for alpL in range(4):
            # choose a random lowercase letter
            ran_alp_low = choice(alphabet_lower)
            password += ran_alp_low

        for alpU in range(4):
            # choose a random uppercase letter
            ran_alp_up = choice(alphabet_upper)
            password += ran_alp_up

        for nms in range(4):
            # choose a random number
            ran_nums = choice(nums)
            password += ran_nums

        for symb in range(4):
            # choose a random symbol
            ran_symb = choice(symbols)
            password += ran_symb

        # shuffle the password characters
        pass_list = list(password)
        shuffle(pass_list)

        # join the shuffled characters into a string
        self.result = "".join(pass_list)

        return self.result

    def save_password(self):
        data = readDB()
        data[self.name] = self.result
        uploadDB(data)

    # ask the user if they want to save the password
    def ask_user(self):
        # print the generated password
        generated_password = self.result
        cls.print(OUTPUT_PASSWORD, generated_password)

        # ask the user if they want to save the password
        ask_save = self.cls.input(
            "[bold magenta]Save password? ([/][bold green]y[/]/[bold red]n[/][bold magenta]):[/] "
        )
        # if the user wants to save the password, ask for a name
        if ask_save.lower() == "y":
            set_name = self.cls.input(
                "[bold magenta]Enter a name for this password:[/] "
            )
            self.name = set_name
            # save the password to the database
            self.save_password()
            cls.print(f'[bold green]Password saved as "{self.name}"![/]')
            # copy the password to the clipboard
            pyperclip.copy(self.result)
            cls.print(COPIED)

        # if the user does not want to save the password, ask if they want to generate another
        elif ask_save.lower() == "n":
            ask_redo = self.cls.input(
                "[bold magenta]Generate another password? ([/][bold green]y[/]/[bold red]n[/][bold magenta]):[/] "
            )

            # if the user wants to generate another password, do so
            if ask_redo.lower() == "y":
                print()  # print a blank line for spacing
                self.generate_password()
                self.ask_user()

            # if the user does not want to generate another password, go back to the menu
            elif ask_redo.lower() == "n":
                clear()
                from main import Menu

                Menu().menu_page()
        else:
            # if the user wrote anything other than 'y' or 'n', show an error message and ask again
            print()
            cls.print(SAVE_ASK_ERROR)
            print()
            self.ask_user()
