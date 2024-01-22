import unittest

"""unittest
    Python module for Unit testing
"""


from filter_integer import filter_integer

class TestFilterList(unittest.TestCase):

    #Check empty list
    def test_empty_input(self):
        input_list = []
        result = filter_integer(input_list)
        self.assertEqual(result, [])

    # Check expected output
    def test_valid_output(self):
        input_list = list(range(10))
        result = filter_integer(input_list)
        self.assertEqual(result, [1, 5, 7])

    #Check list length
    def test_invalid_length(self):
        input_list = list(range(15))
        with self.assertRaises(ValueError):
            filter_integer(input_list)

    # Expected Outpout for mixed_input is [2, 6, 8, 12, 14, 18, 20]
    def test_mixed_input(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        result = filter_integer(input_list)
        self.assertEqual(result, [2, 6, 8, 12, 14, 18, 20])

if __name__ == '__main__':
    unittest.main()
