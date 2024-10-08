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
        
    def test_insert_and_find(self, map: Map):
        entry = Entry("key1", "value1")
        map.insert(entry)
        assert map.find("key1") == "value1"

    def test_insert_kv_and_find(self, map: Map):
        map.insert_kv("key2", "value2")
        assert map.find("key2") == "value2"

    def test_insert_and_update(self, map: Map):
        entry1 = Entry("key3", "value3")
        entry2 = Entry("key3", "value3_updated")
        map.insert(entry1)
        old_value = map.insert(entry2)
        assert old_value == "value3"
        assert map.find("key3") == "value3_updated"

    # @pytest.mark.skip("inf loop smth going on")
    def test_remove(self, map: Map):
        print("pp")
        map.insert_kv("key4", "value4")
        map.remove("key4")
        assert map.find("key4") is None

    def test_setitem(self, map: Map):
        map["key5"] = "value5"
        assert map.find("key5") == "value5"

    def test_rehash_2(self, map: Map):
        for i in range(100):
            map.insert_kv(f"key{i}", f"value{i}")
        assert map._capacity > 53  # Initial capacity is 53, should be rehashed to a larger size

    def test_find_nonexistent_key(self, map: Map):
        assert map.find("nonexistent_key") is None

    # @pytest.mark.skip("ditto remove test reason")
    def test_insert_and_remove_multiple(self, map: Map):
        map.insert_kv("key6", "value6")
        map.insert_kv("key7", "value7")
        map.remove("key6")
        assert map.find("key6") is None
        assert map.find("key7") == "value7"
