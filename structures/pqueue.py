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
        idx = 0
        smallest = idx
        size = self._arr.get_size()

        while idx < size:
            left = 2 * idx + 1
            right = 2 * idx + 2

            s = self._arr[smallest]
            l = self._arr[left]
            r = self._arr[right]

            if left < size and (l is not None and s is not None): 
                if s.get_key() > l.get_key():
                    smallest = left

            if right < size and (r is not None and s is not None):
                if s.get_key() > r.get_key():
                    smallest = right

            if smallest != idx:
                self._arr[idx], self._arr[smallest] = self._arr[smallest], self._arr[idx]
                idx = smallest

            else:
                break

        return result.get_value()

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
        n = input_list.get_size()
        idx = 1
        while idx < n:
            parent = (idx - 1) // 2
            parent_val = input_list[parent]
            current_val = input_list[idx]

            if parent_val is not None and current_val is not None:  # if both exist, swap and recheck
                if parent_val > current_val:
                    input_list[idx], input_list[parent] = input_list[parent], input_list[idx]
                    idx = parent
                    continue
            idx += 1

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
        size = self.get_size()
        n_size = size
        for idx in range(size):
            self._arr[0], self._arr[n_size - 1] = self._arr[n_size - 1], self._arr[0]

            indx = 0
            smallest = idx
            while indx < n_size:
                left = 2 * indx + 1
                right = 2 * indx + 2

                s = self._arr[smallest]
                l = self._arr[left]
                r = self._arr[right]

                if left < n_size and (l is not None and s is not None): 
                    if s.get_key() > l.get_key():
                        smallest = left

                if right < n_size and (r is not None and s is not None):
                    if s.get_key() > r.get_key():
                        smallest = right

                if smallest != indx:
                    self._arr[indx], self._arr[smallest] = self._arr[smallest], self._arr[indx]
                    indx = smallest

                else:
                    break

            n_size -= 1

        return self._arr
