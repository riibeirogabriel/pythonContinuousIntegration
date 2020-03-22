import unittest
from OpsNumbers import sum


class TestSum(unittest.TestCase):
    def test_result_sum(self):
        data = [1, 2, 3, 4]
        self.assertEqual(sum(data), 10,
                         "Error in function sum from Module OpsNumbers")

    def test_type_sum(self):
        set_tuple = (1, 2, 3, 4)
        set_list = [1, 2, 3, 4]
        set_set = set([1, 2, 3, 4])
        self.assertEqual(sum(set_tuple), 10,
                         "TypeError in function sum from Module OpsNumbers")
        self.assertEqual(sum(set_list), 10,
                         "TypeError in function sum from Module OpsNumbers")
        self.assertEqual(sum(set_set), 10,
                         "TypeError in function sum from Module OpsNumbers")


if __name__ == "__main__":
    unittest.main()
