# Helper libraries
import random 
import time
import pytest

# Importing structures
from structures.bloom_filter import BloomFilter

class TestBloomFilter():

    # @pytest.mark.skip("check")
    def test_setUp(self):
        bf = BloomFilter(10000)
        assert bf._bit == 98317
        assert bf._capacity == 98317
        assert bf._size == 0
        assert bf.is_empty() == True
        assert bf.get_capacity() == bf._capacity

    def test_insert1(self):
        bf = BloomFilter(10000)
        bf.insert("abcdefghijklmnopqrstuvwxyz")
        bf.insert("aaaaa")
        bf.insert(472)

        assert bf.contains(472)
        assert not bf.contains(473)
        assert bf.contains("abcdefghijklmnopqrstuvwxyz")
        assert not bf.contains("abcdefghijklmnopqrstuvwxy")
        assert bf._size == 3

    # def test_inserting(self):
    #     bf = BloomFilter(7654585)
        
