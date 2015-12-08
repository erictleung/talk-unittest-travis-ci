#!/usr/bin/env python

import unittest

def fun(x):
    return x + 1

class TestAddingMethod(unittest.TestCase):
    def test_three(self):
        self.assertEqual(fun(3), 4)
    def test_four(self):
        self.assertEqual(fun(4), 5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAddingMethod)
    unittest.TextTestRunner(verbosity=2).run(suite)
