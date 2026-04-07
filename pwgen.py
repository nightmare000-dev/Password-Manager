#!/usr/bin/env python3

import json
import string
from random import *

from rich.console import Console

cls = Console()


# reads file
def readDB():

    with open("db.json", "r", encoding="utf-8") as f:
        return json.load(f)


# uploads data
def uploadDB(data):
    with open("db.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def pwgen():
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
    result = "".join(pass_list)

    return result
