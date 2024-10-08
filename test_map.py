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

    def test_given(self, map: Map):  # testing the given code
        random.seed(1337)
        print("==== Executing Map Tests ====")

        # Make some entries
        e1 = Entry(1, "value_for_key_1")
        e2 = Entry(10, "value_for_key_10")
        map.insert(e1)
        map.insert(e2)
        map.insert_kv(2, "Barry rules")
        assert map.insert(Entry(1, "value_for_key_10")) == "value_for_key_1"

        map[3] = "value_for_key_3"
        assert map.get_size() == 4

    # testing to see if functionality works while half-full
    def test_halfFull(self, map: Map):
        VAL = 26

        for i in range(VAL):
            map.insert(Entry(i, f"{i}"))

        assert map.get_size() == VAL
        assert map._capacity == 53

        # check that all the values exist within the map
        for i in range(VAL + 1):
            if i < VAL:
                assert map.find(i) == f"{i}"
            else:
                assert map.find(i) == None

        for i in range(VAL):
            pass

    # testing to see if rehashing works
    def test_rehash(self, map: Map):
        for i in range(60):
            map.insert(Entry(i, "a"))

        assert map.get_size() == 60
        assert map._capacity == 97
        
    
