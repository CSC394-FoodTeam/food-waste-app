import unittest

def sum(a, b):
    return a + b

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)
        self.assertEqual(sum(-1, -1), -2)
        self.assertEqual(sum(0, 0), 0)

if __name__ == '__main__':
    unittest.main()