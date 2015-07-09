#!/usr/bin/env python
import unittest
import quicksort

test_cases = [
    ("array0.txt", (64, 60, 55)),
    ("array1.txt", (253, 253, 66)),
    ("array2.txt", (1596, 1596, 228)),
    ("array3.txt", (576, 669, 636)),
    ("array4.txt", (237, 235, 172)),
    ("array5.txt", (252, 185, 186)),
    ("array6.txt", (236, 258, 177)),
    ("array7.txt", (213, 199, 180)),
    ("array8.txt", (231, 206, 192)),
    ("array9.txt", (282, 310, 214)),
    ("array10.txt", (191, 232, 206))]

class TestFiles(unittest.TestCase):
    def _testFile(self, filename, question, expected):
        count = quicksort.process(question, "test-cases/%s" % filename)
        self.assertEqual(count, expected)

for filename, expected in test_cases:
    first, last, median = expected
    def testFirst(filename, expected_first):
        return lambda self: self._testFile(filename, 1, expected_first)
    def testLast(filename, expected_last):
        return lambda self: self._testFile(filename, 2, expected_last)
    def testMedian(filename, expected_median):
        return lambda self: self._testFile(filename, 3, expected_median)
    setattr(TestFiles, "test_file_%s" % filename, testFirst(filename, first))
    setattr(TestFiles, "test_file_%s" % filename, testLast(filename, last))
    setattr(TestFiles, "test_file_%s" % filename, testMedian(filename, median))

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity = 2)
    unittest.main(testRunner = runner)

