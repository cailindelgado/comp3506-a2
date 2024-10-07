# Helper libraries
import random
import pytest

# Importing structures
from structures.map import Map
from structures.entry import Entry

class TestMap():

    @pytest.fixture
    def map(self):
        return Map()

    # @pytest.mark.skip("check")
    def test_setUp(self, map: Map):
        assert map.SENTINAL == -1
        assert map._resize_idx == 0
        assert map._capacity == 53
        assert map._table == [None] * 53
        assert map._size == 0
        assert map._loadf == 0

    def test_index_yoinking(self, map: Map):
        e1 = Entry(1, "a")
        e2 = Entry(2, "a")
        e3 = Entry(3, "a")
        e4 = Entry(4, "a")
        e5 = Entry(5, "a")
        e6 = Entry(6, "a")

        map.insert(e1)
        assert map.insert(Entry(1, "B")) == "a"

        map.insert(e2)
        map.insert(e3)
        map.insert(e4)
        map.insert(e5)
        map.insert(e6)
        assert map.get_size() == 6
        assert map.find(5)

    def test_given(self, map: Map):
        random.seed(1337)
        print("==== Executing Map Tests ====")

        # Make some entries
        e1 = Entry(1, "value_for_key_1")
        e2 = Entry(10, "value_for_key_10")
        map.insert(e1)
        map.insert(e2)
        map.insert_kv(2, "Barry rules")
        map[3] = "value_for_key_3"
        assert map.get_size() == 4

    def test_halfFull(self, map: Map):
        pass

    def test_rehash(self, map: Map):
        for i in range(60):
            map.insert(Entry(i, "a"))

        assert map.get_size() == 60
        assert map._capacity == 97
        
    
