import unittest
from src.entities.points import PointsCounter
from src.entities.dice import Dice

class TestDice(unittest.TestCase):
    def setUp(self):
        self.dices = [Dice(), Dice(), Dice(), Dice(), Dice(), Dice()]
        for i in range(6):
            self.dices[i].value = i + 1
        
        self.dices_1 = [Dice(), Dice(), Dice(), Dice(), Dice()]
        for i in range(5):
            self.dices_1[i].value = 1
        self.dices_1[0].value = 2
        self.dices_1[1].value = 2

        self.dices_2 = [Dice(), Dice(), Dice(), Dice(), Dice()]
        for i in range(5):
            self.dices_2[i].value = 1

        self.dices_3 = [Dice(), Dice(), Dice(), Dice(), Dice()]
        for i in range(5):
            self.dices_3[i].value = i + 1
        
        self.dices_4 = [Dice(), Dice(), Dice(), Dice(), Dice()]
        for i in range(5):
            self.dices_4[i].value = i + 2
        
        self.dices_5 = [Dice(), Dice(), Dice(), Dice(), Dice()]
        for i in range(5):
            self.dices_5[i].value = 1
        self.dices_5[3] = 2
        self.dices_5[4] = 3

        self.scoreboard = {
            "ones": "3",
            "twos": "4",
            "threes": "",
            "fours": "8",
            "fives": "15",
            "sixes": "",
            "subtotal": "",
            "bonus": "",
            "pair": "",
            "two_pairs": "",
            "three_of_a_kind": "",
            "four_of_a_kind": "",
            "small_straight": "",
            "large_straight": "",
            "full_house": "",
            "chance": "",
            "yatzy": "",
            "total": ""
        }

        self.scoreboard_1 = {
            "ones": "3",
            "twos": "6",
            "threes": "9",
            "fours": "12",
            "fives": "15",
            "sixes": "18",
            "subtotal": "63",
            "bonus": "",
            "pair": "10",
            "two_pairs": "20",
            "three_of_a_kind": "",
            "four_of_a_kind": "16",
            "small_straight": "",
            "large_straight": "",
            "full_house": "25",
            "chance": "18",
            "yatzy": "50",
            "total": ""
        }

    def test_calculate_ones(self):
        self.assertEqual(PointsCounter.calculate_ones(self.dices), 1)
    
    def test_calculate_twos(self):
        self.assertEqual(PointsCounter.calculate_twos(self.dices), 2)
    
    def test_calculate_threes(self):
        self.assertEqual(PointsCounter.calculate_threes(self.dices), 3)

    def test_calculate_fours(self):
        self.assertEqual(PointsCounter.calculate_fours(self.dices), 4)

    def test_calculate_fives(self):
        self.assertEqual(PointsCounter.calculate_fives(self.dices), 5)
    
    def test_calculate_sixes(self):
        self.assertEqual(PointsCounter.calculate_sixes(self.dices), 6)

    def test_calculate_pair(self):
        self.assertEqual(PointsCounter.calculate_pair(self.dices_1), 4)
        self.assertEqual(PointsCounter.calculate_pair(self.dices_3), 0)

    def test_calculate_two_pairs(self):
        self.assertEqual(PointsCounter.calculate_two_pairs(self.dices_1), 6)
        self.assertEqual(PointsCounter.calculate_two_pairs(self.dices), 0)

    def test_calculate_three_of_a_kind(self):
        self.assertEqual(PointsCounter.calculate_three_of_a_kind(self.dices_1), 3)
        self.assertEqual(PointsCounter.calculate_three_of_a_kind(self.dices), 0)
    
    def test_calculate_four_of_a_kind(self):
        self.assertEqual(PointsCounter.calculate_four_of_a_kind(self.dices_2), 4)
        self.assertEqual(PointsCounter.calculate_four_of_a_kind(self.dices), 0)

    def test_calculate_small_straight(self):
        self.assertEqual(PointsCounter.calculate_small_straight(self.dices_3), 15)
        self.assertEqual(PointsCounter.calculate_small_straight(self.dices_2), 0)

    def test_calculate_large_staright(self):
        self.assertEqual(PointsCounter.calculate_large_straight(self.dices_4), 20)
        self.assertEqual(PointsCounter.calculate_large_straight(self.dices_2), 0)
    
    def test_calculate_full_house(self):
        self.assertEqual(PointsCounter.calculate_full_house(self.dices_1), 7)
        self.assertEqual(PointsCounter.calculate_full_house(self.dices), 0)
        self.assertEqual(PointsCounter.calculate_full_house(self.dices_2), 0)


    def test_calculate_chance(self):
        self.assertEqual(PointsCounter.calculate_chance(self.dices_1), 7)

    def test_calculate_yatzy(self):
        self.assertEqual(PointsCounter.calculate_yatzy(self.dices_2), 50)
        self.assertEqual(PointsCounter.calculate_yatzy(self.dices), 0)

    def test_calculate_subtotal(self):
        self.assertEqual(PointsCounter.calculate_subtotal(self.scoreboard), 30)

    def test_calculate_bonus(self):
        self.assertEqual(PointsCounter.calculate_bonus(self.scoreboard), 0)
        self.assertEqual(PointsCounter.calculate_bonus(self.scoreboard_1), 50)

    def test_calculate_total(self):
        self.assertEqual(PointsCounter.calculate_total(self.scoreboard), 30)
        self.assertEqual(PointsCounter.calculate_total(self.scoreboard_1), 202)
        