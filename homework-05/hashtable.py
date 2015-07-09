#!/usr/bin/env python
import os
import hashlib
import logging
import sys
sys.path.append("../shared/")
import utils
log = utils.create_logger(__file__)
log.setLevel(logging.DEBUG)

def process(targets, filename):
    integers = {}
    for x in utils.read_integer_file(filename):
        integers.__setitem__(x, 1 + integers.get(x, 0))

    results = [0] * len(targets)
    for index, current in enumerate(targets):
        found = False
        for y in integers:
            value = current - y
            if value in integers:
                if value == y and integers.get(value) < 2:
                    continue
                results[index] = 1
                break
    return "".join([str(x) for x in results])

if __name__== "__main__":
    targets = [231552, 234756, 596873, 648219, 726312, 981237, 988331, 1277361, 1283379]
    print process(targets, "input/HashInt.txt")