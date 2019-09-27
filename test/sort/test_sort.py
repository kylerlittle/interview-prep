import unittest
from study.sort.sort import quicksort

class QuickSortTest(unittest.TestCase):
    def test_validsort(self):
        tests = [
            ([5,4,3,2,1], [1,2,3,4,5]),
            ([1,2,3,4,5], [1,2,3,4,5]),
            ([1,4,4,-8,9], [-8,1,4,4,9]),
            ([1], [1])
        ]
        for test in tests:
            inputTest, expectedOutput = test
            self.assertListEqual(expectedOutput, quicksort(inputTest))

    def test_invalidsort(self):
        self.assertListEqual([], quicksort([]))