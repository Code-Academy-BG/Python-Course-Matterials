from unittest import TestCase

from testing.merge_request.merge_request import MergeRequest, MergeRequestStatus, \
    MergeRequestException


class MergeRequestStatusTests(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.merge_request = MergeRequest()

    def test_simple_rejected(self):
        # Initial should be pending
        self.assertEqual(self.merge_request.status, MergeRequestStatus.PENDING)
        self.merge_request.downvote("Georgi")
        # After downvote merge_request is Rejected
        self.assertEqual(self.merge_request.status, MergeRequestStatus.REJECTED)

    def test_just_created_is_pending(self):
        # Initial should be pending
        self.assertEqual(self.merge_request.status, MergeRequestStatus.PENDING)

    def test_pending_awaiting_review(self):
        self.merge_request.upvote("Tsvetomir")
        self.assertEqual(self.merge_request.status, MergeRequestStatus.PENDING)

    def test_approved(self):
        self.merge_request.upvote("Tsvetomir")
        self.merge_request.upvote("Pesho")
        self.assertEqual(self.merge_request.status, MergeRequestStatus.APPROVED)

    def test_cannot_upvote_on_closed_merge_request(self):
        self.merge_request.close()
        self.assertRaises(MergeRequestException, self.merge_request.upvote, "Pesho")

    def test_cannot_downvote_on_closed_merge_request(self):
        self.merge_request.close()
        self.assertRaises(MergeRequestException, self.merge_request.downvote, "Georgi")
