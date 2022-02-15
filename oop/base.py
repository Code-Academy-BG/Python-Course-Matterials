from datetime import datetime
from functools import cached_property


class TimestampMixin:
    @cached_property
    def created_at(self):
        return datetime.now()
