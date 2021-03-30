#!/bin/python3
from random import randint


def generate_and_sort_array():
    x = 0
    arr = []

    while x < 1000:
        arr.append(randint(1, 1000))
        x += 1

    arr = sorted(arr)
    print(f'Updated List {arr}')

    return arr


def binary_search(arr, low, high, search):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == search:
            return mid

        elif arr[mid] > search:
            return binary_search(arr, low, mid - 1, search)

        else:
            return binary_search(arr, mid + 1, high, search)

    else:
        return -1


def main():
    search = 567
    print("Searching for", search, "in the: \n ")
    arr = generate_and_sort_array()

    return binary_search(arr, 0, len(arr) - 1, search)


if __name__ == '__main__':
    result = main()

    if result != -1:
        print("Element is at index", str(result))

    else:
        print("Element is not in the array")
