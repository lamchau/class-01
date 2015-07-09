#!/usr/bin/env python
import unittest
import inversions

test_cases = [
    ("0.txt", 0),
    ("1.txt", 1),
    ("2.txt", 2),
    ("3.txt", 3),
    ("4.txt", 4),
    ("5.txt", 5)]

class TestFiles(unittest.TestCase):
    def _testFile(self, filename, expected):
        count = inversions.process("test-cases/%s" % filename)
        self.assertEqual(count, expected)

for filename, expected in test_cases:
    def test(filename, expected):
        return lambda self: self._testFile(filename, expected)
    
    setattr(TestFiles, "test_file_%s" % filename, test(filename, expected))

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity = 2)
    unittest.main(testRunner = runner)

