from enum import Enum


class MergeRequestStatus(Enum):
    APPROVED = "approved"
    REJECTED = "rejected"
    PENDING = "pending"


class MergeRequest:
    def __init__(self):
        self._context = {
            "upvotes": set(),
            "downvotes": set(),
        }

    @property
    def status(self):
        """
        If MergeRequest have downvotes, then the status is Rejected.
        If MergeRequest have more or 2 upvotes, then the status is Approved.
        In other cases status should be Pending
        :return:
        """
        return

    def upvote(self, by_user):
        pass

    def downvote(self, by_user):
        pass
