import unittest

from oop.stats_list import StatsList


class TestValidInputs(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.stats = StatsList([1, 2, 2, 3, 3, 4])

    def test_mean(self):
        """Test mean functionality of StatsList."""
        self.assertEqual(self.stats.mean(), 2.5)

    def test_median(self):
        self.assertEqual(self.stats.median(), 2.5)
        self.stats.append(4)
        self.assertEqual(self.stats.median(), 3)

    def test_stats_elements_count(self):
        """Test count changes."""

        # Ensure that we start from initial state
        self.assertEqual(len(self.stats), len([1, 2, 2, 3, 3, 4]))

        self.stats.append(22)

        self.assertNotEqual(len(self.stats), len([1, 2, 2, 3, 3, 4]))
