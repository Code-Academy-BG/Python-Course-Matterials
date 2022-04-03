import unittest


def func(x):
    return x + 1


class FuncTests(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(func(3), 5)


if __name__ == "__main__":
    unittest.main()
