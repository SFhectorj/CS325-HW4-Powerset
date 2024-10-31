def powerset(inputSet):
    """
    :param inputSet:
    :return:
    """
    # This list will hold all subsets
    result = []
    return result

def all_subsets(tracker, current_subset, inputSet, result):
    # Base case: When the tracker reaches zero, all elements have been processed.
    if tracker < 0:
        # Copy the current subset to the final result.
        result.append(current_subset[:])
        return