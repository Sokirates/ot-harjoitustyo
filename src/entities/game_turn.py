from .dice import Dice
import pygame

class GameTurn:
    def __init__(self):
        self.throws_left = 3
        self.points = {
            "ones" : None,
            "twos" : None, 
            "threes" : None, 
            "fours" : None, 
            "fives" : None, 
            "sixes": None,
            "pair": None, 
            "two_pairs": None, 
            "three_of_a_kind": None, 
            "four_of_a_kind" : None, 
            "small_straight" : None, 
            "large_straight" : None, 
            "full_house" : None, 
            "chance" : None, 
            "yatzy" : None
        }
        self.dices = [Dice(i*100 + 50, 50) for i in range(5)]
    
    def throw_dices(self):
        if self.throws_left <= 0:
            return None
        self.throws_left -= 3
        
        for dice in self.dices:
            dice.roll()
    
    def lock_dice(self, event):
        if event.key == pygame.K_RETURN: # pylint: disable=no-member  
            x, y = pygame.mouse.get_pos()
            for dice in self.dices:
                if dice.x <= x <= dice.x + dice.size and dice.y <= y <= dice.y + dice.size:
                    dice.locked = not dice.locked  # Vaihda nopan lukitusasetus        
    
if __name__ == "__main__":
    g = GameTurn()
    g.throw_dices()
