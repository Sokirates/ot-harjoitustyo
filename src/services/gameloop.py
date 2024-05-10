import pygame
from ui.game_view import ( # pylint: disable=import-error
    ScreenDrawer
)
from entities.game_turn import GameTurn # pylint: disable=import-error
from services.event_handler import EventHandler # pylint: disable=import-error

def start_game(screen, width):
    game_running = False
    clock = pygame.time.Clock()

    font_large = pygame.font.SysFont("Arial", 36)
    font_small = pygame.font.SysFont("Arial", 24)

    screen_drawer = ScreenDrawer(screen, font_large, font_small, width)
    screen_drawer.draw_start_screen()

    event_handler = EventHandler(screen_drawer)

    game_loop = GameLoop(game_running, clock, event_handler)

    game_loop.start_game_loop()

class GameLoop:
    def __init__(self, game_running, clock, event_handler):
        self.game_running = game_running
        self.clock = clock
        self.event_handler = event_handler

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
                    self.game_running = self.event_handler\
                        .handle_game_not_running_events(
                            event,
                            self.turn.dices,
                            self.turn.throws_left,
                            self.scoreboard
                        )
                else:
                    new_turn = self.event_handler\
                        .handle_game_running_events(
                            event,
                            self.turn.dices,
                            self.scoreboard,
                            self.turn
                        )
                    if new_turn:
                        self.turn = new_turn

            self.clock.tick(80)
