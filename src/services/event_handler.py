import sys
import pygame
from entities.game_turn import GameTurn # pylint: disable=import-error
from entities.points import PointsCounter # pylint: disable=import-error


def quit_game():
    pygame.quit() # pylint: disable=no-member
    sys.exit()

class EventHandler:
    def __init__(self, drawer):
        self._drawer = drawer

    def handle_game_not_running_events(self, event, dices, throws_left, scoreboard):
        game_running = False
        if event.key == pygame.K_SPACE: # pylint: disable=no-member
            self._drawer.draw_game_screen(dices, throws_left, scoreboard)
            game_running = True

        elif event.key == pygame.K_1: # pylint: disable=no-member
            self._drawer.draw_instructions_screen()
        elif event.key == pygame.K_ESCAPE: # pylint: disable=no-member
            quit_game()
        elif event.key == pygame.K_2: # pylint: disable=no-member
            self._drawer.draw_start_screen()
        return game_running

    def handle_game_running_events(self, event, dices, scoreboard, game_turn):
        if event.key == pygame.K_ESCAPE: # pylint: disable=no-member
            quit_game()
        elif game_turn.throws_left <= 0 and not game_turn.points_assigned:
            if event.key == pygame.K_1 and scoreboard['ones'] == "": # pylint: disable=no-member
                scoreboard['ones'] = PointsCounter.calculate_ones(dices)
                game_turn.points_assigned = True

            elif event.key == pygame.K_2 and scoreboard['twos'] == "": # pylint: disable=no-member
                scoreboard['twos'] = PointsCounter.calculate_twos(dices)
                game_turn.points_assigned = True

            elif event.key == pygame.K_3 and scoreboard['threes'] == "": # pylint: disable=no-member
                scoreboard['threes'] = PointsCounter.calculate_threes(dices)
                game_turn.points_assigned = True

            elif event.key == pygame.K_4 and scoreboard['fours'] == "": # pylint: disable=no-member
                scoreboard['fours'] = PointsCounter.calculate_fours(dices)
                game_turn.points_assigned = True

            elif event.key == pygame.K_5 and scoreboard['fives'] == "": # pylint: disable=no-member
                scoreboard['fives'] = PointsCounter.calculate_fives(dices)
                game_turn.points_assigned = True

            elif event.key == pygame.K_6 and scoreboard['sixes'] == "": # pylint: disable=no-member
                scoreboard['sixes'] = PointsCounter.calculate_sixes(dices)
                game_turn.points_assigned = True

            elif event.key == pygame.K_q and scoreboard['pair'] == "": # pylint: disable=no-member
                scoreboard['pair'] = PointsCounter.calculate_pair(dices)
                game_turn.points_assigned = True

            elif event.key == pygame.K_w and scoreboard['two_pairs'] == "": # pylint: disable=no-member
                scoreboard['two_pairs'] = PointsCounter.calculate_two_pairs(dices)
                game_turn.points_assigned = True

            elif event.key == pygame.K_e and scoreboard['three_of_a_kind'] == "": # pylint: disable=no-member
                scoreboard['three_of_a_kind'] = PointsCounter.calculate_three_of_a_kind(dices)
                game_turn.points_assigned = True

            elif event.key == pygame.K_r and scoreboard['four_of_a_kind'] == "": # pylint: disable=no-member
                scoreboard['four_of_a_kind'] = PointsCounter.calculate_four_of_a_kind(dices)
                game_turn.points_assigned = True

            elif event.key == pygame.K_t and scoreboard['small_straight'] == "": # pylint: disable=no-member
                scoreboard['small_straight'] = PointsCounter.calculate_small_straight(dices)
                game_turn.points_assigned = True

            elif event.key == pygame.K_y and scoreboard['large_straight'] == "": # pylint: disable=no-member
                scoreboard['large_straight'] = PointsCounter.calculate_large_straight(dices)
                game_turn.points_assigned = True

            elif event.key == pygame.K_u and scoreboard['full_house'] == "": # pylint: disable=no-member
                scoreboard['full_house'] = PointsCounter.calculate_full_house(dices)
                game_turn.points_assigned = True

            elif event.key == pygame.K_i and scoreboard['chance'] == "": # pylint: disable=no-member
                scoreboard['chance'] = PointsCounter.calculate_chance(dices)
                game_turn.points_assigned = True

            elif event.key == pygame.K_o and scoreboard['yatzy'] == "": # pylint: disable=no-member
                scoreboard['yatzy'] = PointsCounter.calculate_yatzy(dices)
                game_turn.points_assigned = True

            elif event.key == pygame.K_b and scoreboard['bonus'] == "": # pylint: disable=no-member
                scoreboard['bonus'] = PointsCounter.calculate_bonus(scoreboard)
                game_turn.points_assigned = True

            if game_turn.points_assigned:
                self._drawer.draw_points(scoreboard)

        elif game_turn.throws_left <= 0 and event.key == pygame.K_RETURN: # pylint: disable=no-member
            new_turn = GameTurn()
            self._drawer.draw_game_screen(new_turn.dices, new_turn.throws_left, scoreboard)
            return new_turn

        elif game_turn.throws_left >= 1 and event.key == pygame.K_SPACE: # pylint: disable=no-member
            game_turn.throw_dices()
            self._drawer.draw_game_screen(dices, game_turn.throws_left, scoreboard)

        elif event.key == pygame.K_RETURN: # pylint: disable=no-member
            x, y = pygame.mouse.get_pos()
            for dice in game_turn.dices:
                if dice.x <= x <= dice.x + dice.size and dice.y <= y <= dice.y + dice.size:
                    dice.locked = not dice.locked  # Vaihda nopan lukitusasetus
                    self._drawer.draw_game_screen(dices, game_turn.throws_left, scoreboard)

        pygame.display.flip()
