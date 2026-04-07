#!/usr/bin/env python3

"""Options file is going to display all the options that the program has: (solver, helper)"""

from rich.console import Console

from vocabulary import *

cls = Console()  # initialization rich.console


def title_options(options):  # displays all the options: Solver and Helper
    for key, value in options.items():
        cls.print(f"{key}{value}")


class Options:
    @staticmethod
    def title_display():  # displays options
        title_options(MENU)  # gets the options from the vocabulary.py
