# Binary Search
### Binary search is an efficient algorithm for finding an item from a <strong>sorted list</strong> of items. It works by repeatedly dividing the half portion of the list that can contain the item until you minimize the possible locations to just one.

---
### Imagine you are searching for a person name in a phone book or looking for a word in a dictionary, You could start at the beginning and keep flipping pages until you get the page that the name/word starts with. But you are more likely to open the middle of the book beacause it might be the nearest way to find what you are looking for. And with binary search is the same aproach
---
<br>

# Describing binary search
### The main idea of binary search is to keep track of the current range of reasonble guesses.
### Lets say that Im thinking in a number between 1 and 100. If I guessed 25 and the number is higher after I guessed 80 and the number is lower. We"ll keep in track the range between 26 - 80 that are the reasonble guesses
<br>

![ranges](https://cdn.kastatic.org/ka-perseus-images/91981c0666c061815dd0e9b473ad0570a1803a45.png)
<br>

### In each turn we choose a guess that divides the set of reasonble guesses into two ranges. Eliminating half of the list if the guesses is not correct. For example we were keeping track in the range 26 - 80, the next guess will be 53 ((26 + 80) / 2). If the guess is to high we"ll keep in the track in the range between 26 and 52.
<br>

![ranges](https://cdn.kastatic.org/ka-perseus-images/a376ce2d2746fc126293571121a818f395a97354.png)

<br>

## Basic Implementation
    1 - min = 0 and max = len(list) - 1 
    2 - middle = (min + max) / 2 
    3 - guess = list[middle] 
    4 - if (guess == target) {
        return guess
    } 
    5 - elif (guess < target) {
        min = middle + 1
    } 
    6 - elif (guess > target) {
        max = middle - 1
    }

    7 - We have a new middle, a new try and the loop continuos

<ol>
    <li>
        We set the minimum that is the position zero and the maximum that is the list size -1
    </li>
    <li>
        The middle will be the sum of minimum and maximum divided by two, getting the exacly middle of the list
    </li>
    <li>
        The guess is the middle of the list
    </li>
    <li>
        If you guessed the number, stop. You found it!
    </li>
    <li>
        If the guess is lower, that means that the target is to the right side so we move our minimum value setting it to the middle + 1, slicing the list to the reasonble range
    </li>
    <li>
        If the guess is high, we do the opposite setting the maximum to the middle - 1 
    </li>
</ol>

---





