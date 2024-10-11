"""
Skeleton for COMP3506/7505 A2, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any
from structures.bit_vector import BitVector
from structures.util import object_to_byte_array as oba
from math import log as ln
from random import randrange as rr

class BloomFilter:
    """
    A BloomFilter uses a BitVector as a container. To insert a given key, we
    hash the key using a series of h unique hash functions to set h bits.
    Looking up a given key follows the same logic, but only checks if all
    bits are set or not.

    Note that a BloomFilter is considered static. It is initialized with the
    number of total keys desired (as a parameter) and will not grow. You
    must decide what this means in terms of allocating your bitvector space
    accordingly.

    You can add functions if you need to.

    *** A NOTE ON KEYS ***
    We will only ever use int or str keys.
    We will not use `None` as a key.
    You might like to look at the `object_to_byte_array` function
    stored in util.py -- This function can be used to convert a string
    or integer key into a byte array, and then you can use the byte array
    to make your own hash function (bytes are just integers in the range
    [0-255] of course).
    """

    def __init__(self, max_keys: int) -> None:
        # use formula on ed discussion for number of bits: -max_keys * ln(0.01)/(ln(2)^2)
        self._bits = (-1 * max_keys * ln(0.01) / (ln(2)**2))  # make next largest prime
        self._bit_options = [97, 193, 389, 769, 1543, 3079, 6151, 12289, 24593, 49157, 98317,
                          196613, 393241, 786433, 1572869, 3145739, 6291469, 12582917, 25165843, 
                          50331653, 100663319, 201326611, 402653189, 805306457, 1610612741, 
                          4294967311]  
        for i in range(25):
            if self._bits > self._bit_options[i] and self._bits < self._bit_options[i + 1]:
                self._bit = self._bit_options[i + 1]

        # primes for the compression function
        self._primes = [4294967311, 4294967357, 4294967371, 4294967377, 4294967387, 4294967459]  
        #compression func 1
        self._a = rr(1, self._primes[0])  # a in [1, prime]
        self._b = rr(self._primes[0])  # b in [0, prime]

        # compression func 2
        self._c = rr(1, self._primes[1])
        self._d = rr(self._primes[1])

        # compression func 3
        self._e = rr(1, self._primes[2])
        self._f = rr(self._primes[2])

        # compression func 4
        self._g = rr(1, self._primes[3])
        self._h = rr(self._primes[3])

        # compression func 5
        self._i = rr(1, self._primes[4])
        self._j = rr(self._primes[4])

        # compression func 6
        self._k = rr(1, self._primes[5])
        self._l = rr(self._primes[5])

        # for cyclic shifting hash
        self._mask = (1 << 32) - 1

        # should have, and allocate it accordingly.
        self._data = BitVector()
        self._data.allocate(self._bit)
        
        # More variables here if you need, of course
        self._capacity = self._bit
        self._size = 0
    
    def __str__(self) -> str:
        """
        A helper that allows you to print a BloomFilter type
        via the str() method.
        This is not marked. <<<<
        """
        return "turtles"

    def insert(self, key: Any) -> None:
        """
        Insert a key into the Bloom filter.
        Time complexity for full marks: O(1)
        """
        # self._data.set_at(self.hash(key, 1))
        # self._data.set_at(self.hash(key, 2))
        hash1 = self._hash(key, 1)
        hash2 = self._hash(key, 2)
        self._data.set_at(self._compress(hash1, 0))
        self._data.set_at(self._compress(hash1, 1))
        # self._data.set_at(self._compress(hash1, 2))
        self._data.set_at(self._compress(hash2, 3))
        self._data.set_at(self._compress(hash2, 4))
        # self._data.set_at(self._compress(hash2, 5))

        self._size += 1

    def _hash(self, key: Any, hash_func: int) -> int:
        """
        hash function, takes in a key and convers it into a hashed
        and scrambeled output to be compressed to @self._size@
        then uses a compression function (MAD) to compress the 
        array down to an index to use
        """
        key = oba(key)
        hash = 0

        if hash_func == 1:
            for byte in key:
                hash = (hash << 5 & self._mask) | (hash >> 27)
                hash += byte

        elif hash_func == 2:
            for byte in key:
                hash = (hash << 9 & self._mask) | (hash >> 23)
                hash += byte

        return hash

    def _compress(self, hash: int, compression_func: int) -> int:
        """
        A bunch of compression functions to distribute the hash across the bloomfilter
        # do the MAD compression
        """
        N = self._capacity

        if compression_func == 0:
            prime = self._primes[0]
            return ((self._a * hash + self._b) % prime) % N

        elif compression_func == 1:
            prime = self._primes[1]
            return ((self._c * hash + self._d) % prime) % N
        
        elif compression_func == 2:
            prime = self._primes[2]
            return ((self._e * hash + self._f) % prime) % N

        elif compression_func == 3:
            prime = self._primes[3]
            return ((self._g * hash + self._h) % prime) % N

        elif compression_func == 4:
            prime = self._primes[4]
            return ((self._i * hash + self._j) % prime) % N
        else:
            prime = self._primes[5]
            return ((self._k * hash + self._l) % prime) % N

    def contains(self, key: Any) -> bool:
        """
        Returns True if all bits associated with the h unique hash functions
        over k are set. False otherwise.
        Time complexity for full marks: O(1)
        """
        # bloom filter if any not 1 then no
        hash1 = self._hash(key, 1)
        hash2 = self._hash(key, 2)
        set1 = self._data.get_at(self._compress(hash1, 0))
        set2 = self._data.get_at(self._compress(hash1, 1))
        # set3 = self._data.get_at(self._compress(hash1, 2))
        set4 = self._data.get_at(self._compress(hash2, 3))
        set5 = self._data.get_at(self._compress(hash2, 4))
        # set6 = self._data.get_at(self._compress(hash2, 5))

        # if set1 and set2 and set3 and set4 and set5 and set6:
        if set1 and set2 and set4 and set5:
            return True
        else:
            return False

    def __contains__(self, key: Any) -> bool:
        """
        Same as contains, but lets us do magic like:
        `if key in my_bloom_filter:`
        Time complexity for full marks: O(1)
        """
        return self.contains(key)

    def is_empty(self) -> bool:
        """
        Boolean helper to tell us if the structure is empty or not
        Time complexity for full marks: O(1)
        """
        return self._size == 0

    def get_capacity(self) -> int:
        """
        Return the total capacity (the number of bits) that the underlying
        BitVector can currently maintain.
        Time complexity for full marks: O(1)
        """
        return self._capacity
