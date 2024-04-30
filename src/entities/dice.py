import random
import pygame


class Dice:
    def __init__(self, x=0, y=0, size=70):
        self.x = x
        self.y = y
        self.size = size
        self.value = 0
        self.locked = False
        self.points = {"ones" : None, 
                       "twos" : None, 
                       "threes" : None, 
                       "fours" : None, 
                       "fives" : None, 
                       "sixes":None,
                       "pair":None, 
                       "two_pairs":None, 
                       "three_of_a_kind":None, 
                       "four_of_a_kind" : None, 
                       "small_straight" : None, 
                       "large_straight" : None, 
                       "full_house" : None, 
                       "chance" : None, 
                       "yatzy" : None}


    def roll(self):
        self.value = random.randint(1, 6)

    def draw(self, screen, font):
        pygame.draw.rect(screen, (0, 0, 0),
                         (self.x, self.y, self.size, self.size), 2)
        if self.locked:
            dice_text = font.render(str(self.value), True, (255, 0, 0))
        else:
            dice_text = font.render(str(self.value), True, (0, 0, 0))
        screen.blit(dice_text, (self.x + self.size // 2 - dice_text.get_width() // 2,
                                self.y + self.size // 2 - dice_text.get_height() // 2))