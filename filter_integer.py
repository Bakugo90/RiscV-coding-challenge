def filter_integer(list):
    """
    Filters an input list based on specific conditions.

    Parameters:
    - list: The input list of integers.

    Returns:
    - list: A filtered list containing elements at index not multiples of 2 or 3.

    Raises:
    - ValueError: If the length of the input list is not a multiple of 10.
    """

    #Retrieve the lenght of the list and check wether it's multiple of 10 or not
    if len(list) % 10 != 0:

        #Print error and exit the program if the list length is not a multiple of 10
        raise ValueError("Error: The list length must be a multiple of 10.")

    # A list that will contain filtered integer
    filtered_integer = []

    # A littke bit confusing finally, I assume that index == position
    position = 0
    for item in list:

        # Add item to filtered list if item's position is not multiple of 2 and 3
        if position % 2 != 0 and position % 3 != 0:
            filtered_integer.append(item)
        position += 1
    return filtered_integer
