import unittest
from src.entities.dice import Dice
import random


class TestDice(unittest.TestCase):
    def setUp(self):
        self.dice = Dice()

    def test_roll(self):
        random.seed(1)
        self.dice.roll()

        self.assertEqual(self.dice.value, 2)

if __name__ == "__main__":
    unittest.main()
