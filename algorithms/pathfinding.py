"""
Skeleton for COMP3506/7505 A2, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov

You may wish to import your data structures to help you with some of the
problems. Or maybe not. We did it for you just in case.
"""
from structures.entry import Entry
from structures.dynamic_array import DynamicArray
from structures.graph import Graph, LatticeGraph, Node
from structures.map import Map
from structures.pqueue import PriorityQueue
from structures.bloom_filter import BloomFilter
from structures.util import Hashable

def bfs_traversal(
    graph: Graph | LatticeGraph, origin: int, goal: int
    ) -> tuple[DynamicArray, DynamicArray]:
    """
    Task 2.1: Breadth First Search

    @param: graph
      The general graph or lattice graph to process
    @param: origin
      The ID of the node from which to start traversal
    @param: goal
      The ID of the target node

    @returns: tuple[DynamicArray, DynamicArray]
      1. The ordered path between the origin and the goal in node IDs
      (or an empty DynamicArray if no path exists);
      2. The IDs of all nodes in the order they were visited.


    Q = new empty queue
    Q.enqueue(u)
    Mark vertex u as visited
    while not Q.isEmpty() do
        v = Q.dequeue()
        for all e in G.incidentEdges(v) do
            if e is not explored then
                w <- G.opposite(v, e)
                if w has not been visited then
                    Record edge e as a discovery edge for vertex w
                    Q.enqueue(w)
                    Mark vertex w as visited
                else
                    Mark e as a cross edge
    """
    # Stores the keys of the nodes in the order they were visited
    visited_order = DynamicArray()
    visited_nodes = Map()

    # Stores the path from the origin to the goal
    path = DynamicArray()

    # ALGO GOES HERE
    Q = PriorityQueue()
    start = graph.get_node(origin)
    end = graph.get_node(goal)
    found = False

    if start is not None and end is not None:
        Q.insert_fifo(start)
        visited_order.append(start.get_id())
        visited_nodes.insert_kv(start.get_id(), start.get_id())

        while not Q.is_empty():
            current = Q.remove_min()
            visited_order.append(current.get_id())
            if current is end:
                path.append(current.get_id())
                found = True
                break

            for neighbor in graph.get_neighbours(current):  
                if isinstance(neighbor, Node):
                    if visited_nodes.find(neighbor.get_id()) is None:  # if neighbor not explored
                        Q.insert_fifo(neighbor)
                        visited_nodes.insert_kv(neighbor.get_id(), current.get_id())  # mark as visited

        if found:  # reverse the list
            current = end.get_id()
            while current is not start.get_id():
                current = visited_nodes.find(current)
                path.append(current)

            len = path.get_size()
                

    return (path, visited_order)   # Return the path and the visited nodes list


def dijkstra_traversal(
    graph: Graph, origin: int, goal: int
    ) -> tuple[DynamicArray, DynamicArray]:
    """
    Task 2.2: Dijkstra Traversal

    @param: graph
      The *weighted* graph to process (POSW graphs)
    @param: origin
      The ID of the node from which to start traversal
    @param: goal
      The ID of the target node

    @returns: tuple[DynamicArray, DynamicArray]
      1. The ordered path between the origin and the goal in node IDs;
      2. The IDs of all nodes in the order they were visited.

    NOTE: Dijkstra does not work (by default) on LatticeGraph types.
    This is because there is no inherent weight on an edge of these
    graphs. It should of course work where edge weights are uniform.
    """

    # Stores the keys of the nodes in the order they were visited
    visited_order = DynamicArray()
    # Stores the path from the origin to the goal
    path = DynamicArray()

    # ALGO GOES HERE

    # Return the path and the visited nodes list
    return (path, visited_order)


def dfs_traversal(
    graph: Graph | LatticeGraph, origin: int, goal: int
    ) -> tuple[DynamicArray, DynamicArray]: 
    """
    Task 2.3: Depth First Search **** COMP7505 ONLY ****
    COMP3506 students can do this for funsies.

    @param: graph
      The general graph or lattice graph to process
    @param: origin
      The ID of the node from which to start traversal
    @param: goal
      The ID of the target node

    @returns: tuple[DynamicArray, DynamicArray]
      1. The ordered path between the origin and the goal in node IDs
      (or an empty DynamicArray if no path exists);
      2. The IDs of all nodes in the order they were visited.
    
    """
    # Stores the keys of the nodes in the order they were visited
    visited_order = DynamicArray()
    # Stores the path from the origin to the goal
    path = DynamicArray()

    # ALGO GOES HERE

    # Return the path and the visited nodes list
    return (path, visited_order)

