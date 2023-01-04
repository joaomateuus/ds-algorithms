# def locate_cards(cards, query):
#     position = 0
    
#     while position < len(cards):
#         if cards[position] == query:
#             return position
#         position += 1    
#     return -1

# list_cards = []
# nb_query = 5
# result = locate_cards(list_cards, nb_query)
# print(result)

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
        
nb_list = [3, 5, 4, 9, 7, 4, 6]
sorted_list = sorted(nb_list)
item = 7
result = binary_search(sorted_list, item)
print(result)

