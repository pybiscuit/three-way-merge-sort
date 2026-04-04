BloomFilter

To run custom test cases, replace training.txt and holdout.txt in the src folder with the custom test cases. NOTE: the name of the files must remain "training.txt" and "holdout.txt".

Simple example:

from bloom_filter import BloomFilter

bloom = BloomFilter()
bloom.build()

bloom.query_analysis()

bloom.query(hexadecimal_password)
bloom.insert(hexadecimal_password)