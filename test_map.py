# Helper libraries
import random
import pytest

# Importing structures
from structures.map import Map as m
from structures.entry import Entry

class TestMap():

    @pytest.fixture
    def map(self):
        return m()

    def test_given(self, map):
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


