#!/usr/bin/env python
import os
import logging
import sys
sys.path.append("../shared/")
import utils
log = utils.create_logger(__file__)
# #log.setLevel(logging.DEBUG)
log.setLevel(logging.INFO)

# naive
# def find_inversions(integers):
#     count = 0
#     for i, j in list(enumerate(integers)):
#         i += 1
#         for k in integers[i:]:
#             if j > k:
#                 count += 1
#     return count

def find_inversions(integers):
    count = 0
    remaining = sorted(integers)
    for i in integers:
        count += remaining.index(i)
        remaining.remove(i)
    return count

def process(filename):
    integers = utils.read_integer_file(filename)
    return find_inversions(integers)

if __name__== "__main__":
    print process("input/IntegerArray.txt")