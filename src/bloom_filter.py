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
Filename: bloom_filter.py
Description: Bloom Filter class containing methods for creating, inserting, and querying a bloom filter
for password hashes. Supported by methods in Hashing.py.
"""
import math
from typing import Tuple, Boolean, List, Bytearray
from hashing import Hashing

HASH_SEED = 0xCAFEBABE_DEAD10CC

class BloomFilter:
    def __init__(self):
        self.filter = self.init_filter()
        self.params = Hashing.make_params(7, 2**160+13, HASH_SEED)


    def find_index(bit_index):
        byte_index = bit_index // 8
        bit_offset = bit_index % 8

        # python stores rightmost bit as position 0
        bit_val = 1 << bit_offset
        return (byte_index, bit_val)
    

    def insert(self, hex_password: str) -> None:
        # convert password from hex -> int
        # run hashing on the int and flip the 0 bits at the specified locs
        int_pass = int(password, 16)

        m = len(self.filter) * 8
        p = 2**160 + 13

        for (a,b) in self.params:
            bit_index = Hashing.hash_function(int_pass, a, b, p, m)

            (byte_index, bit_val) = self.find_index(bit_index)

            self.filter[byte_index]= self.filter[byte_index] | bit_val

     
    def query(self, hashed_password: str) -> Boolean:
        # convert password from hex -> int
        # run hashing on the int and check the bits at the specified locs
        # return true if matchall else false.
        int_pass = int(hashed_password, 16)

        m = len(self.filter) * 8
        p = 2**160 + 13

        for (a,b) in self.params:
            bit_index = Hashing.hash_function(int_pass, a, b, p, m)

            (byte_index, bit_val) = self.find_index(bit_index)

            if (self.filter[byte_index] & bit_val) == 0:
                # break loop if found 0
                return False
                
        return True
    

    @timed
    def build(self) -> None: 
        """
        Builds the bloom filter by opening the training data text file and looping over all hashed 
        passwords and inserting them into the Byte array by callling insert().
        """
        passwords = self.read_training_data()
        for hex in passwords:
            self.insert(hex)

    def read_training_data(self) -> List:
        """
        Opens training data text file and returns stripped array (List) of the values.

        :return: List of hashed passwords.
        """
        with open("training.txt", "r") as r:
            training_data = r.read().splitlines()

        return training_data

    def read_holdout_data(self) -> List:
        """
        Opens holdout data text file and returns stripped array (List) of the values.

        :return: List of hashed passwords.
        """
        with open("holdout.txt", "r") as r:
            holdout_data = r.read().splitlines()

        return holdout_data

    def init_filter(self) -> Bytearray:
        """
        Create bytearray that represents the bloom filter. Values for m are hard coded at present.
        The byte array is created using the ceiling of (m/8).

        :return: bytearray for the bloom filter.
        """
        return bytearray(math.ceil(8_700_000/8))

    @timed
    def query_analysis(self) -> None: 
        holdout_data = self.read_holdout_data()

        for i in range(1000):
            print(self.query(holdout_data[i]))
        

    def timed(func):
        def wrapped(n):
            start = time.time()
            result = func(n)
            end = time.time()
            return end - start
        return wrapped

if __name__ == "__main__":
    print("[+] BloomFilter class loaded direcly.")