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
"""
import math
from hashing import Hashing

HASH_SEED = 0xCAFEBABE_DEAD10CC

class BloomFilter:
    def __init__(self):
        self.filter = self.init_filter()
        self.params = Hashing.make_params(7, 2**160+13, HASH_SEED)

    def insert(self, password): 
        # convert password from hex -> int
        # run hashing on the int and flip the 0 bits at the specified locs
        int_pass = int(password, 16)



        
        
    def query(self): ...
        # convert password from hex -> int
        # run hashing on the int and check the bits at the specified locs
        # return true if matchall else false.

    
    
    def find_index(bit_index):
        byte_index = bit_index // 8
        bit_offset = bit_index % 8

        # python stores rightmost bit as position 0
        bit_val = 1 << bit_offset
        return (byte_index, bit_val)

    @timed
    def build(self): ...
        # open training file
        # for each pw:
        # convert to integer k_int
        # run k_int through hash 7 times
        # flip the bit at each index returned

    def read_training(self): ...
        # read password from training.txt

    def read_holdout(self): ...
        # read passwords from holdout.txt

    def init_filter(self):
        return bytearray(math.ceil(8_700_000/8))

    @timed
    def query_analysis(self): ...
        # loop over 1000 passwords querying them.
        

    def timed(func):
        def wrapped(n):
            start = time.time()
            result = func(n)
            end = time.time()
            return end - start
        return wrapped

if __name__ == "__main__":
    print("[+] BloomFilter class loaded direcly.")