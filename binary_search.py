# classic implementation of a binary search
def binary_search(list, item):
    left = 0
    right = len(list) - 1 
        
    while left <= right:
        middle = int((left + right) / 2)
        
        if(list[middle] == item):
            return middle
        elif (list[middle] > item):
            right = middle - 1
        else: 
            left = middle + 1
    return -1 
        
# nb_list = [3, 5, 4, 9, 7, 4, 6]
# sorted_list = sorted(nb_list)
# item = 7
# result = binary_search(sorted_list, item)
# # print(result)

def recursion_binary_search(array, target, low, high):
    low = 0
    high = len(array) - 1
    
    while low <= high:
        middle = (low + high) / 2
        
        if(array[middle] == target):
            return middle
        elif (array[middle] > target):
            return recursion_binary_search(array, target, low, middle - 1)
        else: 
            return recursion_binary_search(array, target, middle + 1, high)
    return -1
        
nb_list = [3, 5, 4, 9, 7, 4, 6]
sorted_list = sorted(nb_list)
item = 7
result = binary_search(sorted_list, item)
print(sorted_list)
print(result)

"""
Alice has some cards with numbers written on them. She arranges the cards in decreasing order,
and lays them out face down in a sequence on a table.She challenges Bob to pick out the card
containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.
"""
# Linear search aproach 
def locate_cards(cards, query):
    position = 0
    
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1    
    return -1

# list_cards = []
# nb_query = 5
# result = locate_cards(list_cards, nb_query)
# print(result)

