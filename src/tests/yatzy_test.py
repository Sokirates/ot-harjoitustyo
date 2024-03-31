import unittest
from yatzy import Dice
import random

class TestDice(unittest.TestCase):
    def setUp(self) -> None:
        self.dice = Dice()
    
    def test_roll(self):
        random.seed(1)
        self.dice.roll()
        self.value(1)

