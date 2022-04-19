from enum import Enum


class MergeRequestException(Exception):
    pass


class MergeRequestStatus(Enum):
    APPROVED = "approved"
    REJECTED = "rejected"
    PENDING = "pending"
    OPEN = "open"
    CLOSED = "closed"


class MergeRequest:
    def __init__(self):
        self._context = {
            "upvotes": set(),
            "downvotes": set(),
        }
        self._status = MergeRequestStatus.OPEN

    def close(self):
        self._status = MergeRequestStatus.CLOSED

    def _cannot_vote_if_closed(self):
        if self._status == MergeRequestStatus.CLOSED:
            raise MergeRequestException("can't vote on closed merge request")

    @property
    def status(self):
        """
        If MergeRequest have downvotes, then the status is Rejected.
        If MergeRequest have more or 2 upvotes, then the status is Approved.
        In other cases status should be Pending
        :return:
        """
        from testing.merge_request.acceptance_threshold import AcceptanceThreshold

        if self._status == MergeRequestStatus.CLOSED:
            return self._status
        return AcceptanceThreshold(self._context).status()

    def upvote(self, by_user):
        self._cannot_vote_if_closed()

        self._context["downvotes"].discard(by_user)
        self._context["upvotes"].add(by_user)

    def downvote(self, by_user):
        self._cannot_vote_if_closed()

        self._context["downvotes"].add(by_user)
        self._context["upvotes"].discard(by_user)
