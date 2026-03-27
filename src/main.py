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
Filename: Main.java

Description:
Implements a three way meger sort. Progressively larger inputs are divided 
into 3, roughly equal, lists and then a merge sort is applied, timed, and analyzed.
"""

import time

@timed
def merge(input_list): ...

def read_input(directory): ...

def generate_list(): ...

def timed(func):
    def wrapped(n):
        start = time.time()
        result = func(n)
        end = time.time()
        return end - start
    return wrapped

if __name__ == "__main__":
    print("[+] Sorter loaded.")