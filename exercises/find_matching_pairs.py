import itertools


def find_matching_pairs(original_list: list, target_num: int) ->list:
    """
    Returns a list with groupings of 2 element tuples
    that sum to equal the target number.

    Initialise the list object to an empty list depending upon
    whether it is None
    """
    if original_list is None:
        original_list = []

    """
    Convert original list to a filtered list where the numbers
    in the list are all less than or equal to target_num - 1
    """
    filtered_list = list(filter(lambda num: num <= target_num - 1, original_list))

    """
    From the filtered list, create an interator of all of the combinations
    """
    combins = itertools.combinations(filtered_list, 2)

    """
    Loop over the combinations iterator and test whether the 2
    elements equal the target_num. If so, append them to a pairings_list
    """
    pairings_list = []
    for combin in combins:
        if sum(combin) == target_num:
            pairings_list.append(combin)
    return pairings_list


"""
The statements below conduct some sanity checks without using a
testing framework. There are more complete parametrized tests
in another file with more variants
"""
print([sum(test) == 4 for test in find_matching_pairs([1, 2, 3, 4, 5, 6, 7], 4)])
print([sum(test) == 5 for test in find_matching_pairs([1, 2, 3, 4, 5, 6, 7, 8], 5)])
print([sum(test) == 3 for test in find_matching_pairs([1, 2, 3, 4, 5, 6, 7], 3)])
