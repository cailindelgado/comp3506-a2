# Helper libraries
import random
from random import randrange

import pytest

# Importing structures
from structures.pqueue import PriorityQueue
from structures.dynamic_array import DynamicArray
from structures.entry import Entry

class TestPriorityQueue():

    @pytest.fixture
    def priority_queue(self):
        return PriorityQueue()

    def test_init(self, priority_queue):
        assert priority_queue._arr.is_empty()
        assert priority_queue._max_priority == 0
        assert priority_queue.get_size() == 0
        assert priority_queue.is_empty()

    def test_insert(self, priority_queue):
        priority_queue.insert(28, 10)
        priority_queue.insert(91, 7)
        priority_queue.insert(42, 12)

        assert priority_queue.get_min_priority() == 28
        assert priority_queue.get_min_value() == 10

        priority_queue.insert(19, 6)
        priority_queue.insert(73, 15)
        priority_queue.insert(14, 17)

        assert priority_queue.get_min_priority() == 14
        assert priority_queue.get_min_value() == 17
        assert priority_queue.get_size() == 6

    def test_insert_fifo(self, priority_queue):
        priority_queue.insert_fifo(-1)
        priority_queue.insert_fifo(0)
        priority_queue.insert_fifo(2)
        priority_queue.insert_fifo(4)
        priority_queue.insert_fifo(5)
        priority_queue.insert_fifo(6)

        assert priority_queue.get_min_priority() == 0 
        assert priority_queue.get_min_value() == -1

    def test_remove_min(self, priority_queue):
        priority_queue.insert(4, 7)
        priority_queue.insert(9, 1)
        priority_queue.insert(2, 6)
        priority_queue.insert(5, 8)

        print(priority_queue.get_size())
        print(priority_queue)

        assert priority_queue.remove_min() == 6  # min is 2, 6
        assert priority_queue.remove_min() == 7  # min is 4, 7
        assert priority_queue.remove_min() == 8  # min is 5, 8
        assert priority_queue.remove_min() == 1  # min is 9, 1
        assert priority_queue.remove_min() is None

    # @pytest.mark.skip("womp womp")
    def test_ip_build(self, priority_queue):
        random.seed(20)
        VAL = 10
        da = DynamicArray()
        inserted = "["
        for i in range(VAL):
            x = randrange(VAL)
            da.append(Entry(x, x))
            inserted += f'{x}, '

        inserted = inserted[:-2] + "]"

        priority_queue.ip_build(da)
        print(inserted)
        print(priority_queue)

        assert priority_queue.remove_min() == 0

        # lst = priority_queue._arr
        # for i in range(VAL):
        #     l = 2*i + 1
        #     r = 2*i + 2
        #
        #     if l < VAL and r < VAL:
        #         assert lst[i] <= lst[l] and lst[i] <= lst[r]
        #     elif l < VAL <= r:
        #         assert lst[i] <= lst[l]
        #     elif l >= VAL > r:
        #         assert lst[i] <= lst[r]


    def test_heapSort(self, priority_queue: PriorityQueue):
        # random.seed(20)
        VAL = 20
        for i in range(VAL):
            x = randrange(VAL)
            priority_queue.insert_fifo(x)

        sorted = priority_queue.sort()
        print(sorted)
        # assert 1 == 2

        for i in range(sorted.get_size() - 1):
            assert sorted[i].get_value() > sorted[i + 1].get_value()