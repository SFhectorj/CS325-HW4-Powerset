def powerset(input_set):
    """
    This serves as a helper function to recursively call the all_subsets function.
    The goal for this function is to initialize result list, and the current_subsets
    list.
    """
    # This list will hold all subsets
    result = []
    # Initializes the current element to the back of the list  and
    # the current subset to an empty list.
    all_subsets(len(input_set) - 1, [], input_set, result)
    return result


def all_subsets(current_element, current_subset, input_set, result):
    """
    This is a helper function that manages the subsets that will be called by the
    power set function. This function employs the back tracking method by removing the
    previous element from the current subset.
    """
    # Base case: When the tracker reaches zero, all elements have been processed.
    if current_element < 0:
        # Copy the current subset to the final result.
        # The copy must include all nested objects.
        result.append(current_subset[:])
        return

    # First Option: Include the element in the subset
    current_subset.append(input_set[current_element])

    # Recursive call with the next element
    all_subsets(current_element - 1, current_subset, input_set, result)

    # Employ backtracking by removing the last added element.
    current_subset.pop()

    # Second Option: Exclude the element and continue on
    all_subsets(current_element - 1, current_subset, input_set, result)


