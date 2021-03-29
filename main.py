#!/bin/python3


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 40, 60, 400, 8000, 8001, 8002, 8003, 8004, 9000, 10000, 13000]
x = 8003


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        return -1


if __name__ == '__main__':
    result = binary_search(arr, 0, len(arr) - 1, x)
    if result != -1:
        print("Element is at index", str(result))
    else:
        print("Element is not in the array")
