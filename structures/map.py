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
    SENTINAL = -1  # for when doing quadratic probing

    def __init__(self) -> None:
        """
        Construct the map.
        You are free to make any changes you find suitable in this function
        to initialise your map.
        """
        # resizing primes
        self._resizing = [53, 97, 193, 389, 769, 1543, 3079, 6151, 12289, 24593, 49157, 98317, 
                          196613, 393241, 786433, 1572869, 3145739, 6291469, 12582917, 25165843, 
                          50331653, 100663319, 201326611, 402653189, 805306457, 1610612741, 
                          4294967311]  

        # 5 primes > 2^32
        self._p_list = [4294967311, 4294967357, 4294967371, 4294967377, 4294967387]  

        # index to resize too
        self._resize_idx = 0
        self._capacity = self._resizing[self._resize_idx]
        self._a = randrange(1, self._p_list[self._resize_idx])  # a in [1, prime]
        self._b = randrange(self._p_list[self._resize_idx])  # b in [0, prime]
        self._table = [None] * self._capacity
        self._size = 0
        self._loadf = 0.0
        self._active_size = 0

    def _get_index(self, entry: Entry) -> int:
        """
        Gets the index in the hashmap array for a given entry key
        """
        hash_key = entry.get_hash()
        N = self._capacity
        prime = self._p_list[self._resize_idx % 5]

        return ((self._a * hash_key + self._b) % prime) % N

    def _rehash(self):
        """
        when self._loadf gets large enough it becomes time to 
        rehash the table to maintain optminal functionality
        """
        self._resize_idx += 1
        old_cap = self._capacity

        if self._resize_idx >= 26:
            self._capacity = self._resizing[26]
        else:
            self._capacity = self._resizing[self._resize_idx]

        # rehash the table
        newT = [None] * self._capacity
        for idx in range(old_cap):
            elem = self._table[idx]
            if isinstance(elem, Entry):
                newT[self._get_index(elem)] = elem

        self._table = newT
        self._loadf = self._size / self._capacity

        # recalculate the a and b values for hashing
        self._a = randrange(1, self._p_list[self._resize_idx % 5])  # a in [1, prime]
        self._b = randrange(self._p_list[self._resize_idx % 5])  # b in [0, prime]

    def insert(self, entry: Entry) -> Any | None:
        """
        Associate value v with key k for efficient lookups. If k already exists
        in your map, you must return the old value associated with k. Return
        None otherwise. (We will not use None as a key or a value in our tests).
        Time complexity for full marks: O(1*)
        """
        if self._loadf >  0.8:
            self._rehash()

        idx = -1
        probe_idx = self._get_index(entry)
        counter = 1
        N = self._capacity

        while counter != N:
            elem = self._table[probe_idx]

            if elem is None or elem.get_key() == entry.get_key(): 
                idx = probe_idx
                break
            else:
                probe_idx = (probe_idx + (counter ** 2)) % N
                counter += 1

        if idx == -1:
            return None

        if self._table[idx] is None:
            self._table[idx] = entry
            self._size += 1
            self._active_size += 1
            self._loadf = self._size / self._capacity
            return None

        # if index, then update val and return old val
        if isinstance(self._table[idx], Entry):
            out_val = self._table[idx].get_value()
            self._table[idx].update_value(entry.get_value())
            return out_val

    def insert_kv(self, key: Any, value: Any) -> Any | None:
        """
        A version of insert which takes a key and value explicitly.
        Handy if you wish to provide keys and values directly to the insert
        function. It will return the value returned by insert, so keep this
        in mind. You can modify this if you want, as long as it behaves.
        Time complexity for full marks: O(1*)
        """
        entry = Entry(key, value)
        return self.insert(entry)

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
        idx = -1
        probe_idx = self._get_index(Entry(key, None))
        counter = 1
        N = self._capacity

        while counter != N:
            elem = self._table[probe_idx]

            if elem is None:
                break
            elif elem.get_key() == key:
                idx = probe_idx
                break
            else:
                probe_idx = (probe_idx + (counter ** 2)) % N
                counter += 1

        if idx == -1:
            return None

        #idx is not none, so key exists in ADT
        self._table[idx] = self.SENTINAL
        self._active_size -= 1

    def find(self, key: Any) -> Any | None:
        """
        Find and return the value v corresponding to key k if it
        exists; return None otherwise.
        Time complexity for full marks: O(1*)
        """
        # doing the most quadratic of probing 
        probe_idx = self._get_index(Entry(key, value=None))
        counter = 1
        N = self._capacity

        while counter != N:
            elem = self._table[probe_idx]

            if elem is None: 
                return None
            elif isinstance(elem, Entry) and elem.get_key() == key:
                return elem.get_value()
            else:  # goes here if sentinal or diff elem found
                probe_idx = (probe_idx + (counter ** 2)) % N
                counter += 1

        return None

    def __getitem__(self, key: Any) -> Any | None:
        """
        For convenience, you may wish to use this as an alternative
        for find()
        Time complexity for full marks: O(1*)
        """
        return self.find(key)

    def get_size(self) -> int:
        """
        Time complexity for full marks: O(1)
        """
        return self._active_size

    def is_empty(self) -> bool:
        """
        Time complexity for full marks: O(1)
        """
        return self._size == 0
