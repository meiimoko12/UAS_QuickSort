def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x > pivot]  # > karena sorting dari besar ke kecil
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]
    return quicksort(left) + middle + quicksort(right)


angka = [12, 45, 5, 67, 32, 66, 78, 10, 17, 9]
print("Data sebelum diurutkan:", angka)
print("Data setelah diurutkan (besar ke kecil):", quicksort(angka))