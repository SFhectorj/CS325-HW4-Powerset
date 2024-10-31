def powerset(input_set):
    """
    :return:
    """
    # This list will hold all subsets
    result = []
    return result


def all_subsets(current_element, current_subset, input_set, result):
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

    # Second Option: Exclude the element and continue on
    all_subsets(current_element - 1, current_subset, input_set, result)


