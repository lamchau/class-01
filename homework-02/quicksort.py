#!/usr/bin/env python
import os
import logging
import sys
sys.path.append("../shared/")
import utils
log = utils.create_logger(__file__)
# #log.setLevel(logging.DEBUG)
log.setLevel(logging.INFO)

# naive (not in place, memory intensive)
# def quick_sort(array):
#     if len(array) < 2:
#         return array
#     pivot = array[0]
#     array.remove(pivot)
#     less = []
#     greater = []
#     for item in array:
#         if item <= pivot:
#             less.append(item)
#         else:
#             greater.append(item)
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# in-place (memory efficient)
def quick_sort(array, left, right):
    global __cmp_count__
    # empty or single item list
    if array and len(array) > 1 and left < right:
        log.debug("%s (size=%d)" % (str(array), len(array)))
        index = partition(array, left, right)
        quick_sort(array, left, index - 1)
        quick_sort(array, index, right)
    return __cmp_count__

def partition(array, left, right):
    global __cmp_count__
    pivot = find_pivot(array, left, right - 1)
    i = left + 1
    for j in xrange(i, right):
        __cmp_count__ += 1
        if array[j] < pivot:
            swap(array, i, j)
            i += 1
    swap(array, left, i - 1)
    return i

def swap(array, i, j):
    if i == j:
        #log.debug("No swap needed, same index (%d)" % i)
        return False
    else:
        log.debug("%d <-> %d" % (i, j))
        array[i], array[j] = array[j], array[i]
        return True    

def find_pivot(array, left, right):
    array_name = "pivot"
    pivot = None
    if __question__ == 1:
        # Question 2.1 (pivot = first element)
        pivot = left
    elif __question__ == 2:
        # Question 2.2 (pivot = final element)
        pivot = right
    elif __question__ == 3:
        # Question 2.3 (Median of 3; left/right)
        median, pivot = find_median(array, left, right)
    
    if pivot is None or pivot < 0:
        raise Exception("Failed to find pivot")
    log.debug(utils.array2str(array, pivot, array_name))
    swap(array, left, pivot)
    return array[left]

def find_median(array, left, right):
    middle = left + ((right - left)/2)
    elements = [(array[x], x) for x in set([left, middle, right])]
    if len(elements) == 3:
        # 'true' median is the middle element
        median, index = sorted(elements)[1]
    else:
        # no median found, use minimum as pivot
        median, index = min(elements)
    # avoid overhead, skip debug logging
    if log.level == logging.DEBUG:
        debug_message = []
        for x, y in elements:
            is_median = median == x
            msg = utils.array2str(array, y, mark=is_median, spacing=8)
            debug_message.append(msg)
        log.debug("\n" + "\n".join(debug_message))
    return (median, index)

def process(question, file):
    global __cmp_count__
    global __question__
    __cmp_count__ = 0
    __question__ = question
    integers = utils.read_integer_file(file)
    quick_sort(integers, 0, len(integers))
    return __cmp_count__

if __name__ == "__main__":
    for q in xrange(1, 4): # 1, 2, 3
        print "Question %d: %d" % (q, process(q, "input/QuickSort.txt"))