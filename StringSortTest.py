import unittest
from StringSort import SortString  # Assuming your main code file is named "main.py"

class TestSortString(unittest.TestCase):

    def setUp(self):
        self.unsorted_array = ["California State University Fullerton", "California State University East Bay", "California State University Long Beach", "University Of Southern California", "Arizona State Univerity"]

    def test_insertion_sort(self):
        sorted_array, time_consumed = SortString.SortString(self.unsorted_array, "InsertionSort")
        self.assertEqual(sorted_array, sorted(self.unsorted_array))
        self.assertGreaterEqual(time_consumed, 0)

    def test_bubble_sort(self):
        sorted_array, time_consumed = SortString.SortString(self.unsorted_array, "BubbleSort")
        self.assertEqual(sorted_array, sorted(self.unsorted_array))
        self.assertGreaterEqual(time_consumed, 0)

    def test_merge_sort(self):
        sorted_array, time_consumed = SortString.SortString(self.unsorted_array, "MergeSort")
        self.assertEqual(sorted_array, sorted(self.unsorted_array))
        self.assertGreaterEqual(time_consumed, 0)

    def test_heap_sort(self):
        sorted_array, time_consumed = SortString.SortString(self.unsorted_array, "HeapSort")
        self.assertEqual(sorted_array, sorted(self.unsorted_array))
        self.assertGreaterEqual(time_consumed, 0)

if __name__ == "__main__":
    unittest.main()
