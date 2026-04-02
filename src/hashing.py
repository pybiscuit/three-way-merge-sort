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
Filename: hasing.py
Description: Implements functionality for k paramter generation and hashing implementation.
"""

import math
from typing import List

class Hashing:
    def __init__(self): ...

    def convert_hex_int(hased_password: str) -> int: ...

    def make_params(k: int, p: int, seed: int) -> List: 
        """
        Deterministically generate k independent multiplier, offset (a,b) pairs using
        a seed.

        Uses LCG instead of random generator.
        https://en.wikipedia.org/wiki/Linear_congruential_generator

        Introduction to Algorithms 4E - Cormen, Leiserson, Rivest, and Stein
        Sections: 11.3.4, 31.3.X

        Constants come from Knuth AOCPVol2. for LCGs.

        :return: A list of tuples representing the k multiplier and offset combinations required by
            the hashing algorithm.
        """
        params = []
        state = seed

        for _ in range(k):
            state = (6364136223846793005 * state + 1442695040888963407) & 0xFFFFFFFFFFFFFFFF
            a = (state % (p - 1)) + 1

            state = (6364136223846793005 * state + 1442695040888963407) & 0xFFFFFFFFFFFFFFFF
            b = state % p

            params.append((a,b))
        
        return params

    def hash_function(k_int: int, a: int, b: int, p: int, m: int) -> int:
        """
        Hash function dervied form the universal family of hash functions based on number theory 
        for random hashing. It is an ideal candidate for uniform indepenent mapping. 
        
        H_pm = {h_ab : a E Z_p* and b E Z_p}

        Introduction to Algorithms 4E - Cormen, Leiserson, Rivest, and Stein
        Sections: 11.3.4, 31.3.X

        https://en.wikipedia.org/wiki/Universal_hashing

        :param k_int: The integer value of the hexadecimal (sha-1 hashed) password from HIBP.
        :param a: The modular arithmetic multiplier.
        :param b: The modular arithmetic offset.
        :param p: The universal hash function primer number.
        :param m: The size of the hash table (BloomFilter).
        """
        return ((a * k_int + b) % p) % m
