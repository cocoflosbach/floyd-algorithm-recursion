"""This is a program to create a recursive version
of the floyd_Warshall shortest paths algorithm."""



def floyd_warshall_algo(distance_graph):
    """A recursive implementation of Floyd's algorithm"""

    #Define number of nodes in the given graph
    node_number = len(distance_graph)

    #Define the infinite variable  which will be used for nodes not connected to each other
    INF = 9999

    #Write recursive function to find shortest path between two nodes.
    #Initialise variables [i] as start_node, [j] as end_node  and [k] as intermediate_node
    def fw_recursive_func(i, j, k):
        for k in range(node_number):
            for i in range(node_number):
                for j in range(node_number):

                    #If start_node [i] is equal to end_node [j]
                    if i == j:
                        return 0

                    #If intermediate [k] is less than 0
                    elif k < 0:
                        return distance_graph[i][j]

                    elif [i][j] >= INF:
                        return INF
                    else:
                        return min(fw_recursive_func(i, j, k),
                                fw_recursive_func(i, k, k -1) + fw_recursive_func(i, j, k - 1))
                distance_graph[i][j] = fw_recursive_func(i, j, k)
                return distance_graph
    print_dist_solution(distance_graph)


    def print_dist_solution(distance_graph):
        """Function to print out node values from recursive solution"""

        print("The following matix shows the shortest paths between all node pairs")
        for i in range(node_number):
            for j in range(node_number):
                if distance_graph[i][j] >= INF:
                    print("INF")
                else:
                    print(distance_graph[i][j])
        print(distance_graph[i][j])


    if __name__== "__main__":
        distance_graph = [
            [0, 7, INF, 8],
        [INF, 0, 5, INF],
        [INF, INF, 0, 2],
        [INF, INF, INF, 0]
        ]