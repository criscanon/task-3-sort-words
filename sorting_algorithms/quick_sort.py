def quick_sort(arr):
    """
    Sort an array using Quick Sort algorithm.
    
    Parameters:
    arr (list): The input list to be sorted.
    
    Returns:
    list: The sorted list.
    """
    if len(arr) <= 1:  # O(1) - Verificar si la lista tiene 0 o 1 elemento
        return arr

    pivot = arr[len(arr) // 2]  # O(1) - Seleccionar el pivote en la posición del medio
    
    left = [x for x in arr if x < pivot]  # O(n) - Crear la lista de elementos menores que el pivote
    middle = [x for x in arr if x == pivot]  # O(n) - Crear la lista de elementos iguales al pivote
    right = [x for x in arr if x > pivot]  # O(n) - Crear la lista de elementos mayores que el pivote

    return quick_sort(left) + middle + quick_sort(right)  # Recursión en las sublistas

# Complexity: O(n) * O(n) ≈ O(n^2)
# Average complexity: O(n log n)