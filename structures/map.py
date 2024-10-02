"""
Skeleton for COMP3506/7505 A2, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov

Please read the following carefully. This file is used to implement a Map
class which supports efficient insertions, accesses, and deletions of
elements.

There is an Entry type defined in entry.py which *must* be used in your
map interface. The Entry is a very simple class that stores keys and values.
The special reason we make you use Entry types is because Entry extends the
Hashable class in util.py - by extending Hashable, you must implement
and use the `get_hash()` method inside Entry if you wish to use hashing to
implement your map. We *will* be assuming Entry types are used in your Map
implementation.
Note that if you opt to not use hashing, then you can simply override the
get_hash function to return -1 for example.
"""

from random import randrange
from typing import Any
from structures.entry import Entry

class Map:
    """
    An implementation of the Map ADT.
    The provided methods consume keys and values via the Entry type.
    """

    def __init__(self) -> None:
        """
        Construct the map.
        You are free to make any changes you find suitable in this function
        to initialise your map.
        """
        self._sentinal = Entry(None, None)  # for when doing quadratic probing

        self._resizing = [53, 97, 193, 389, 769, 1543, 3079, 6151, 12289, 24593, 49157, 
                          98317, 196613, 393241, 786433, 1572869, 3145739, 6291469, 12582917, 
                          25165843, 50331653, 100663319, 201326611, 402653189, 805306457, 
                          1610612741, 4294967311]  # resizing primes

        # index to resize too
        self._resize_idx = 0
        self._capacity = self._resizing[self._resize_idx]

        # 5 primes > 2^32
        self._p_list = [4294967311, 4294967357, 4294967371, 4294967377, 4294967387]  

        self._a = randrange(1, self._p_list[self._resize_idx % 5])  # a in [1, prime]
        self._b = randrange(self._p_list[self._resize_idx % 5])  # b in [0, prime]

        self._table = [None] * self._capacity
        self._size = 0

    def _rehash(self):
        """
        when self._loadf gets large enough it becomes time to 
        rehash the table to maintain optminal functionality
        """
        self._resize_idx += 1

        if self._resize_idx > 25:
            self._resize_idx += 1
            
        # rehash the table
        self._capacity = self._resizing[self._resize_idx]


    def _get_index(self, entry: Entry) -> int:
        """
        Gets the place in the array from the given index
        """
        hash_key = entry.get_hash()
        N = self._capacity
        prime = self._p_list[self._resize_idx % 5]

        return ((self._a * hash_key + self._b) % prime) % N

    def insert(self, entry: Entry) -> Any | None:
        """
        Associate value v with key k for efficient lookups. If k already exists
        in your map, you must return the old value associated with k. Return
        None otherwise. (We will not use None as a key or a value in our tests).
        Time complexity for full marks: O(1*)
        """
        if self.find(entry.get_key()) is not None:
            return None

        key = entry.get_key()
        pass

    def insert_kv(self, key: Any, value: Any) -> Any | None:
        """
        A version of insert which takes a key and value explicitly.
        Handy if you wish to provide keys and values directly to the insert
        function. It will return the value returned by insert, so keep this
        in mind. You can modify this if you want, as long as it behaves.
        Time complexity for full marks: O(1*)
        """
        entry = Entry(key, value)
        self.insert(entry)

    def __setitem__(self, key: Any, value: Any) -> None:
        """
        For convenience, you may wish to use this as an alternative
        for insert as well. However, this version does _not_ return
        anything. Can be used like: my_map[some_key] = some_value
        Time complexity for full marks: O(1*)
        """
        self.insert_kv(key, value)

    def remove(self, key: Any) -> None:
        """
        Remove the key/value pair corresponding to key k from the
        data structure. Don't return anything.
        Time complexity for full marks: O(1*)
        """
        pass

    def find(self, key: Any) -> Any | None:
        """
        Find and return the value v corresponding to key k if it
        exists; return None otherwise.
        Time complexity for full marks: O(1*)
        """
        pass

    def __getitem__(self, key: Any) -> Any | None:
        """
        For convenience, you may wish to use this as an alternative
        for find()
        Time complexity for full marks: O(1*)
        """
        self.find(key)

    def get_size(self) -> int:
        """
        Time complexity for full marks: O(1)
        """
        return self._size

    def is_empty(self) -> bool:
        """
        Time complexity for full marks: O(1)
        """
        return self._size == 0
