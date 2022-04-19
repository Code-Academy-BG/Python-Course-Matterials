import pytest

from testing.merge_request.acceptance_threshold import AcceptanceThreshold
from testing.merge_request.merge_request import MergeRequestStatus


@pytest.mark.parametrize("context, expected_status", (
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
))
def test_status_resolution(context, expected_status):
    assert AcceptanceThreshold(context).status() == expected_status
