"""
Problem:
    - Count occurrences of a number in a sorted array with duplicates
    Given a sorted integer array containing duplicates, count occurrences of a given number. If the element is not found in the array, report that as well.

Behavior: 
Input:  nums[] = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
target = 5
 
Output: Target 5 occurs 3 times
 
 
Input:  nums[] = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
target = 6
 
Output: Target 6 occurs 2 times
"""

def problem(arr: list, target: int):
    low = 0
    high = len(arr) - 1
    occurrence_left = 0
    
    while low <= high:
        middle = (low + high) // 2
        
        if target == arr[middle]:
            occurrence_left += 1
            
            #search on the left side
            high = middle - 1
            
        elif target > arr[middle]:
            low = middle + 1
        else:
            high = middle - 1
    
    right_side_occ = search_on_right_side(arr, target)
    
    return occurrence_left + right_side_occ
            

def search_on_right_side(arr: list, target: int):
    low = 0
    high = len(arr) - 1
    occurrence_count = 0
    first_iteration = True
    
    while low <= high:
        
        middle = (low + high // 2) + 1 if first_iteration else (low + high) // 2
        first_iteration = False
    
        if target == arr[middle]:
            occurrence_count += 1
            
            #search on the right side
            low = middle + 1
        elif target > arr[middle]:
            low = middle + 1
        else:
            high = middle - 1
        
        
    return occurrence_count
            
resultado = problem([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 6)

if resultado != 0:
    print(f"The target was found {resultado} times")
else:
    print(f"Target was not found")