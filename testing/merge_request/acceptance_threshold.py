from testing.merge_request.merge_request import MergeRequestStatus


class AcceptanceThreshold:
    UPVOTES_TO_APPROVE = 2

    def __init__(self, merge_request_context: dict, upvotes_to_approve=UPVOTES_TO_APPROVE):
        self._context = merge_request_context
        self.upvotes_to_approve = upvotes_to_approve

    def status(self):
        if self._context["downvotes"]:
            return MergeRequestStatus.REJECTED
        elif len(self._context["upvotes"]) >= self.upvotes_to_approve:
            return MergeRequestStatus.APPROVED
        return MergeRequestStatus.PENDING
