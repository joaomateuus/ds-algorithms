"""
Find floor and ceil of a number in a sorted integer array

Given a sorted integer array, find the floor and ceil of a given number in it.
The floor and ceil map the given number to the largest previous or the smallest following integer in the array.
More precisely, for a number x, floor(x) is the largest integer in the array less than or equal to x,
and ceil(x) is the smallest integer in the array greater than or equal to x. If the floor or ceil doesnt exist, consider it to be -1. For example,

Input:
 
nums[] = [1, 4, 6, 8, 9]
Number: 0 to 10
 
Output:
 
Number 0 -> ceil is 1, floor is -1
Number 1 -> ceil is 1, floor is 1
Number 2 -> ceil is 4, floor is 1
Number 3 -> ceil is 4, floor is 1
Number 4 -> ceil is 4, floor is 4
Number 5 -> ceil is 6, floor is 4
Number 6 -> ceil is 6, floor is 6
Number 7 -> ceil is 8, floor is 6
Number 8 -> ceil is 8, floor is 8
Number 9 -> ceil is 9, floor is 9
Number 10 -> ceil is -1, floor is 9
"""

def problem_ceil(arr: list, num: int):
    low = 0
    high = len(arr) - 1
    ceil = -1
    
    while low <= high:
        middle = (low + high) // 2
        
        if arr[middle] == num:
            return arr[middle]
        elif num > arr[middle]:
            low = middle + 1
        else:
            ceil = arr[middle]
            high = middle - 1
    return ceil

def problem_floor(arr: list, num: int):
    low = 0
    high = len(arr) - 1
    floor = -1
    
    while low <= high:
        middle = (low + high) // 2
        
        if arr[middle] == num:
            return arr[middle]
        elif num > arr[middle]:
            floor = arr[middle]
            low = middle + 1
        else:
            high = middle - 1
    return floor

nums = [1, 4, 6, 8, 9]
 
for i in range(max(nums) + 2):
    print(f'Number {i} -> ceil is {problem_ceil(nums, i)},floor is {problem_floor(nums, i)}')
 