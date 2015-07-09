#!/usr/bin/env python
import unittest
import hashtable

test_cases = [
    ("1.txt", ([3, 5, 6, 10], "1110")),
    ("2.txt", ([2, 6, 7], "011")),
    ("3.txt", ([3, 6, 6], "111")),
    ("4.txt", ([3, 5, 6, 10], "1111")),
    ("5.txt", ([0, 0, 0, 0], "0000")),
    ("6.txt", ([-5, 1, 0, 10], "1110")),
    ("7.txt", ([1, 5, 7, 9, 12, 33, 22], "0010001"))]

class TestFiles(unittest.TestCase):
    def _testFile(self, filename, expected):
        targets, result = expected
        result_str = hashtable.process(targets, "test-cases/%s" % filename)
        self.assertEqual(result_str, result)

for filename, expected in test_cases:
    def test(filename, expected):
        return lambda self: self._testFile(filename, expected)
    setattr(TestFiles, "test_file_%s" % filename, test(filename, expected))

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity = 2)
    unittest.main(testRunner = runner)