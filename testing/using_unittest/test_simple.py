import unittest


def func(x: int):
    return x + 1


class FuncTests(unittest.TestCase):
    def test_success_answer(self):
        self.assertEqual(func(4), 5, msg="Success message")

    def test_failing_answer(self):
        self.assertEqual(func(3), 5, msg="Fail message")


if __name__ == "__main__":
    unittest.main()
