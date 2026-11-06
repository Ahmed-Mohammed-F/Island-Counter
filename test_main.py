import unittest
from main import count_islands

class IslandTests(unittest.TestCase):
    def test_three_islands(self):
        self.assertEqual(count_islands([list(x) for x in ["11000", "11000", "00100", "00011"]]), 3)
    def test_no_islands(self):
        self.assertEqual(count_islands([list("000"), list("000")]), 0)
    def test_all_land(self):
        self.assertEqual(count_islands([list("11"), list("11")]), 1)
    def test_diagonal_not_connected(self):
        self.assertEqual(count_islands([list("10"), list("01")]), 2)
    def test_empty(self):
        self.assertEqual(count_islands([]), 0)

if __name__ == '__main__':
    unittest.main()
