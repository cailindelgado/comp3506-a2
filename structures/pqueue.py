"""
Skeleton for COMP3506/7505 A2, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any, List
from structures.entry import Entry
from structures.dynamic_array import DynamicArray

class PriorityQueue:
    """
    An implementation of the PriorityQueue ADT. We have used the implicit
    tree method: an array stores the data, and we use the heap shape property
    to directly index children/parents.

    The provided methods consume keys and values. Keys are called "priorities"
    and should be comparable numeric values; smaller numbers have higher
    priorities.
    Values are called "data" and store the payload data of interest.
    We use the Entry types to store (k, v) pairs.
    """
    
    def __init__(self):
        """
        Empty construction
        """
        self._arr = DynamicArray()  # insert O(n), removeMin/min O(1)
        self._max_priority = 0

    def __str__(self) -> str:
        # return str(self._arr)
        out = "[ "
        for i in range(self._arr.get_size()):
                if self._arr[i] is None:
                    break

                out += f" |{str(self._arr[i])}| "

        return out + "]"

    def _parent(self, ix: int) -> int:
        """
        Given index ix, return the index of the parent
        """
        if ix == 0:
            return ix

        return (ix - 1) // 2

    def insert(self, priority: int, data: Any) -> None:
        """
        Insert some data to the queue with a given priority.
        """
        new = Entry(priority, data)

        # Put it at the back of the heap
        self._arr.append(new)
        ix = self._arr.get_size() - 1

        # Now swap it upwards with its parent until heap order is restored
        while ix > 0 and self._arr[ix].get_key() < self._arr[self._parent(ix)].get_key():
            parent_ix = self._parent(ix)
            self._arr[ix], self._arr[parent_ix] = self._arr[parent_ix], self._arr[ix]
            ix = parent_ix

    def insert_fifo(self, data: Any) -> None:
        """
        Insert some data to the queue in FIFO mode. Note that a user
        should never mix `insert` and `insert_fifo` calls, and we assume
        that nobody is silly enough to do this (we do not test this).
        """
        self.insert(self._max_priority, data)
        self._max_priority += 1

    def get_min_priority(self) -> Any:
        """
        Return the priority of the min element
        """
        if self.is_empty():
            return None

        return self._arr[0].get_key()

    def get_min_value(self) -> Any:
        """
        Return the highest priority value from the queue, but do not remove it
        """
        if self.is_empty():
            return None

        return self._arr[0].get_value()

    def remove_min(self) -> Any:
        """
        Extract (remove) the highest priority value from the queue.
        You must then maintain the queue to ensure priority order.
        """
        if self.is_empty():
            return None

        result = self._arr[0]
        
        if result is None:
            return None

        self._arr[0] = self._arr[self.get_size() - 1]
        self._arr.remove_at(self.get_size() - 1)

        # Heapify to maintain properties
        self.heapify(self._arr, self._arr.get_size(), 0)

        return result.get_value()

    def heapify(self, lst: DynamicArray | List, size: int, idx: int):
        """
        Goes down the heap to make sure that the heap property is being maintained
        """
        smallest = idx

        while idx < size:
            left = 2 * idx + 1
            right = 2 * idx + 2

            s = lst[smallest]
            l = lst[left]
            r = lst[right]

            if left < size and (l is not None and s is not None): 
                if s.get_key() > l.get_key():
                    smallest = left

            if right < size and (r is not None and s is not None):
                if s.get_key() > r.get_key():
                    smallest = right

            if smallest != idx:
                lst[idx], lst[smallest] = lst[smallest], lst[idx]
                idx = smallest

            else:
                break

    def get_size(self) -> int:
        """
        Does what it says on the tin
        """
        return self._arr.get_size()

    def is_empty(self) -> bool:
        """
        Ditto above
        """
        return self._arr.is_empty()

    def ip_build(self, input_list: DynamicArray) -> None:
        """
        Take ownership of the list of Entry types, and build a heap
        in-place. That is, turn input_list into a heap, and store it
        inside the self._arr as a DynamicArray. You might like to
        use the DynamicArray build_from_list function. You must use
        only O(1) extra space.

        [9, 8, 7, 6, 5, 4, 3, 2, 1, N, N, N]
        """

        size = input_list.get_size() - 1 
        l_node = (size // 2) - 1  # last non-leaf node is at n//2 -1

        # want to maintian the order for the tree's
        for idx in range(l_node, -1, -1):
            smallest = idx

            while idx < size:
                left = 2 * idx + 1
                right = 2 * idx + 2

                s = input_list[smallest]
                l = input_list[left]
                r = input_list[right]

                if left < size and (l is not None and s is not None): 
                    if s > l:
                        smallest = left

                if right < size and (r is not None and s is not None):
                    if s > r:
                        smallest = right

                if smallest != idx:
                    input_list[idx], input_list[smallest] = input_list[smallest], input_list[idx]
                    idx = smallest

                else:
                    break

        self._arr = input_list

    def sort(self) -> DynamicArray:
        """
        Use HEAPSORT to sort the heap being maintained in self._arr, using
        self._arr to store the output (in-place). You must use only O(1)
        extra space. Once sorted, return self._arr (the DynamicArray of
        Entry types).

        Once this sort function is called, the heap can be considered as
        destroyed and will not be used again (hence returning the underlying
        array back to the caller).
        """
        for idx in range(self._arr.get_size()):
            val = self.remove_min()
            self._arr[self.get_size() - idx] = val
         
        return self._arr
