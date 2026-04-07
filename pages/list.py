#!/usr/bin/env python3

"""List page for PwGen."""

import json
import os

from pyfiglet import Figlet
from rich.console import Console

from vocabulary import *

cls = Console()
fgl = Figlet(font="slant")


# reads file
def readDB():

    with open("db.json", "r", encoding="utf-8") as f:
        return json.load(f)


# uploads data
def uploadDB(data):
    with open("db.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


class ListPage:
    @staticmethod
    def output_list():
        # if the database is empty, show an error message and return
        if len(readDB()) == 0:
            cls.print("[bold red]No entries found.[/]")
            return

        # if the database is not empty, show the list of entries
        data = readDB()
        iteration = 1
        # iterate through the entries and print them
        for key, value in data.items():
            cls.print(f"[bold cyan]({iteration}) - {key}:[/] [yellow]{value}[/]")
            iteration += 1

        # ask the user for an action and validate it

    @staticmethod
    def ask_action():
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
            return ListPage.ask_action()
