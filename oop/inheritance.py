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


short_key_dictionary = DictOfShortKeys()
short_key_dictionary["This is too long name"] = "test"
short_key_dictionary["Pesho"] = "Good name"


class OddsOnly(list):
    def append(self, item) -> None:
        if item % 2 != 0:
            super().append(item)
            return
        raise ValueError("Only odd ints are acceptable")
