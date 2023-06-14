#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    Returns the weighted average of all integer tuples.
    """
    if not my_list:
        return 0

    total_weighted_sum = 0
    total_weight = 0

    for score, weight in my_list:
        total_weighted_sum += score * weight
        total_weight += weight

    if total_weight == 0:
        return 0

    return total_weighted_sum / total_weight
