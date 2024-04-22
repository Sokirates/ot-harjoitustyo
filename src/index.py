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

    game_loop(screen, game_running, clock, font_small, font_large, width)

def handle_game_not_running_events(event, screen, font_large, font_small, width, game_running):
    if event.key == pygame.K_SPACE:
        dices = [Dice(i*100 + 50, 50) for i in range(5)]

        draw_game_screen(screen, font_small, dices)
        game_running = True
        
    elif event.key == pygame.K_1:
        draw_instructions_screen(screen, font_large, font_small, width)
    elif event.key == pygame.K_ESCAPE:
        quit_game()
    elif event.key == pygame.K_2:
        draw_start_screen(screen, font_large, font_small, width)
    return game_running, dices

def handle_game_running_events(event, screen, font_small, dices):
    if event.key == pygame.K_SPACE:
        for dice in dices:
            dice.roll()
        draw_game_screen(screen, font_small, dices)
        pygame.display.flip()
        
    elif event.key == pygame.K_1:
        draw_ones_points(screen, font_small, dices)
        pygame.display.flip()
    
    elif event.key == pygame.K_2:
        draw_twos_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_3:
        draw_threes_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_4:
        draw_fours_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_5:
        draw_fives_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_6:
        draw_sixes_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_q:
        draw_pair_points(screen, font_small, dices)
        pygame.display.flip()
    
    elif event.key == pygame.K_w:
        draw_two_pairs_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_e:
        draw_three_of_a_kind_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_r:
        draw_four_of_a_kind_points(screen, font_small, dices)
        pygame.display.flip()
    
    elif event.key == pygame.K_t:
        draw_small_straight_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_y:
        draw_large_straight_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_u:
        draw_full_house_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_i:
        draw_chance_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_o:
        draw_yatzy_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_ESCAPE:
        quit_game()

def game_loop(screen, game_running, clock, font_small, font_large, width):
    while True:
        for event in pygame.event.get():
            if event.type != pygame.KEYDOWN:
                continue

            if not game_running:
                game_running, dices = handle_game_not_running_events(
                    event, screen, font_large, font_small, width, game_running
                )
            else:
                handle_game_running_events(event, screen, font_small, dices)

        clock.tick(80)

if __name__ == "__main__":
    main()
