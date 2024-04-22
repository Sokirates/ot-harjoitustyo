import random
import pygame


class Dice:
    def __init__(self, x=0, y=0, size=70):
        self.x = x
        self.y = y
        self.size = size
        self.value = 0

    def roll(self):
        self.value = random.randint(1, 6)

    def draw(self, screen, font):
        pygame.draw.rect(screen, (0, 0, 0),
                         (self.x, self.y, self.size, self.size), 2)
        dice_text = font.render(str(self.value), True, (0, 0, 0))
        screen.blit(dice_text, (self.x + self.size // 2 - dice_text.get_width() //
                    2, self.y + self.size // 2 - dice_text.get_height() // 2))
