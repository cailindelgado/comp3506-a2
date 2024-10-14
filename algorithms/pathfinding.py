"""
Skeleton for COMP3506/7505 A2, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov

You may wish to import your data structures to help you with some of the
problems. Or maybe not. We did it for you just in case.
"""
import math
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
    """
    # Stores the keys of the nodes in the order they were visited
    visited_order = DynamicArray()
    visited_nodes = Map()

    # Stores the path from the origin to the goal
    path = DynamicArray()

    Q = PriorityQueue()
    start = graph.get_node(origin)
    end = graph.get_node(goal)
    found = False

    if start is not None and end is not None:
        Q.insert_fifo(start)
        visited_nodes.insert_kv(start.get_id(), start.get_id())

        while not Q.is_empty():
            current = Q.remove_min()
            visited_order.append(current.get_id())
            if current is end:
                found = True
                break

            for neighbor in graph.get_neighbours(current.get_id()):  
                if isinstance(neighbor, Node):
                    if visited_nodes.find(neighbor.get_id()) is None:  # if neighbor not explored
                        Q.insert_fifo(neighbor)
                        visited_nodes.insert_kv(neighbor.get_id(), current.get_id())  # mark as visited

        if found:  # if the goal has been found then create the shortest path
            current = end.get_id()
            while current is not start.get_id():
                path.append(current)
                current = visited_nodes.find(current)

            path.append(current)

            # as path has the path backwards, now to correct it
            len = path.get_size()
            lst = [0] * len
            counter = 0
            for i in range(len - 1, -1, -1):
                lst[counter] = path[i]
                counter += 1

            path.build_from_list(lst)  # eat the corrected list

    return (path, visited_order)   # Return the path and the visited nodes list

def dijkstra_traversal(graph: Graph, origin: int) -> DynamicArray:
    """
    Task 2.2: Dijkstra Traversal

    @param: graph
      The *weighted* graph to process (POSW graphs)
    @param: origin
      The ID of the node from which to start traversal.

    @returns: DynamicArray containing Entry types.
      The Entry key is a node identifier, Entry value is the cost of the
      shortest path to this node from the origin.

    NOTE: Dijkstra does not work (by default) on LatticeGraph types.
    This is because there is no inherent weight on an edge of these
    graphs. It should of course work where edge weights are uniform.
    """
    valid_locations = DynamicArray() # This holds your answers
    valid_locations.allocate(len(graph._nodes), 0)

    PQ = PriorityQueue()

    for node in graph._nodes:
        if node.get_id() == origin:
            # print(f'setting: @ {node.get_id()}, with 0')
            valid_locations.set_at(node.get_id(), Entry(node.get_id, 0))
        else:
            # print(f'setting: @ {node.get_id()}, with inf')
            valid_locations.set_at(node.get_id(), Entry(node.get_id, math.inf))

        insert_dist = valid_locations[node.get_id()].get_value()
        if insert_dist is not None:
            PQ.insert(insert_dist, node.get_id())  # inserts (k=distance, v=node_id)

    while not PQ.is_empty():
        current = PQ.remove_min()  # get the id of the node with the smallest weight

        print(f'\n--- NEW LOOP @ {current} ---\n')
        for node_info in graph.get_neighbours(current):
            if isinstance(node_info, tuple):
                neighbor = node_info[0]
                weight = node_info[1]
                print(f"({str(neighbor)}, {weight})")

                dist = valid_locations[current].get_value()
                if dist is not None:
                    new_dist = dist + weight
                
                    print(f'n_dist - {new_dist}, old dist - {valid_locations[neighbor.get_id()].get_value()}')
                    print(new_dist < valid_locations[neighbor.get_id()].get_value())
                    if new_dist < valid_locations[neighbor.get_id()].get_value():
                        print('updating')
                        # print(f'updated node {neighbor.get_id()} from an old dist of {valid_locations[neighbor.get_id()].get_value()} to {new_dist}')
                        print(PQ)
                        valid_locations[neighbor.get_id()] = Entry(neighbor.get_id(), new_dist)  # (vertix, dist)
                        print(str(valid_locations[neighbor.get_id()]))
                        PQ.update(new_dist, neighbor.get_id())
                        print(PQ)
                print("\n")

    # Return the DynamicArray containing Entry types
    return valid_locations


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

