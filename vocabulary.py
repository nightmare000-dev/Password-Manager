#!/usr/bin/env python3

"""The vocabulary file is going to keep here
all the words and phrases
for different things"""

from rich.console import Console

cls = Console()

TITLES: list = ["Password Manager", "Generation", "Helper", "View List"]

MENU: dict = {
    "[bold cyan](1)[/bold cyan]": "[bold cyan] - Generate a password[/bold cyan]",
    "[bold cyan](2)[/bold cyan]": "[bold cyan] - View list of passwords[/bold cyan]",
    "[bold cyan](3)[/bold cyan]": "[bold cyan] - Help[/bold cyan]",
    "[bold red](4)[/bold red]": "[bold red] - Exit[/bold red]",
}

INVITATIONS: list = [
    "[bold italic red]\n$ [/]",
]

ENDING: str = "[bold italic red]\nPress ENTER to continue...[/]"  # if it is the end of the program
OPTION_ERROR: str = "[bold red]Error! Choose 1, 2, 3 or 4 option![/]"  # if a user wrote anything other than 1, 2, 3 or 4
OUTPUT_PASSWORD: str = "[bold green]Generated password: [/]"
COPIED: str = "[bold green]Copied to clipboard![/]"
SAVE_ASK_ERROR: str = "[bold red]Error! Choose 'y' or 'n' option![/]"  # if a user wrote anything other than 'y' or 'n'
ACTIONS: dict = {
    "[bold cyan](g)[/bold cyan]": "[bold cyan] - Generate password[/bold cyan]",
    "[bold cyan](e)[/bold cyan]": "[bold cyan] - Edit password[/bold cyan]",
    "[bold cyan](c)[/bold cyan]": "[bold cyan] - Copy password[/bold cyan]",
    "[bold cyan](d)[/bold cyan]": "[bold cyan] - Delete password[/bold cyan]",
    "[bold cyan](q)[/bold cyan]": "[bold cyan] - Quit[/bold cyan]",
}

ACTIONS_FOR_TYPE: list = ["g", "e", "c", "d", "q"]
