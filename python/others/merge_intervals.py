

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Sort the interval by their starting points. Compare the ending point of current interval with
    next examining interval to determine if we can merge them
    :param intervals: list of intervals
    :return: merged interval
    """
    if intervals is None or len(intervals) == 1:
        return intervals

    intervals = sorted(intervals, key=lambda a: a[0])

    output = [];

    for interval in intervals:
        if not output or output[-1][1] < interval[0]:
            output.append(interval)
        else:
            output[-1][1] = max(output[-1][1], interval[1])

    return output
