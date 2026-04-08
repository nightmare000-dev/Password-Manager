#!/usr/bin/env python3

"""The helper file is going to display to user all the rules for inputting user's expression"""

from rich.console import Console

from vocabulary import *

cls = Console()


class Helper:
    def output_help(self):
        cls.print(f"[bold cyan]{HELPER}[/]")
