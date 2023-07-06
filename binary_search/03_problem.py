"""
Problem:

Given a sorted integer array, find the index of a given numbers first or last occurrence.
If the element is not present in the array, report that as well.

**************** Behavior ****************

Input:
 
nums = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
target = 5
 
Output:
 
The first occurrence of element 5 is located at index 1
The last occurrence of element 5 is located at index 3
 
 
Input:
 
nums = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
target = 4
 
Output:
 
Element not found in the array

*******************************

- Following the classic binary search would finish on the first occurrence
- We have to adjust it to search in the left side to find the first occurrence
- And in the right side to find the last occurrence

"""

def problem(arr: list, target: int):
    low = 0
    high = len(arr) - 1
    
    first_occ = -1
    
    while low <= high:
        middle = (low + high) // 2
        
        if target == arr[middle]:
            first_occ = middle
            high = middle - 1
            
        elif target > arr[middle]:
            low = middle + 1
        else:
            high = middle - 1
    
    last_occ = search_right_side(arr, target)
    return first_occ, last_occ

def search_right_side(arr: list, target: int):
    low = 0
    high = len(arr) - 1
    
    last_occ = -1
    
    while low <= high: 
        middle = (low + high) // 2
        
        if target == arr[middle]:
            last_occ = middle
            low = middle + 1
            
        elif target > arr[middle]:
            low = middle + 1
        else:
            high = middle - 1
    return last_occ
    

first, last = problem([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5)

if first != -1 and last != -1:
    print(f"The first occurrence was on the {first} index")
    print(f"The last occurrence was on the {last} index")
else:
    print("Element not found")            