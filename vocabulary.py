#!/usr/bin/env python3

"""The vocabulary file is going to keep here
all the words and phrases
for different things"""

from rich.console import Console

cls = Console()

TITLES: list = ["Password Generator", "Generation", "Helper"]

MENU: dict = {
    "[bold cyan](1)[/bold cyan]": "[bold cyan] - Generate a password[/bold cyan]",
    "[bold cyan](2)[/bold cyan]": "[bold cyan] - View list of passwords[/bold cyan]",
    "[bold red](3)[/bold red]": "[bold red] - Exit[/bold red]",
}

INVITATIONS: list = [
    "[bold italic red]\n$ [/]",
]

ENDING: str = "[bold italic red]\nPress ENTER to continue...[/]"  # if it is the end of the program
OPTION_ERROR: str = "[bold red]Error! Choose 1, 2 or 3 option![/]"  # if a user wrote anything other than 1 or 2
OUTPUT_PASSWORD: str = "[bold green]Generated password: [/]"
COPIED: str = "[bold green]Copied to clipboard![/]"
