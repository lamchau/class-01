#!/usr/bin/env python
import os
import sys
from operator import itemgetter, attrgetter
import unittest
import karger

test_file_dir = "test-cases"

class TestFiles(unittest.TestCase):
    def _testFile(self, filename, expected_min_cut):
        path = os.path.join(test_file_dir, filename)
        min_cut = karger.process(path)
        self.assertEqual(min_cut, expected_min_cut)

# def size_sorter(item):
#     filename, target = item
#     path = os.path.join(test_file_dir, filename)
#     return os.path.getsize(path)

test_cases = [
    ("adjList01m1.txt", 1),
    ("adjList02m2.txt", 2),
    ("adjList03m1.txt", 1),
    ("adjList04m1.txt", 1),
    ("adjList05m2.txt", 2),
    ("adjList06m3.txt", 3),
    ("adjList07m1.txt", 1),
    ("adjList08m1.txt", 1),
    ("adjList09m1.txt", 1),
    ("adjList10m2.txt", 2),
    ("n3m3_2.txt", 2),
    ("n3m5_2.txt", 2),
    ("n4m5_2.txt", 2),
    ("n4m6_3.txt", 3),
    ("n5m5_2.txt", 2),
    ("n8m14_2.txt", 2),
    ("test0_m3.txt", 3),
    ("test0_m5.txt", 5),
    ("test1.2.txt", 2),
    ("test1bm3.txt", 3),
    ("test1_m5.txt", 5),
    ("test1_m6.txt", 6),
    ("test2.4.txt", 4),
    ("test2b2.txt", 2),
    ("test2_m5.txt", 5),
    ("test2_m7.txt", 7),
    ("test3.1.txt", 1),
    ("test3_m3.txt", 3),
    ("test4.3.txt", 3),
    ("test4_m5.txt", 5),
    ("test5_m4.txt", 4),
    ("test6_m4.txt", 4),
    ("test7_m4.txt", 4),
    ("test8_m3.txt", 3),
    ("test9_m4.txt", 4)]

#test_cases = sorted(test_cases, key=size_sorter)

for filename, expected_min_cut in test_cases:
    def test(filename, min_cut):
        return lambda self: self._testFile(filename, min_cut)
    test_filename = "test_file_%s" % filename
    test_case = test(filename, expected_min_cut)
    setattr(TestFiles, test_filename, test_case)

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity = 2)
    unittest.main(testRunner = runner)
