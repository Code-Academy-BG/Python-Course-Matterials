from functools import cached_property


class Singleton:
    instance = None
    _total_score = 0

    def __new__(cls, score, *args, **kwargs):
        if cls.instance is None:
            instance = super().__new__(cls)
            cls.instance = instance
        return cls.instance

    def __init__(self, score):
        self._total_score += score

    @property
    def total_score(self):
        return self._total_score

    @cached_property
    def cached_total_score(self):
        return self._total_score


a = Singleton(5)
print(a.cached_total_score)
b = Singleton(10)
print(b.cached_total_score)

print(id(a), id(b))
print(a.total_score, b.total_score)
