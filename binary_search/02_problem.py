"""
Given a circularly sorted integer array, search an element in it.
Assume there are no duplicates in the array, and the rotation is in the anti-clockwise direction.

************ Behavior *************
Input:
 
nums = [8, 9, 10, 2, 5, 6]
target = 10
 
Output: Element found at index 2
 
 
Input:
 
nums = [9, 10, 2, 5, 6, 8]
target = 5
 
Output: Element found at index 3
**********************************

- Sabemos que o elemento do meio sempre divide o array em dois sub arrays

- E o target so pode estar entre um dos sub arrays

- Pelo menos um dos sub arrays vai ser ordenado

- Se o elemento do meio for o pivot, os dois arrays serao ordenados 

*********************************
"""""
def problem(arr: list, target: int):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        # get the middle of the list
        middle = (low + high) // 2
        
        # if its in the middle return it
        if target == arr[middle]:
            return f"Element found at the index {middle}"
        
        # check if the right side its sorted
        # if its we'll search there, if it isnt we'll search on the leftside
        if arr[middle] < arr[high]:
            
            # Check if the target is between the middle and the end
            if arr[middle] < target <= arr[high]:
                low = middle + 1
            else:
                high = middle - 1
        else: 
            
            # Check if the target is between the begining and the middle
            if arr[low] <= target < arr[middle]:
                high = middle - 1
            else:
                low = middle + 1
    return "Element not found"

resultado = problem([9, 10, 2, 5, 6, 8], 5)
print(resultado)