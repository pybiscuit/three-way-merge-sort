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
    # remainder goes to the last chunk  (e.g. n=7 → 2, 2, 3)

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

    remaining = merge2(a[i:], b[j:])
    remaining = merge2(remaining, c[k:])
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
    return [random.randint(-(2**31), 2**31 - 1) for _ in range(n)]

def gen_float(n):
    return [random.uniform(-1e9, 1e9) for _ in range(n)]


def check_correctness():
    for _ in range(200):
        n   = random.randint(0, 300)
        arr = gen_int(n)
        assert merge_sort_3way(arr) == sorted(arr), "Correctness check FAILED"
    print("Correctness check passed (200 random trials)\n")

