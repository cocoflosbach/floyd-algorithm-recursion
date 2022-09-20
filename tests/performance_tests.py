"""Get and compare runtime performance between the recursive
and imperative versions of the Floyd_Warshall algorithm"""

import cProfile
import timeit
import sys
sys.path.append('/Users/cocoflosbach/Documents/UOL/software-dev-projects/floyd-algorithm-recursion/src')

# Import the recursive and imperative functions from the source folder
# import src.floyd_imperative as floyd_imperative
# import src.floyd_recursive as floyd_recursive
from src.floyd_imperative import floyd_warshall_imp
from src.floyd_recursive import floyd_warshall_rec

# Import sample test data from testdata file
from tests.test_sample_data import (graph1_node_input)

# Performance tests for recursive function
cProfile.run("floyd_warshall_rec(graph1_node_input)")
cProfile.run("floyd_warshall_rec(graph2_node_input)")

# Performance tests for imperative functions
cProfile.run("floyd_warshall_imp(graph1_node_input)")
cProfile.run("floyd_warshall_imp(graph2_node_input)")


def compare_performance():
    """Define function to calculate the runtime for both verions of the algorithm"""
    INF = 9999
    graph = [
        [
        [0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0]
        ]
    ]

    # Calculate time execution time for the recursive version
    recursive_time = timeit.timeit("floyd_warshall_rec(graph)", number= 4000)
    # Calculate time execution time for the recursive version
    imperative_time = timeit.timeit("floyd_warshall_imp(graph)", number= 4000)
    print("Recursive execution time: " + recursive_time)
    print("Imperative execution time: " + imperative_time)



if __name__ == '__main__':
    compare_performance()
