def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Finde das Minimum im unsortierten Teil des Arrays
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Tausche das Minimum mit dem aktuellen Element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Beispielaufruf
array = [64, 25, 12, 22, 11]
sorted_array = selection_sort(array)
print("Sortiertes Array:")
print(sorted_array)