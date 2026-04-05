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

# Iterative bottom-up 3-way merge sort

def merge_sort_3way(arr):
    n = len(arr)
    if n <= 1:
        return arr

    # Start with chunks of size 1, triple the chunk size each pass
    chunks = [[x] for x in arr]

    while len(chunks) > 1:
        merged = []
        i = 0
        while i < len(chunks):
            if i + 2 < len(chunks):
                merged.append(merge3(chunks[i], chunks[i+1], chunks[i+2]))
                i += 3
            elif i + 1 < len(chunks):
                merged.append(merge2(chunks[i], chunks[i+1]))
                i += 2
            else:
                merged.append(chunks[i])
                i += 1
        chunks = merged

    return chunks[0]

# Data generators 

def gen_int(n):
    return [random.randint(2**20, 2**30) for _ in range(n)]

def gen_float(n):
    return [random.uniform(0.0, 1.0) for _ in range(n)]

# Benchmarking 

def benchmark(sizes, generator):
    times = []
    for n in sizes:
        exp = n.bit_length() - 1
        data = generator(n) # exclude I/O time

        t0 = time.perf_counter()
        merge_sort_3way(data)
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

# Main 

def main():
    sizes = [2**e for e in range(20, 30)]

    print("Benchmarking with integers …")
    int_times = benchmark(sizes, gen_int)

    print("\nBenchmarking with floats …")
    float_times = benchmark(sizes, gen_float)

    plot_results(sizes, int_times, float_times)

if __name__ == "__main__":
    main()