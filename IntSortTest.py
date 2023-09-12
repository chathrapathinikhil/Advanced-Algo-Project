import unittest
from IntSort import SortInteger 

class TestSortInteger(unittest.TestCase):

    def setUp(self):
        self.unsorted_array = [211, 34, 545, 6, 1, 0, 23, 98, 76, 12,
                 45, 67, 89, 32, 11, 90, 54, 87, 23, 65,
                 87, 12, 56, 32, 10, 2, 43, 87, 34, 76,
                 8, 99, 31, 78, 54, 20, 7, 19, 65, 77,
                 43, 90, 15, 37, 88, 44, 61, 29, 53, 76]

    def test_insertion_sort(self):
        sorted_array, time_consumed = SortInteger.SortInteger(self.unsorted_array, "InsertionSort")
        self.assertEqual(sorted_array, sorted(self.unsorted_array))
        self.assertGreaterEqual(time_consumed, 0)

    def test_bubble_sort(self):
        sorted_array, time_consumed = SortInteger.SortInteger(self.unsorted_array, "BubbleSort")
        self.assertEqual(sorted_array, sorted(self.unsorted_array))
        self.assertGreaterEqual(time_consumed, 0)

    def test_merge_sort(self):
        sorted_array, time_consumed = SortInteger.SortInteger(self.unsorted_array, "MergeSort")
        self.assertEqual(sorted_array, sorted(self.unsorted_array))
        self.assertGreaterEqual(time_consumed, 0)

    def test_heap_sort(self):
        sorted_array, time_consumed = SortInteger.SortInteger(self.unsorted_array, "HeapSort")
        self.assertEqual(sorted_array, sorted(self.unsorted_array))
        self.assertGreaterEqual(time_consumed, 0)

    def test_bucket_sort(self):
        sorted_array, time_consumed = SortInteger.SortInteger(self.unsorted_array, "BucketSort")
        self.assertEqual(sorted_array, sorted(self.unsorted_array))
        self.assertGreaterEqual(time_consumed, 0)

    def test_counting_sort(self):
        sorted_array, time_consumed = SortInteger.SortInteger(self.unsorted_array, "CountingSort")
        self.assertEqual(sorted_array, sorted(self.unsorted_array))
        self.assertGreaterEqual(time_consumed, 0)

    def test_quick_sort(self):
        sorted_array, time_consumed = SortInteger.SortInteger(self.unsorted_array, "QuickSort")
        self.assertEqual(sorted_array, sorted(self.unsorted_array))
        self.assertGreaterEqual(time_consumed, 0)

    def test_radix_sort(self):
        sorted_array, time_consumed = SortInteger.SortInteger(self.unsorted_array, "RadixSort")
        self.assertEqual(sorted_array, sorted(self.unsorted_array))
        self.assertGreaterEqual(time_consumed, 0)

if __name__ == "__main__":
    unittest.main()
