import unittest


def average(seq):
    return sum(seq) / len(seq)


class TestAverage(unittest.TestCase):
    def test_zero(self):
        self.assertRaises(ZeroDivisionError, average, [])

    def test_with_zero(self):
        with self.assertRaises(ZeroDivisionError):
            average([])

    def test_non_empty_seq(self):
        self.assertEqual(average([1, 2, 3, 4]), 2.5)


if __name__ == "__main__":
    unittest.main()
