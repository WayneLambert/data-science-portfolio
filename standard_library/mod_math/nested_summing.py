from decimal import Decimal


def sum_all(list_to_sum: float) -> float:
    """ Computes the sum of nested list items """
    return Decimal(sum(sum(item) for item in list_to_sum))


sum_of_all_values = sum_all([[1, 2], [3], [4, 5, 6]])
print(sum_of_all_values)
