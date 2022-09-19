"""Unit testing the floyd_warshall imperative algorithm version"""

import unittest

from floyd_imperative import floyd_warshall_imp
#Import sample test data from testdata file
from tests.test_sample_data import (graph1_node_input, graph1_expected_output,
                                    graph2_node_input, graph2_expected_output)

class TestFloydWarshallImperative(unittest.TestCase):
    """Test Class for the Floyd_warshall recursive algorithm"""

    def test_floyd_warshall_imp1(self):
        """Fist test case checks that the actual output returned is equal to the expected
        output of graph1_node_input defined in the test data file"""

        self.assertEqual(floyd_warshall_imp(graph1_node_input), graph1_expected_output,
                            "Test Failed. Actual output does not match expected output")

    def test_floyd_warshall_imp2(self):
        """Second test case checks that the actual output returned is equal to the expected
        output of graph2_node_input defined in the test data file"""

        self.assertEqual(floyd_warshall_imp(graph2_node_input), graph2_expected_output,
                            "Test Failed. Actual output does not match expected output")


if __name__ == '__main__':
    unittest.main()
        