"""
Three Way Merge Sort

Course:  CS361
Section: 001
Authors: 
    Robert Vanderburg
    Kiana Tarter
    Neveah Martinez
Project: 
    Performance Analysis of 3-Way Merge Sort and Bloom
    Filter-Based Breach Detection at Scale
Filename: hibp_utils.py
Description: Provides functionality for loading HIBP password data into two unified
files for processing - traning.txt and holdout.txt
"""

import os
from typing import List

BASE_DIRECTORY = "/media/darkbiscuit/AltQ/Pwndpasswords"

def load_passwords(prefix: str) -> List:
    dir = BASE_DIRECTORY + "/" + prefix
    with open(dir, "r") as r:
        pw_data = r.readlines()

    pw_data = [prefix + pw_data[i][0:35] for i in range(len(pw_data))]

    return pw_data

def write_password(pw_data: List) -> None: 
    with open("training.txt", "a") as f:
        for pw in pw_data:
            f.write(pw + "\n")

def get_prefixes() -> List:
    prefixes = os.listdir(BASE_DIRECTORY)
    return prefixes

if __name__ == "__main__":
    print("[+] HIBP utilities have been loaded direcly.")