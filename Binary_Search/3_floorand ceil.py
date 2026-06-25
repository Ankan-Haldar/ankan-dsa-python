def getFloorAndCeil(a, n, x):
    floor_val = -1
    ceil_val = -1

    low, high = 0, n - 1

    # Find Floor
    while low <= high:
        mid = (low + high) // 2

        if a[mid] <= x:
            floor_val = a[mid]
            low = mid + 1
        else:
            high = mid - 1

    low, high = 0, n - 1

    # Find Ceil
    while low <= high:
        mid = (low + high) // 2

        if a[mid] >= x:
            ceil_val = a[mid]
            high = mid - 1
        else:
            low = mid + 1

    return floor_val, ceil_val


# Example
n = 6
x = 5
a = [3, 4, 7, 8, 8, 10]

floor_val, ceil_val = getFloorAndCeil(a, n, x)

print("Floor:", floor_val)
print("Ceil:", ceil_val)