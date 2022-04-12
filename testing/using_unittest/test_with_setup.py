import unittest


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


class FruitSaladTests(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.salad = FruitSalad(Fruit("Banana"), Fruit("Apple"))

    def test_salad_fruits_are_cubed(self):
        self.assertTrue(all(fruit.cubed for fruit in self.salad.fruit))

    def test_fruits_count(self):
        self.assertEqual(len(self.salad.fruit), 2)


if __name__ == "__main__":
    unittest.main()
