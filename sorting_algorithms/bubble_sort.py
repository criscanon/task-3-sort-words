def bubble_sort(arr):
    """
    Sort an array using Bubble Sort algorithm.
    
    Parameters:
    arr (list): The input list to be sorted.
    
    Returns:
    list: The sorted list.
    """
    n = len(arr)                                        # O(1)
    
    for i in range(n):                                  # O(n)
        for j in range(0, n-i-1):                       # O(n)
            if arr[j] > arr[j+1]:                       # O(1)
                arr[j], arr[j+1] = arr[j+1], arr[j]     # O(1)
    
    return arr

# Complexity: O(n) * O(n) ≈ O(n^2)
# Average complexity: O(n^2)