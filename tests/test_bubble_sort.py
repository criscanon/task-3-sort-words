import unittest
from sorting_algorithms.bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    """
    Test case for Bubble Sort algorithm.
    """
    
    def test_bubble_sort(self):
        """
        Test if bubble_sort() sorts the list correctly.
        """
        test_list = ["banana", "apple", "orange", "grape", "kiwi"]
        sorted_list = bubble_sort(test_list)
        self.assertEqual(sorted_list, ["apple", "banana", "grape", "kiwi", "orange"])
        
    def test_bubble_sort_empty_list(self):
        """
        Test if bubble_sort() handles an empty list correctly.
        """
        test_list = []
        sorted_list = bubble_sort(test_list)
        self.assertEqual(sorted_list, [])
        
    def test_bubble_sort_single_element_list(self):
        """
        Test if bubble_sort() handles a list with a single element correctly.
        """
        test_list = ["apple"]
        sorted_list = bubble_sort(test_list)
        self.assertEqual(sorted_list, ["apple"])
        
    def test_bubble_sort_reverse_sorted(self):
        """
        Test if bubble_sort() handles a list sorted in reverse order correctly.
        """
        test_list = ["orange", "kiwi", "grape", "banana", "apple"]
        sorted_list = bubble_sort(test_list)
        self.assertEqual(sorted_list, ["apple", "banana", "grape", "kiwi", "orange"])

    def test_bubble_sort_already_sorted(self):
        """
        Test if bubble_sort() handles a list that is already sorted correctly.
        """
        test_list = ["apple", "banana", "grape", "kiwi", "orange"]
        sorted_list = bubble_sort(test_list)
        self.assertEqual(sorted_list, ["apple", "banana", "grape", "kiwi", "orange"])

    def test_bubble_sort_same_elements(self):
        """
        Test if bubble_sort() handles a list with all elements being the same correctly.
        """
        test_list = ["apple", "apple", "apple", "apple", "apple"]
        sorted_list = bubble_sort(test_list)
        self.assertEqual(sorted_list, ["apple", "apple", "apple", "apple", "apple"])

    def test_bubble_sort_lower_bound(self):
        """
        Test if bubble_sort() handles a list with elements in the lower bound correctly.
        """
        test_list = ["a", "b", "c", "d", "e"]
        sorted_list = bubble_sort(test_list)
        self.assertEqual(sorted_list, ["a", "b", "c", "d", "e"])

    def test_bubble_sort_upper_bound(self):
        """
        Test if bubble_sort() handles a list with elements in the upper bound correctly.
        """
        test_list = ["z", "y", "x", "w", "v"]
        sorted_list = bubble_sort(test_list)
        self.assertEqual(sorted_list, ["v", "w", "x", "y", "z"])

if __name__ == "__main__":
    unittest.main()
