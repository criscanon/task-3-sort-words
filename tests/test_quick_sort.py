import unittest
from sorting_algorithms.quick_sort import quick_sort

class TestQuickSort(unittest.TestCase):
    """
    Test case for Quick Sort algorithm.
    """
    
    def test_quick_sort(self):
        """
        Test if quick_sort() sorts the list correctly.
        """
        test_list = ["banana", "apple", "orange", "grape", "kiwi"]
        sorted_list = quick_sort(test_list)
        self.assertEqual(sorted_list, ["apple", "banana", "grape", "kiwi", "orange"])
        
    def test_quick_sort_empty_list(self):
        """
        Test if quick_sort() handles an empty list correctly.
        """
        test_list = []
        sorted_list = quick_sort(test_list)
        self.assertEqual(sorted_list, [])
        
    def test_quick_sort_single_element_list(self):
        """
        Test if quick_sort() handles a list with a single element correctly.
        """
        test_list = ["apple"]
        sorted_list = quick_sort(test_list)
        self.assertEqual(sorted_list, ["apple"])
        
    def test_quick_sort_reverse_sorted(self):
        """
        Test if quick_sort() handles a list sorted in reverse order correctly.
        """
        test_list = ["orange", "kiwi", "grape", "banana", "apple"]
        sorted_list = quick_sort(test_list)
        self.assertEqual(sorted_list, ["apple", "banana", "grape", "kiwi", "orange"])

    def test_quick_sort_already_sorted(self):
        """
        Test if quick_sort() handles a list that is already sorted correctly.
        """
        test_list = ["apple", "banana", "grape", "kiwi", "orange"]
        sorted_list = quick_sort(test_list)
        self.assertEqual(sorted_list, ["apple", "banana", "grape", "kiwi", "orange"])

    def test_quick_sort_same_elements(self):
        """
        Test if quick_sort() handles a list with all elements being the same correctly.
        """
        test_list = ["apple", "apple", "apple", "apple", "apple"]
        sorted_list = quick_sort(test_list)
        self.assertEqual(sorted_list, ["apple", "apple", "apple", "apple", "apple"])

    def test_quick_sort_lower_bound(self):
        """
        Test if quick_sort() handles a list with elements in the lower bound correctly.
        """
        test_list = ["a", "b", "c", "d", "e"]
        sorted_list = quick_sort(test_list)
        self.assertEqual(sorted_list, ["a", "b", "c", "d", "e"])

    def test_quick_sort_upper_bound(self):
        """
        Test if quick_sort() handles a list with elements in the upper bound correctly.
        """
        test_list = ["z", "y", "x", "w", "v"]
        sorted_list = quick_sort(test_list)
        self.assertEqual(sorted_list, ["v", "w", "x", "y", "z"])

if __name__ == "__main__":
    unittest.main()
