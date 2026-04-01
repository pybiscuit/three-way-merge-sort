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
"""

import math
from typing import Dict

def hashing_params() -> Dict: 
    """
    returns calculated paramters (a, b) for the universal family of hash functions.

    :return: A tuple representing the the multiplier and offset for the hashing algorithm.
    """


    parm_dict = {}
    return parm_dict

def hash_function(parm_dict: Dict, key: int):
    """
    Universal family of hash functions based on number theory for random hashing. Ideal
    candidate for uniform indepenent mapping (maps Z_p to Z_m). 
    Set - H_pm = {h_ab : a E Z_p* and b E Z_p}

    :param parm_dict: The dictionary containing paramters for the hash function, includes multiplier
                      offset, optimal family size, prime number, and hash table size.
    :param key: Integer value of the hexadecimal hash of the password retreived from HIBP.
    
    """
