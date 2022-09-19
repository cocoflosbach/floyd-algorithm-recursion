"""This is an imperative version
of the floyd_Warshall shortest paths algorithm."""

import itertools

def floyd_warshall_imp(distance_graph):
    """A simple implementation of Floyd's algorithm"""
    #Define number of nodes in the given graph
    node_number = len(distance_graph)

    #Define the infinite variable  which will be used for nodes not connected to each other
    for intermediate, start_node, end_node\
        in itertools.product\
            (range(node_number), range(node_number), range(node_number)):
            #Assume that if start_node and end_node are the same
            #then the distance would be zero

        if start_node == end_node:
            distance_graph[start_node][end_node] = 0
            continue
            #return all possible paths and find the minimum
        distance_graph[start_node][end_node] = min(distance_graph[start_node][end_node], 
        distance_graph[start_node][intermediate] + [intermediate][end_node])
            #Any vallue that have sys.maxsize has no path
        print(distance_graph)
    floyd_warshall_imp(distance_graph)


    def floyd_warshall():
        for k in range(node_number):
            for i in range(node_number):
                for j in range(node_number):
                    distance_graph[i,j]= min(distance_graph[i,j], distance_graph[i,k] + distance_graph[k,j])
