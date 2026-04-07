#!/usr/bin/env python3

"""List page for PwGen."""

import json
import os

from pyfiglet import Figlet
from rich.console import Console

from vocabulary import *

cls = Console()
fgl = Figlet(font="slant", justify="center")


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


class ListPage:
    def __init__(self) -> None:
        self.last_value = 0

    def output_list(self):
        data = readDB()
        # clear the screen and print the list of entries
        if not data:
            # if no entries are found, print a message and return
            cls.print("[bold red]No entries found.[/]")
            self.last_value = 0  # initialize last_value to 0
            self.keys_by_id = {}  # initialize keys_by_id as an empty dictionary
            return

        # map each key to its corresponding index and store it in keys_by_id
        self.keys_by_id = {i: k for i, k in enumerate(data.keys(), 1)}
        # print each entry in the list
        for i, k in self.keys_by_id.items():
            cls.print(f"[bold cyan]({i}) - {k}:[/] [yellow]{data[k]}[/]")
        self.last_value = len(self.keys_by_id)  # store the number of entries

    def ask_action(self):
        print()
        # print the available actions
        for key, value in ACTIONS.items():
            cls.print(key, value)
        # ask the user for an action and validate it
        ask_action = cls.input(
            "\n[bold cyan]Type action ([/][bold magenta]g[/]/[bold yellow]e[/]/[bold red]d[/]/[bold blue]q[/][bold cyan]):[/] "
        )

        # validate the action and return it
        if ask_action not in ACTIONS_FOR_TYPE:
            os.system("clear")
            from functions import Functions

            # show the list page again and ask for a valid action
            func_obj = Functions()
            func_obj.open_list()
            cls.print("[bold red]Invalid action.[/]")
            return ListPage.ask_action(self)

        elif ask_action == "g":
            from functions import Functions

            from .generator import Generator

            # open the generator page and generate a password
            func_obj = Functions()
            pwgen_obj = Generator()

            # generate the password and ask the user to save it
            func_obj.open_generator()
            pwgen_obj.generate_password()
            pwgen_obj.ask_user()
        elif ask_action == "e":
            pass
        elif ask_action == "d":
            data = readDB()
            # ask the user which entry to delete
            ask_which = cls.input(
                "[bold yellow]Which entry to delete? Type the number: [/]"
            )
            # validate the user's input and delete the corresponding entry
            if (
                ask_which.isdigit()
                and ask_which != "0"
                and int(ask_which) in range(1, self.last_value + 1)
            ):
                # get the key to delete and remove it from the data dictionary
                idx = int(ask_which)
                key_to_delete = self.keys_by_id.get(idx)
                # remove the key from the data dictionary and update the keys_by_id dictionary
                if key_to_delete is None:
                    cls.print("[bold red]Invalid index.[/]")
                    return self.ask_action()
                data.pop(key_to_delete, None)
                uploadDB(data)
                os.system("clear")
                self.output_list()  # refresh the list after deletion
                return self.ask_action()  # ask the user for an action after deletion
        elif ask_action == "q":
            os.system("clear")
            from main import Menu

            # show the menu page again
            Menu().menu_page()
