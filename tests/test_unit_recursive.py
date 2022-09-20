"""Unit testing the floyd_warshall recursive algorithm version"""

import unittest
# Import the recursive function from the source folder
from src.floyd_recursive import floyd_warshall_rec
# Import sample test data from testdata file
from tests.test_sample_data import (graph1_node_input, graph1_expected_output,
                                    graph2_node_input, graph2_expected_output)



class TestFloydWarshallRecursive(unittest.TestCase):
    """Test Class for the Floyd_warshall recursive algorithm"""

    def test_floyd_warshall_rec1(self):
        """Fist test case checks that the actual output returned is equal to the expected
        output of graph1_node_input defined in the test data file"""

        self.assertEqual(floyd_warshall_rec(graph1_node_input), graph1_expected_output,
                            "Test Failed. Actual output does not match expected output")

    def test_floyd_warshall_rec2(self):
        """Second test case checks that the actual output returned is equal to the expected
        output of graph2_node_input defined in the test data file"""

        self.assertEqual(floyd_warshall_rec(graph2_node_input), graph2_expected_output,
                            "Test Failed. Actual output does not match expected output")


if __name__ == '__main__':
    unittest.main()
