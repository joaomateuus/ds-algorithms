"""
Search in a nearly sorted array in logarithmic time

Given a nearly sorted array such that each of the n elements may be misplaced by no more than one position from the correct sorted order, search a given element in it efficiently. Report if the element is not present in the array.

An element at index i in a correctly sorted order can be misplaced by the ± 1 position, i.e., it can be present at index i-1 or i or i+1 in the input array.

"""

def problem(arr: list, num: int):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        middle = (low + high) // 2
        
        if arr[middle] == num:
            return middle
        elif middle - 1 >= low and arr[middle - 1] == num:
            return middle - 1
        elif middle + 1 >= high and arr[middle + 1] == num:
            return middle + 1
        elif num > arr[middle]:
            low = middle + 2
        else:
            high = middle - 2
    return - 1


resultado = problem([2, 1, 3, 5, 4, 7, 6, 8, 9], 5)
print(f"Element found at index {resultado}")
