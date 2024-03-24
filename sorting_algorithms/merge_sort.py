def merge_sort(arr):
    """
    Sort an array using Merge Sort algorithm.
    
    Parameters:
    arr (list): The input list to be sorted.
    
    Returns:
    list: The sorted list.
    """
    if len(arr) > 1:                        # O(1)
        mid = len(arr) // 2                 # O(1)
        
        L = arr[:mid]                       # O(n/2)
        R = arr[mid:]                       # O(n/2)

        merge_sort(L)                       # O(log n)
        merge_sort(R)                       # O(log n)

        i = j = k = 0                       # O(1)
        while i < len(L) and j < len(R):    # O(n)
            if L[i] < R[j]:                 # O(1)
                arr[k] = L[i]               # O(1)
                i += 1                      # O(1)
            else:
                arr[k] = R[j]               # O(1)
                j += 1                      # O(1)
            k += 1                          # O(1)

        while i < len(L):                   # O(n)
            arr[k] = L[i]                   # O(1)
            i += 1                          # O(1)
            k += 1                          # O(1)

        while j < len(R):                   # O(n)
            arr[k] = R[j]                   # O(1)
            j += 1                          # O(1)
            k += 1                          # O(1)
    
    return arr                              # O(1)

# Complexity: O(log n) * O(n) ≈ O(n log n)
# Average complexity: O(n log n)
