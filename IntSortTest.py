import unittest
from IntSort import SortInteger  # Import the SortInteger class from IntSort module

# Defined a test class that inherits from unittest.TestCase
class TestSortInteger(unittest.TestCase):

    # Set up a list of unsorted integers for testing
    def setUp(self):
        self.unsorted_array = [211, 34, 545, 6, 1, 0, 23, 98, 76, 12,
                 45, 67, 89, 32, 11, 90, 54, 87, 23, 65,
                 87, 12, 56, 32, 10, 2, 43, 87, 34, 76,
                 8, 99, 31, 78, 54, 20, 7, 19, 65, 77,
                 43, 90, 15, 37, 88, 44, 61, 29, 53, 76]

    # Test insertion sort
    def test_insertion_sort(self):
        sorted_array, time_consumed = SortInteger.SortInteger(self.unsorted_array, "InsertionSort")
        self.assertEqual(sorted_array, sorted(self.unsorted_array))  # Check if the array is sorted
        self.assertGreaterEqual(time_consumed, 0)  # Check if time consumed is non-negative

    # Test bubble sort
    def test_bubble_sort(self):
        sorted_array, time_consumed = SortInteger.SortInteger(self.unsorted_array, "BubbleSort")
        self.assertEqual(sorted_array, sorted(self.unsorted_array))
        self.assertGreaterEqual(time_consumed, 0)

    # Test merge sort
    def test_merge_sort(self):
        sorted_array, time_consumed = SortInteger.SortInteger(self.unsorted_array, "MergeSort")
        self.assertEqual(sorted_array, sorted(self.unsorted_array))
        self.assertGreaterEqual(time_consumed, 0)

    # Test heap sort
    def test_heap_sort(self):
        sorted_array, time_consumed = SortInteger.SortInteger(self.unsorted_array, "HeapSort")
        self.assertEqual(sorted_array, sorted(self.unsorted_array))
        self.assertGreaterEqual(time_consumed, 0)

    # Test bucket sort
    def test_bucket_sort(self):
        sorted_array, time_consumed = SortInteger.SortInteger(self.unsorted_array, "BucketSort")
        self.assertEqual(sorted_array, sorted(self.unsorted_array))
        self.assertGreaterEqual(time_consumed, 0)

    # Test counting sort
    def test_counting_sort(self):
        sorted_array, time_consumed = SortInteger.SortInteger(self.unsorted_array, "CountingSort")
        self.assertEqual(sorted_array, sorted(self.unsorted_array))
        self.assertGreaterEqual(time_consumed, 0)

    # Test quick sort
    def test_quick_sort(self):
        sorted_array, time_consumed = SortInteger.SortInteger(self.unsorted_array, "QuickSort")
        self.assertEqual(sorted_array, sorted(self.unsorted_array))
        self.assertGreaterEqual(time_consumed, 0)

    # Test radix sort
    def test_radix_sort(self):
        sorted_array, time_consumed = SortInteger.SortInteger(self.unsorted_array, "RadixSort")
        self.assertEqual(sorted_array, sorted(self.unsorted_array))
        self.assertGreaterEqual(time_consumed, 0)

# Run the tests 
if __name__ == "__main__":
    unittest.main()
