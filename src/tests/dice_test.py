import unittest
from src.entities.dice import Dice
import pygame


class TestDice(unittest.TestCase):
    def setUp(self):
        self.dice = Dice()

    def test_roll(self):
        self.dice.roll()
        self.assertIn(self.dice.value, range(1, 7))
    
    def test_draw(self):
        pygame.init()
        screen = pygame.Surface((640, 480))
        font = pygame.font.SysFont("Arial", 24)
        self.dice.draw(screen, font)

        expected_rect = pygame.Rect(self.dice.x, self.dice.y, self.dice.size, self.dice.size)
        self.assertTrue(screen.get_rect().colliderect(expected_rect), "Ei ole näytön sisällä")

        dice_text = str(self.dice.value)
        rendered_text = font.render(dice_text, True, (0, 0, 0))
        text_rect = rendered_text.get_rect(center=expected_rect.center)
        text_rect.topleft = (self.dice.x + self.dice.size // 2 - text_rect.width // 2, self.dice.y + self.dice.size // 2 - text_rect.height // 2)
        self.assertTrue(screen.get_rect().colliderect(text_rect), "Teksti ei ole näytön sisällä")


if __name__ == "__main__":
    unittest.main()