def powerset(input_set):
    """
    :return:
    """
    # This list will hold all subsets
    result = []
    return result


def all_subsets(tracker, current_subset, input_set, result):
    # Base case: When the tracker reaches zero, all elements have been processed.
    if tracker < 0:
        # Copy the current subset to the final result.
        # The copy must include all nested objects.
        result.append(current_subset[:])
        return
