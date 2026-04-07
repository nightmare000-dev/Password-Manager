#!/usr/bin/env python3

"""List page for PwGen."""

import json

from pyfiglet import Figlet
from rich.console import Console

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
        if len(readDB()) == 0:
            cls.print("[bold red]No entries found.[/]")
            return
        data = readDB()
        iteration = 1
        for key, value in data.items():
            cls.print(f"[bold cyan]({iteration}) - {key}:[/] [yellow]{value}[/]")
            iteration += 1
