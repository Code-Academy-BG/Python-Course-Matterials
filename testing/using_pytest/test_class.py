class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")


"""
Grouping tests in classes can be beneficial for the following reasons:

Test organization

Sharing fixtures for tests only in that particular class

Applying marks at the class level and having them implicitly apply to all tests

Something to be aware of when grouping tests inside classes is that each test has a unique instance
of the class. Having each test share the same class instance would be very detrimental to test 
isolation and would promote poor test practices. This is outlined below:
"""


class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1
