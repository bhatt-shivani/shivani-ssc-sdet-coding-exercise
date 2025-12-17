"""
This module provides a function to remove duplicates from a list,
while preserving the original order of elements.
"""
def remove_duplicates(lst) -> list:
    """
    Removes duplicates from the given list, preserving the original
    order of the first occurences.

    Args: 
        lst(list):  A list of elements, which may contain duplicates.

    Returns:
        list: A new list with duplicates removed, preserving the original order.
    Raises:
        TypeError: If the input is not a list
    Time Complexity:
        O(n), where n is the length of the list, since the 'set' operations
        are average O(1) in complexity.
    """

    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    # Declare a set to keep track of seen elements
    seen = set()
    # Use filter and set.add() to preserve order and remove duplicates.
    # Note: List comprehension is typically used in Python for such tasks,
    # which is why I used it here as well.
    return list(filter(lambda x: not (x in seen or seen.add(x)), lst))


# Alternate solution using a loop (not using list comprehension):
# This removes duplicates as well, but in terms of readibility:
# seen = set()
# result = []
# for item in lst:
#   if item not in seen:
#       result.append(item)
#       seen.add(item)
# return result
