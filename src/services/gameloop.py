import pygame
from ui.game_view import ( # pylint: disable=import-error
    draw_start_screen,
    draw_chance_points,
    draw_fives_points,
    draw_four_of_a_kind_points,
    draw_fours_points,
    draw_full_house_points,
    draw_game_screen,
    draw_instructions_screen,
    draw_large_straight_points,
    draw_ones_points,
    draw_pair_points,
    draw_sixes_points,
    draw_small_straight_points,
    draw_three_of_a_kind_points,
    draw_threes_points,
    draw_two_pairs_points,
    draw_twos_points,
    draw_yatzy_points,
    quit_game
)
from entities.dice import Dice # pylint: disable=import-error


def start_game(screen, width):
    game_running = False
    clock = pygame.time.Clock()

    font_large = pygame.font.SysFont("Arial", 36)
    font_small = pygame.font.SysFont("Arial", 24)

    draw_start_screen(screen, font_large, font_small, width)

    game_loop(screen, game_running, clock, font_small, font_large, width)


def game_loop(screen, game_running, clock, font_small, font_large, width):
    while True:
        for event in pygame.event.get():
            if event.type != pygame.KEYDOWN: # pylint: disable=no-member
                continue

            if not game_running:
                game_running, dices = handle_game_not_running_events(
                    event, screen, font_large, font_small, width, game_running
                )
            else:
                handle_game_running_events(event, screen, font_small, dices)

        clock.tick(80)


def handle_game_not_running_events(event, screen, font_large, font_small, width, game_running):
    dices = None
    if event.key == pygame.K_SPACE: # pylint: disable=no-member
        dices = [Dice(i*100 + 50, 50) for i in range(5)]

        draw_game_screen(screen, font_small, dices)
        game_running = True

    elif event.key == pygame.K_1: # pylint: disable=no-member
        draw_instructions_screen(screen, font_large, font_small, width)
    elif event.key == pygame.K_ESCAPE: # pylint: disable=no-member
        quit_game()
    elif event.key == pygame.K_2: # pylint: disable=no-member
        draw_start_screen(screen, font_large, font_small, width)
    return game_running, dices


def handle_game_running_events(event, screen, font_small, dices):
    if event.key == pygame.K_SPACE: # pylint: disable=no-member
        for dice in dices:
            dice.roll()
        draw_game_screen(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_1: # pylint: disable=no-member
        draw_ones_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_2: # pylint: disable=no-member
        draw_twos_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_3: # pylint: disable=no-member
        draw_threes_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_4: # pylint: disable=no-member
        draw_fours_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_5: # pylint: disable=no-member
        draw_fives_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_6: # pylint: disable=no-member
        draw_sixes_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_q: # pylint: disable=no-member
        draw_pair_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_w: # pylint: disable=no-member
        draw_two_pairs_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_e: # pylint: disable=no-member
        draw_three_of_a_kind_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_r: # pylint: disable=no-member
        draw_four_of_a_kind_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_t: # pylint: disable=no-member
        draw_small_straight_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_y: # pylint: disable=no-member
        draw_large_straight_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_u: # pylint: disable=no-member
        draw_full_house_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_i: # pylint: disable=no-member
        draw_chance_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_o: # pylint: disable=no-member
        draw_yatzy_points(screen, font_small, dices)
        pygame.display.flip()

    elif event.key == pygame.K_ESCAPE: # pylint: disable=no-member
        quit_game()
