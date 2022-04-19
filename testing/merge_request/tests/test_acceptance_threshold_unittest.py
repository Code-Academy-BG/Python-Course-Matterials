import unittest

from testing.merge_request.acceptance_threshold import AcceptanceThreshold
from testing.merge_request.merge_request import MergeRequestStatus


class AcceptanceThresholdTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture_data = (
            (
                {"downvotes": set(), "upvotes": set()},
                MergeRequestStatus.PENDING,
            ),
            (
                {"downvotes": set(), "upvotes": {"Pesho"}},
                MergeRequestStatus.PENDING,
            ),
            (
                {"downvotes": "Georgi", "upvotes": set()},
                MergeRequestStatus.REJECTED,
            ),
            (
                {"downvotes": set(), "upvotes": {"Tsvetomir", "Angel", "Ani"}},
                MergeRequestStatus.APPROVED,
            ),
        )

    def test_status_resolution(self):
        for context, expected in self.fixture_data:
            with self.subTest(context=context):
                print(f"Test with {context}, having expected: {expected}")
                status = AcceptanceThreshold(context).status()
                self.assertEqual(status, expected)
