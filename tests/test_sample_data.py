"""Initialise distance inputs and expected outputs for a give node"""
INF = 9999

graph1_node_input = [
    [
        [0, 7, INF, 8],
        [INF, 0, 5, INF],
        [INF, INF, 0, 2],
        [INF, INF, INF, 0]
        ]
]

graph1_expected_output = [
    [
        [0, 7, 12, 8],
        [INF, 0, 5, INF],
        [INF, INF, 0, 2],
        [INF, INF, INF, 0]
        ]
]
graph2_node_input = [
    [
        [0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0]
        ]
]

graph2_expected_output = [
    [
        [0, 3, INF, 7],
        [8, 0, 2, 15],
        [5, 8, 0, 1],
        [2, 8, INF, 0]
        ]
]
