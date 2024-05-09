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
    draw_bonus_points,
    quit_game
)
from entities.dice import Dice # pylint: disable=import-error
from entities.game_turn import GameTurn # pylint: disable=import-error

choose1 = choose2 = choose3 = choose4 = choose5 =  choose6 = choose7 = choose8 = choose9 = choose10 = choose11 = choose12 = choose13 = choose14 = choose15 = 1

def start_game(screen, width):
    game_running = False
    clock = pygame.time.Clock()

    font_large = pygame.font.SysFont("Arial", 36)
    font_small = pygame.font.SysFont("Arial", 24)

    draw_start_screen(screen, font_large, font_small, width)

    game_loop = GameLoop(screen, game_running, clock, font_small, font_large, width)

    game_loop.start_game_loop()

class GameLoop:
    def __init__(self, screen, game_running, clock, font_small, font_large, width):
        self.screen = screen
        self.game_running = game_running
        self.clock = clock
        self.font_small = font_small
        self.font_large = font_large
        self.width = width

        self.turn = GameTurn()
    
    def start_game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type != pygame.KEYDOWN: # pylint: disable=no-member
                    continue

                if not self.game_running:
                    self.game_running = self.handle_game_not_running_events(event)
                else:
                    self.handle_game_running_events(event)

            self.clock.tick(80)


    def handle_game_not_running_events(self, event):
        if event.key == pygame.K_SPACE: # pylint: disable=no-member
            draw_game_screen(self.screen, self.font_small, self.turn.dices, self.turn.throws_left)
            game_running = True

        elif event.key == pygame.K_1: # pylint: disable=no-member
            draw_instructions_screen(self.screen, self.font_large, self.font_small, self.width)
        elif event.key == pygame.K_ESCAPE: # pylint: disable=no-member
            quit_game()
        elif event.key == pygame.K_2: # pylint: disable=no-member
            draw_start_screen(self.screen, self.font_large, self.font_small, self.width)
        return game_running

    def handle_game_running_events(self, event):
        if self.turn.throws_left <= 0 and event.key == pygame.K_RETURN:
            self.turn = GameTurn()
            draw_game_screen(self.screen, self.font_small, self.turn.dices, self.turn.throws_left)

        elif self.turn.throws_left >= 1 and event.key == pygame.K_SPACE: # pylint: disable=no-member
            self.turn.throw_dices()
            draw_game_screen(self.screen, self.font_small, self.turn.dices, self.turn.throws_left)

        elif event.key == pygame.K_RETURN: # pylint: disable=no-member  
            x, y = pygame.mouse.get_pos()
            for dice in self.turn.dices:
                if dice.x <= x <= dice.x + dice.size and dice.y <= y <= dice.y + dice.size:
                    dice.locked = not dice.locked  # Vaihda nopan lukitusasetus
                    draw_game_screen(self.screen, self.font_small, self.turn.dices, self.turn.throws_left)

        elif event.key == pygame.K_1 and choose1 == 1: # pylint: disable=no-member
            draw_ones_points(self.screen, self.font_small, self.turn.dices)
            choose1 -1

        elif event.key == pygame.K_2 and choose2 == 1: # pylint: disable=no-member
            draw_twos_points(self.screen, self.font_small, self.turn.dices)
            choose2 -1

        elif event.key == pygame.K_3 and choose3 == 1: # pylint: disable=no-member
            draw_threes_points(self.screen, self.font_small, self.turn.dices)
            choose3 -1

        elif event.key == pygame.K_4 and choose4 == 1: # pylint: disable=no-member
            draw_fours_points(self.screen, self.font_small, self.turn.dices)
            choose4 -1

        elif event.key == pygame.K_5 and choose5 == 1: # pylint: disable=no-member
            draw_fives_points(self.screen, self.font_small, self.turn.dices)
            choose5 -1

        elif event.key == pygame.K_6 and choose6 == 1: # pylint: disable=no-member
            draw_sixes_points(self.screen, self.font_small, self.turn.dices)
            choose6 -1

        elif event.key == pygame.K_q and choose7 == 1: # pylint: disable=no-member
            draw_pair_points(self.screen, self.font_small, self.turn.dices)
            choose7 -1

        elif event.key == pygame.K_w and choose8 == 1: # pylint: disable=no-member
            draw_two_pairs_points(self.screen, self.font_small, self.turn.dices)
            choose8 -1

        elif event.key == pygame.K_e and choose9 == 1: # pylint: disable=no-member
            draw_three_of_a_kind_points(self.screen, self.font_small, self.turn.dices)
            choose9 -1

        elif event.key == pygame.K_r and choose10 == 1: # pylint: disable=no-member
            draw_four_of_a_kind_points(self.screen, self.font_small, self.turn.dices)
            choose10 -1

        elif event.key == pygame.K_t and choose11 == 1: # pylint: disable=no-member
            draw_small_straight_points(self.screen, self.font_small, self.turn.dices)
            choose11 -1

        elif event.key == pygame.K_y and choose12 == 1: # pylint: disable=no-member
            draw_large_straight_points(self.screen, self.font_small, self.turn.dices)
            choose12 -1

        elif event.key == pygame.K_u and choose13 == 1: # pylint: disable=no-member
            draw_full_house_points(self.screen, self.font_small, self.turn.dices)
            choose13 -1

        elif event.key == pygame.K_i and choose14 == 1: # pylint: disable=no-member
            draw_chance_points(self.screen, self.font_small, self.turn.dices)
            choose14 -1

        elif event.key == pygame.K_o and choose15 == 1: # pylint: disable=no-member
            draw_yatzy_points(self.screen, self.font_small, self.turn.dices)
            choose15 -1

        elif event.key == pygame.K_b:
            draw_bonus_points(self.screen, self.font_small)

        elif event.key == pygame.K_ESCAPE: # pylint: disable=no-member
            quit_game()

        pygame.display.flip()

