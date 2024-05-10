import entities.points
import pygame
import sys


class ScreenDrawer:
    def __init__(
            self,
            screen,
            font_large,
            font_small,
            width=640
        ):
        self._screen = screen
        self._font_large = font_large
        self._font_small = font_small
        self._width = width

    def draw_start_screen(self):
        self._screen.fill((255, 255, 255))

        start_message = self._font_large.render("Yatzy", True, (0, 0, 0))
        self._screen.blit(start_message, (self._width // 2 -
                    start_message.get_width() // 2, 100))

        start_game_text = self._font_small.render(
            "Aloita peli (Paina SPACE)", True, (0, 0, 0))
        self._screen.blit(start_game_text, (self._width // 2 -
                    start_game_text.get_width() // 2, 200))

        see_instructions = self._font_small.render(
            "Katso ohjeet (Paina 1)", True, (0, 0, 0))
        self._screen.blit(see_instructions, (self._width // 2 -
                    start_game_text.get_width() // 2, 300))

        quit_game_text = self._font_small.render(
            "Lopeta peli (Paina ESC)", True, (0, 0, 0))
        self._screen.blit(quit_game_text, (self._width // 2 -
                    quit_game_text.get_width() // 2, 250))

        pygame.display.flip()

    def draw_instructions_screen(self):
        self._screen.fill((255, 255, 255))

        instructions_message = self._font_large.render("Ohjeet", True, (0, 0, 0))
        self._screen.blit(instructions_message, (self._width // 2 -
                    instructions_message.get_width() // 2, 50))

        instructions_text2 = self._font_small.render(
            "Vuoron aikana pelaaja saa vuorollaan heittää noppia", True, (0, 0, 0))
        self._screen.blit(instructions_text2, (self._width // 2 -
                    instructions_text2.get_width() // 2, 150))

        instructions_text3 = self._font_small.render(
            "enintään kolmekertaa. Pelaaja voi lukita osan nopista", True, (0, 0, 0))
        self._screen.blit(instructions_text3, (self._width // 2 -
                    instructions_text3.get_width() // 2, 200))

        instructions_text4 = self._font_small.render(
            "ensimmäisen tai toisen heiton jälkeen", True, (0, 0, 0))
        self._screen.blit(instructions_text4, (self._width // 2 -
                    instructions_text4.get_width() // 2, 250))

        instructions_text5 = self._font_small.render(
            "ja heittää loput uudestaan.", True, (0, 0, 0))
        self._screen.blit(instructions_text5, (self._width // 2 -
                    instructions_text5.get_width() // 2, 300))

        go_start_screen = self._font_small.render(
            "Palaa aloitus näyttöön (Paina 2)", True, (0, 0, 0))
        self._screen.blit(go_start_screen, (self._width // 2 -
                    go_start_screen.get_width() // 2, 350))

        start_game_text = self._font_small.render(
            "Aloita peli (Paina SPACE)", True, (0, 0, 0))
        self._screen.blit(start_game_text, (self._width // 2 -
                    start_game_text.get_width() // 2, 400))

        pygame.display.flip()

    def draw_game_screen(self, dices, throws_left=None, scoreboard=""):
        self._screen.fill((255, 255, 255))
        for dice in dices:
            dice.draw(self._screen, self._font_small)

        dice_rolling_text = self._font_small.render(
            "Heitä nopppia (Paina SPACE)", True, (0, 0, 255))
        self._screen.blit(dice_rolling_text, (10, 10))

        quit_game_text = self._font_small.render(
            "Lopeta peli (Paina ESC)", True, (0, 0, 0))
        self._screen.blit(quit_game_text, (500 -
                    quit_game_text.get_width() // 2, 450))

        if throws_left == 0:
            text_rolls_left = self._font_small.render(
                "Aloita uusi kierros (ENTER)", True, (255, 0, 0))   
            self._screen.blit(text_rolls_left, (340, 10))
        else:
            text_rolls_left = self._font_small.render(
                f"Heittoja jäljellä: {throws_left}", True, (255, 0, 0))
            self._screen.blit(text_rolls_left, (400, 10))

        text_hold_dice = self._font_small.render(
            "Lukitse haluamia noppia (Paina ENTER)", True, (0, 0, 255))
        self._screen.blit(text_hold_dice, (40, 130))

        text_y_position = 170
        texts_points_1 = ["1(1):",
                        "2(2):",
                        "3(3):",
                        "4(4): ",
                        "5(5): ",
                        "6(6): ",
                        "Välisumma: ",
                        f"Bonus: {scoreboard['bonus']}"
                        ]
        text_y_position = 170
        for text in texts_points_1:
            text_rendered = self._font_small.render(text, True, (0, 0, 0))
            self._screen.blit(text_rendered, (50, text_y_position))
            text_y_position += 35

        text_y_position = 170
        texts_points_1 = [f"{scoreboard['ones']}",
                        f"{scoreboard['twos']}",
                        f"{scoreboard['threes']}",
                        f"{scoreboard['fours']}",
                        f"{scoreboard['fives']}",
                        f"{scoreboard['sixes']}",
                        ]
        text_y_position = 170
        for text in texts_points_1:
            text_rendered = self._font_small.render(text, True, (0, 0, 0))
            self._screen.blit(text_rendered, (120, text_y_position))
            text_y_position += 35

        texts_points_2 = ["Yksi pari (q):",
                        "Kaksi paria (w):",
                        "Kolmoisluku (e):",
                        "Neloisluku (r): ",
                        "Pieni suora (t):",
                        "Suuri suora (y):",
                        "Täysikäsi (u):",
                        "Sattuma (i):  ",
                        "Yatzy (o):"    
                        ]
        text_y_position = 170
        for text in texts_points_2:
            text_rendered = self._font_small.render(text, True, (0, 0, 0))
            self._screen.blit(text_rendered, (300, text_y_position))
            text_y_position += 30

        texts_points_3 = [f"{scoreboard['pair']}",
                        f"{scoreboard['two_pairs']}",
                        f"{scoreboard['three_of_a_kind']}",
                        f"{scoreboard['four_of_a_kind']}",
                        f"{scoreboard['small_straight']}",
                        f"{scoreboard['large_straight']}",
                        f"{scoreboard['full_house']}",
                        f"{scoreboard['chance']}",
                        f"{scoreboard['yatzy']}"
                        ]
        text_y_position = 170
        for text in texts_points_3:
            text_rendered = self._font_small.render(text, True, (0, 0, 0))
            self._screen.blit(text_rendered, (500, text_y_position))
            text_y_position += 30

        pygame.display.flip()
        global game_running
        game_running = True

    def draw_points(self, scoreboard):
        for i, (_, val) in enumerate(scoreboard.items()):
            text_redered = self._font_small.render(f"{val}", True, (0, 0, 0))
            if i < 8:
                self._screen.blit(text_redered, (120, 170 + i*35))
            else:
                self._screen.blit(text_redered, (500, 170 + (i - 8)*30))
        pygame.display.flip()
