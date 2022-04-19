import pytest

from testing.merge_request.merge_request import MergeRequest, MergeRequestStatus, \
    MergeRequestException


def test_simple_rejected():
    merge_request = MergeRequest()
    merge_request.downvote("Georgi")
    assert merge_request.status == MergeRequestStatus.REJECTED


def test_just_created_is_pending():
    assert MergeRequest().status == MergeRequestStatus.PENDING


def test_pending_awaiting_review():
    merge_request = MergeRequest()
    merge_request.upvote("Ani")
    assert merge_request.status == MergeRequestStatus.PENDING


def test_cannot_upvote_on_closed_merge_request():
    merge_request = MergeRequest()
    merge_request.close()
    pytest.raises(MergeRequestException, merge_request.upvote, "Pesho")


@pytest.fixture
def rejected_mr():
    merge_request = MergeRequest()
    merge_request.downvote("Georgi")
    merge_request.upvote("Pesho")
    merge_request.upvote("Angel")
    merge_request.downvote("Tsvetomir")
    return merge_request


def test_simple_rejected_second(rejected_mr):
    assert rejected_mr.status == MergeRequestStatus.REJECTED


if __name__ == "__main__":
    pytest.main()
