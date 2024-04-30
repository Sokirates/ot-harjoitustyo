import unittest
from src.entities.game_turn import GameTurn
import random

class TestDice(unittest.TestCase):
    def setUp(self):
        self.turn = GameTurn()

    def test_roll(self):
        random.seed(1)
        self.turn.throw_dices()

        test_values = [2, 5, 1, 3, 1]

        for dice, val in zip(self.turn.dices, test_values):
            self.assertEqual(dice.value, val)


if __name__ == "__main__":
    unittest.main()
