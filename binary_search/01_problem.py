"""
Find the number of rotations in a circularly sorted array
Given a circularly sorted integer array, find the total number of times the array is rotated.
Assume there are no duplicates in the array, and the rotation is in the anti-clockwise direction.

Input:  nums = [8, 9, 10, 2, 5, 6]
Output: The array is rotated 3 times
 
 
Input:  nums = [2, 5, 6, 8, 9, 10]
Output: The array is rotated 0 times
"""

def problem(arr: list):    
    low = 0
    high = len(arr) - 1
    
    # check if the first index is lower than the last if its return zero
    if arr[low] < arr[high]:
        return low
    
    while low <= high:
        middle = low + (high - low) // 2
        prev = (middle + len(arr) - 1) % len(arr)
        next = (middle + 1) % len(arr)
        
        # checar o pivot, se o meio da lista for, retorna o index do pivot
        if arr[middle] < arr[prev] and arr[middle] < arr[next]:
            return middle
        
        # check the rotation direction and adjust the pointers
        elif arr[middle] > arr[high]:
            low = middle + 1
        else:
            high = middle - 1
            
resultado = problem([2, 5, 6, 8, 9, 10])
print(resultado)