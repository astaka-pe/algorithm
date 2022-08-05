def binary_search(key, a):
    left = 0
    right = len(a) - 1
    while right >= left:
        mid = left + (right - left) // 2
        if a[mid] == key:
            return mid
        elif a[mid] > key:
            right = mid - 1
        elif a[mid] < key:
            left = mid + 1
    return -1

N = 8
a = [3, 5, 8, 10, 14, 17, 21, 39]

print(binary_search(10, a))
print(binary_search(3, a))
print(binary_search(39, a))
print(binary_search(-100, a))
print(binary_search(9, a))
print(binary_search(100, a))