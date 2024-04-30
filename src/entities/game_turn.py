import pygame
from .dice import Dice

class GameTurn:
    """
    Luokka yhdelle pelivuorolle
    """
    def __init__(self):
        """
        Tässä ylläpidetään noppaoliot ja jäljellä olevat heittovuorot
        """
        self.throws_left = 3
        self.dices = [Dice(i*100 + 50, 50) for i in range(5)]

    def throw_dices(self):
        """
        Lukitsemattomien noppien heittäminen
        """
        self.throws_left -= 1

        for dice in self.dices:
            if not dice.locked:
                dice.roll()

    def lock_dice(self, event):
        """
        Käyttäjän valitseman nopan lukitseminen
        """
        if event.key == pygame.K_RETURN: # pylint: disable=no-member
            x, y = pygame.mouse.get_pos()
            for dice in self.dices:
                if dice.x <= x <= dice.x + dice.size and dice.y <= y <= dice.y + dice.size:
                    dice.locked = not dice.locked  # Vaihda nopan lukitusasetus
