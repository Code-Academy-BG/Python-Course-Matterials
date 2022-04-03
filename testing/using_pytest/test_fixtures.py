import pytest


class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


# Arrange
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)

    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)


"""
Fixtures can request other fixtures

One of pytest’s greatest strengths is its extremely flexible fixture system. 
It allows us to boil down complex requirements for tests into more simple and organized functions, 
where we only need to have each one describe the things they are dependent on. 
We’ll get more into this further down, but for now, here’s a quick example to demonstrate how 
fixtures can use other fixtures:
"""


# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order(first_entry):
    return [first_entry]


def test_string(order):
    # Act
    order.append("b")

    # Assert
    assert order == ["a", "b"]


"""A test/fixture can request more than one fixture at a time."""


# Arrange
@pytest.fixture
def entry_a():
    return "a"


# Arrange
@pytest.fixture
def entry_two():
    return 2


# Arrange
@pytest.fixture
def order(entry_a, entry_two):
    return [entry_a, entry_two]


# Arrange
@pytest.fixture
def expected_list():
    return ["a", 2, 3.0]


def test_multi_fixtures(order, expected_list):
    # Act
    order.append(3.0)

    # Assert
    assert order == expected_list


"""Fixtures can be requested more than once per test (return values are cached)."""


# Arrange
@pytest.fixture
def first_entry_a():
    return "a"


# Arrange
@pytest.fixture
def order():
    return []


# Act
@pytest.fixture
def append_first(order, first_entry):
    return order.append(first_entry)


def test_string_only(append_first, order, first_entry):
    # Assert
    assert order == [first_entry]


"""
If a requested fixture was executed once for every time it was requested during a test, then this 
test would fail because both append_first and test_string_only would see order as an empty list 
(i.e. []), but since the return value of order was cached (along with any side effects executing it 
may have had) after the first time it was called, both the test and append_first were referencing 
the same object, and the test saw the effect append_first had on that object.
"""


"""Autouse fixtures (fixtures you don’t have to request)."""


@pytest.fixture
def first_entry_autouse():
    return "a"


@pytest.fixture
def order_autouse(first_entry):
    return []


@pytest.fixture(autouse=True)
def append_first_autouse(order, first_entry):
    return order.append(first_entry)


def test_string_only_autouse(order, first_entry):
    assert order == [first_entry]


def test_string_and_int_autouse(order, first_entry):
    order.append(2)
    assert order == [first_entry, 2]
