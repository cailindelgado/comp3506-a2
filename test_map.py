# Helper libraries
import argparse
import sys
import random

# Importing structures
from structures.map import Map
from structures.entry import Entry

class TestMap():

    @pytest.fixture
    def map(self):
        return Map()

    def test_given(self, map):
        random.seed(1337)
        print("==== Executing Map Tests ====")
        my_map = Map()

        # Make some entries
        e1 = Entry(1, "value_for_key_1")
        e2 = Entry(10, "value_for_key_10")
        my_map.insert(e1)
        my_map.insert(e2)
        my_map.insert_kv(2, "Barry rules")
        my_map[3] = "value_for_key_3"
        assert my_map.get_size() == 4


