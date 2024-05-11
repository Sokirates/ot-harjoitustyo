import random
import pygame


class Dice:
    """
    Luokka yksittäiselle nopalle

    Attributes:
            x: Nopan x-koordinaatti peliruudulla.
            y: Nopan y-koordinaatti peliruudulla.
            size: Nopan koko peliruudulla.
            value: Nopan silmäluku.
            locked: onko noppa lukittu vai ei 
    """
    def __init__(self, x=0, y=0, size=70):
        """
        Alustaa nopan.

        Args:
            x: Nopan x-koordinaatti peliruudulla.
            y: Nopan y-koordinaatti peliruudulla.
            size: Nopan koko peliruudulla.
        """
        self.x = x
        self.y = y
        self.size = size
        self.value = 0
        self.locked = False

    def roll(self):
        """
        Nopan heittäminen, asettaen satunnaisesti silmäluvun välillä 1-6.
        """
        self.value = random.randint(1, 6)

    def draw(self, screen, font):
        """
        Nopan piirtäminen peliruudulle.

        Args:
            screen: Peliruutu, johon piirretään nopat
            font: Fontti noppien piirämiseen.
        """
        pygame.draw.rect(screen, (0, 0, 0),
                         (self.x, self.y, self.size, self.size), 2)
        if self.locked:
            dice_text = font.render(str(self.value), True, (255, 0, 0))
        else:
            dice_text = font.render(str(self.value), True, (0, 0, 0))
        screen.blit(dice_text, (self.x + self.size // 2 - dice_text.get_width() // 2,
                                self.y + self.size // 2 - dice_text.get_height() // 2))
