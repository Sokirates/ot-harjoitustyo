import pygame
from entities.dice import Dice
from ui.game_view import *


def main():

    pygame.init()
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Yatzy")

    game_running = False
    clock = pygame.time.Clock()

    font_large = pygame.font.SysFont("Arial", 36)
    font_small = pygame.font.SysFont("Arial", 24)

    draw_start_screen(screen, font_large, font_small, width)

    while True:
        for event in pygame.event.get():
            if not game_running:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        dice1 = Dice(50, 50)
                        dice2 = Dice(150, 50)
                        dice3 = Dice(250, 50)
                        dice4 = Dice(350, 50)
                        dice5 = Dice(450, 50)
                        draw_game_screen(screen, font_small, dice1, dice2, dice3, dice4, dice5)
                        game_running = True
                    elif event.key == pygame.K_1:
                        draw_instructions_screen(
                            screen, font_large, font_small, width)
                    elif event.key == pygame.K_ESCAPE:
                        quit_game()
                    elif event.key == pygame.K_2:
                        draw_start_screen(screen, font_large, font_small, width)
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        dice1.roll()
                        dice2.roll()
                        dice3.roll()
                        dice4.roll()
                        dice5.roll()
                        draw_game_screen(screen, font_small, dice1, dice2, dice3, dice4, dice5)
                        pygame.display.flip()    
                    elif event.key == pygame.K_ESCAPE:
                        quit_game()

        clock.tick(80)


if __name__ == "__main__":
    main()
