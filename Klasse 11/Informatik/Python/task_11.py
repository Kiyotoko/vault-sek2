def bubble_sort(arr):
    for n in range(len(arr), 1, -1):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Beispielaufruf
array = [64, 25, 12, 22, 11, 135, 42]
sorted_array = bubble_sort(array)
print("Sortiertes Array:")
print(sorted_array)