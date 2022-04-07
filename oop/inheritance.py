import random


class DictOfShortKeys(dict):
    MAX_KEY_LENGTH = 6

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Only string keys are accepted")
        if len(key) > self.MAX_KEY_LENGTH:
            raise ValueError(
                f"Key length is over key length limit: {len(key)} > {self.MAX_KEY_LENGTH}",
            )
        super().__setitem__(key, value)


# short_key_dictionary = DictOfShortKeys()
# short_key_dictionary["This is too long name"] = "test"
# short_key_dictionary["Pesho"] = "Good name"


class OddsOnly(list):
    def append(self, item: int) -> None:
        if item % 2 != 0:
            super().append(item)
            return
        raise
        # raise ValueError("Only odd ints are acceptable")


class EvensOnly(list):
    def append(self, item: int) -> None:
        if item % 2 == 0:
            super().append(item)
            return
        raise ValueError("Only even ints are acceptable")


# evens_only = EvensOnly()
# while len(evens_only) < 100:
#     random_integer = random.randint(1, 100)
#     try:
#         evens_only.append(random_integer)
#     except ValueError:
#         continue
