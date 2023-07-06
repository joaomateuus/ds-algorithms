"""
Find the smallest missing element from a sorted array

Given a sorted array of non-negative distinct integers, find the smallest missing non-negative element in it.

"""

def problem(arr: list):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == mid:
            low = mid + 1
        else:
            high = mid - 1

    return low


print(problem([0, 1, 2, 3, 4, 5, 6]))