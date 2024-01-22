# RiscV-coding-challenge
Pick one:

1.Write a 20 line program in OCaml that does something interesting.

2.Write a Javascript, Python, or OCaml program that:
- accepts a list of integers
- emits an error message if the list is not a multiple of 10 in length
- returns or prints a list of integers based on the input list, but with items at positions which are a multiple of 2 or 3 removed

**Host your program at a public git-based repository and include robust testing for your program.**

## Steps to resolve the problem

### 1. My choice
I decide to pick the second problem. And choose Python as programming language.

### 2. Pseudo-code


```
    # A function "filter_integer" that filter a list of integer.
    function filter_integer(list):

    #Retrieve the lenght of the list and check wether it's multiple of 10 or not
    if length(inputList) is not a multiple of 10:

        #Print error and exit the program if the list length is not a multiple of 10
        print("Error: The list length must be a multiple of 10.")
        exit

    else
    # A list that will contain filtered integer
    filtered_integer = []

    #For each item which position are not multiple of 2 or 3, add it to filtered_integer
    for position from 0 to length(list) - 1:
        if index is not a multiple of 2 or index is not a multiple of 3:
            add list[position] to filtered_integer

    print("Filtered Integer:", filtered_integer)
    return filtered_integer


```

### 3. Testing

Clone this repository, open your terminal and run `python ./test_filter_integer.py`

### 4. Space and time complexity

The time complexity of the function is O(n) and the space complexity is also O(n), with `n` is the size of the input list.
