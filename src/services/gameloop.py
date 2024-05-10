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

        self.scoreboard = {
            "ones" : "",
            "twos" : "", 
            "threes" : "", 
            "fours" : "", 
            "fives" : "", 
            "sixes": "",
            "subtotal":"",
            "bonus": "",
            "pair": "", 
            "two_pairs": "", 
            "three_of_a_kind": "", 
            "four_of_a_kind" : "", 
            "small_straight" : "", 
            "large_straight" : "", 
            "full_house" : "", 
            "chance" : "", 
            "yatzy" : ""
        }

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
            draw_game_screen(self.screen, self.font_small, self.turn.dices, self.turn.throws_left, self.scoreboard)
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
            draw_game_screen(self.screen, self.font_small, self.turn.dices, self.turn.throws_left, self.scoreboard)

        elif self.turn.throws_left >= 1 and event.key == pygame.K_SPACE: # pylint: disable=no-member
            self.turn.throw_dices()
            draw_game_screen(self.screen, self.font_small, self.turn.dices, self.turn.throws_left, self.scoreboard)

        elif event.key == pygame.K_RETURN: # pylint: disable=no-member  
            x, y = pygame.mouse.get_pos()
            for dice in self.turn.dices:
                if dice.x <= x <= dice.x + dice.size and dice.y <= y <= dice.y + dice.size:
                    dice.locked = not dice.locked  # Vaihda nopan lukitusasetus
                    draw_game_screen(self.screen, self.font_small, self.turn.dices, self.turn.throws_left, self.scoreboard)

        elif event.key == pygame.K_1: # pylint: disable=no-member
            draw_ones_points(self.screen, self.font_small, self.turn.dices, self.scoreboard)

        elif event.key == pygame.K_2: # pylint: disable=no-member
            draw_twos_points(self.screen, self.font_small, self.turn.dices, self.scoreboard)

        elif event.key == pygame.K_3: # pylint: disable=no-member
            draw_threes_points(self.screen, self.font_small, self.turn.dices, self.scoreboard)

        elif event.key == pygame.K_4: # pylint: disable=no-member
            draw_fours_points(self.screen, self.font_small, self.turn.dices, self.scoreboard)

        elif event.key == pygame.K_5: # pylint: disable=no-member
            draw_fives_points(self.screen, self.font_small, self.turn.dices, self.scoreboard)

        elif event.key == pygame.K_6: # pylint: disable=no-member
            draw_sixes_points(self.screen, self.font_small, self.turn.dices, self.scoreboard)

        elif event.key == pygame.K_q: # pylint: disable=no-member
            draw_pair_points(self.screen, self.font_small, self.turn.dices, self.scoreboard)

        elif event.key == pygame.K_w: # pylint: disable=no-member
            draw_two_pairs_points(self.screen, self.font_small, self.turn.dices, self.scoreboard)

        elif event.key == pygame.K_e: # pylint: disable=no-member
            draw_three_of_a_kind_points(self.screen, self.font_small, self.turn.dices, self.scoreboard)

        elif event.key == pygame.K_r: # pylint: disable=no-member
            draw_four_of_a_kind_points(self.screen, self.font_small, self.turn.dices, self.scoreboard)

        elif event.key == pygame.K_t: # pylint: disable=no-member
            draw_small_straight_points(self.screen, self.font_small, self.turn.dices, self.scoreboard)

        elif event.key == pygame.K_y: # pylint: disable=no-member
            draw_large_straight_points(self.screen, self.font_small, self.turn.dices, self.scoreboard)

        elif event.key == pygame.K_u: # pylint: disable=no-member
            draw_full_house_points(self.screen, self.font_small, self.turn.dices, self.scoreboard)

        elif event.key == pygame.K_i: # pylint: disable=no-member
            draw_chance_points(self.screen, self.font_small, self.turn.dices, self.scoreboard)

        elif event.key == pygame.K_o: # pylint: disable=no-member
            draw_yatzy_points(self.screen, self.font_small, self.turn.dices, self.scoreboard)

        elif event.key == pygame.K_b:
            draw_bonus_points(self.screen, self.font_small, self.scoreboard)

        elif event.key == pygame.K_ESCAPE: # pylint: disable=no-member
            quit_game()

        pygame.display.flip()

