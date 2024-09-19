# Helper libraries
import argparse
import sys
import random
import pytest

# Importing structures
from structures.map import Map

class TestMap():

    @pytest.fixture
    def map(self):
        return Map()



