import pygame
from services.gameloop import start_game # pylint: disable=import-error


def main():
    """
    Pääfunktio, joka käynnistää pelin.
    """
    pygame.init() # pylint: disable=no-member
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Yatzy")

    start_game(screen, width)


if __name__ == "__main__":
    main()
