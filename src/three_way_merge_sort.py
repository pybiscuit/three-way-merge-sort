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
Filename: three_way_merge_sort.py
"""

import random
import time
import csv
import sys

# 3-way merge sort

def merge_sort_3way(arr):
    if len(arr) <= 1:
        return arr

    n = len(arr)
    base = n // 3
    rem  = n % 3

    s1 = base
    s2 = base
    # remainder goes to the last chunk ( n = 7 -> 2, 2, 3)

    left   = merge_sort_3way(arr[:s1])
    middle = merge_sort_3way(arr[s1:s1 + s2])
    right  = merge_sort_3way(arr[s1 + s2:])

    return merge3(left, middle, right)


def merge3(a, b, c):
    result = []
    i = j = k = 0

    while i < len(a) and j < len(b) and k < len(c):
        if a[i] <= b[j] and a[i] <= c[k]:
            result.append(a[i]); i += 1
        elif b[j] <= a[i] and b[j] <= c[k]:
            result.append(b[j]); j += 1
        else:
            result.append(c[k]); k += 1

    remaining = merge2(a[i:], b[j:])      # -------------
    remaining = merge2(remaining, c[k:])  # ^ Double check
    result.extend(remaining)
    return result


def merge2(x, y):
    result = []
    i = j = 0
    while i < len(x) and j < len(y):
        if x[i] <= y[j]:
            result.append(x[i]); i += 1
        else:
            result.append(y[j]); j += 1
    result.extend(x[i:])
    result.extend(y[j:])
    return result

def gen_int(n):
    for i in range(n):
        return random.randint(2**20, 2**30)

def gen_float(n):
    for i in range(n):
        return random.uniform(32)



