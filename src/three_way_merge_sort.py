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
import matplotlib.pyplot as plt

# Core merge helpers

CHUNK_THRESHOLD = 64


def merge(arr, left, mid1, mid2, right):
    """
    Merges three sorted lists based on index.
    """
    # Temporary arrays for three parts
    left_arr  = arr[left:mid1 + 1]
    mid_arr   = arr[mid1 + 1:mid2 + 1]
    right_arr = arr[mid2 + 1:right + 1]

    left_index  = len(left_arr)
    mid_index   = len(mid_arr)
    right_index = len(right_arr)

    i = j = k = 0
    index = left

    # Direct comparisons — no min_value scan, no redundant bounds checks
    while i < left_index and j < mid_index and k < right_index:
        if left_arr[i] <= mid_arr[j] and left_arr[i] <= right_arr[k]:
            arr[index] = left_arr[i]; i += 1
        elif mid_arr[j] <= left_arr[i] and mid_arr[j] <= right_arr[k]:
            arr[index] = mid_arr[j]; j += 1
        else:
            arr[index] = right_arr[k]; k += 1
        index += 1

    # Drain remaining elements
    while i < left_index:
        arr[index] = left_arr[i]; i += 1; index += 1
    while j < mid_index:
        arr[index] = mid_arr[j]; j += 1; index += 1
    while k < right_index:
        arr[index] = right_arr[k]; k += 1; index += 1

def three_way_merge_sort(arr, left, right):
    """
    Merge sort algorithm implementation. runs in O(nlgn).

    Introduction to Algorithms 4E - Cormen, Leiserson, Rivest, and Stein
    Sections: 2.3

    https://www.geeksforgeeks.org/dsa/3-way-merge-sort/

    :param arr: the array of elements to be sorted.
    :param left: index of the left most element.
    :param right: index of the right most element.
    """
    
    # If the list only has a single element return
    if right - left < CHUNK_THRESHOLD:
        arr[left:right+1] = sorted(arr[left:right+1])
        return
    
    # Find the two midpoints for a 3-way split
    mid1 = left + (right - left) // 3
    mid2 = left + 2 * (right - left) // 3
    
    # Recursively sort the sub arrays.
    three_way_merge_sort(arr, left, mid1)
    three_way_merge_sort(arr, mid1 + 1, mid2)
    three_way_merge_sort(arr, mid2 + 1, right)
    
    # Merge the the sub arrays.
    merge(arr, left, mid1, mid2, right)

def gen_int(n):
    """
    Generate a random array of intergers [0, n).

    :param n: number of intergers to create.
    """
    return [random.randint(1, 2**20) for _ in range(n)]

def gen_float(n):
    """
    Generate a random array of floats [0.0, 1.0).
    
    :param n: number of floats to create.
    """
    return [random.uniform(0.0, 1.0) for _ in range(n)]

def benchmark(sizes, generator):
    """
    Provide performance benchmarking for three_way_merge_sort algorithm.

    :param size: List of intergers represting the size of arrays to best benchmarked.
    :param generator: generator function for creating arrays.
    """
    times = []
    for n in sizes:
        exp = n.bit_length() - 1
        data = generator(n) # exclude I/O time

        t0 = time.perf_counter()
        three_way_merge_sort(data, 0, len(data) - 1)
        t1 = time.perf_counter()

        elapsed = t1 - t0
        times.append(elapsed)
        print(f"  n=2^{exp:2d} ({n:>12,})  {elapsed:.4f}s")
    return times

# Plotting

def plot_results(sizes, int_times, float_times):
    exponents = [n.bit_length() - 1 for n in sizes]
    labels    = [f"2^{e}" for e in exponents]

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Left: absolute runtime
    ax = axes[0]
    ax.plot(exponents, int_times,   marker='o', color='steelblue',
            label='int',   linewidth=2)
    ax.plot(exponents, float_times, marker='s', color='darkorange',
            label='float', linewidth=2, linestyle='--')
    ax.set_xticks(exponents)
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.set_xlabel("Input size (n)")
    ax.set_ylabel("Time (seconds)")
    ax.set_title("3-Way Merge Sort: Runtime vs Input Size")
    ax.legend()
    ax.grid(True, alpha=0.4)

    # Right: float/int ratio
    ax2 = axes[1]
    ratio = [f / i if i > 0 else 0 for f, i in zip(float_times, int_times)]
    ax2.bar(exponents, ratio, color='mediumpurple', alpha=0.8)
    ax2.axhline(1.0, color='black', linestyle='--', linewidth=1,
                label='ratio = 1 (equal speed)')
    ax2.set_xticks(exponents)
    ax2.set_xticklabels(labels, rotation=45, ha='right')
    ax2.set_xlabel("Input size (n)")
    ax2.set_ylabel("float time / int time")
    ax2.set_title("Float vs Int Runtime Ratio")
    ax2.legend()
    ax2.grid(True, axis='y', alpha=0.4)

    plt.tight_layout()
    plt.savefig("benchmark_plot.png", dpi=150)
    print("\nPlot saved to benchmark_plot.png")
    plt.show()

def main():
    sizes = [2**e for e in range(20, 30)]

    print("Benchmarking with integers …")
    int_times = benchmark(sizes, gen_int)

    print("\nBenchmarking with floats …")
    float_times = benchmark(sizes, gen_float)

    plot_results(sizes, int_times, float_times)

if __name__ == "__main__":
    main()
