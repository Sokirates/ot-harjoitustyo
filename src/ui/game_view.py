import entities.points
import pygame
import sys


def draw_start_screen(screen, font_large, font_small, width):
    screen.fill((255, 255, 255))

    start_message = font_large.render("Yatzy", True, (0, 0, 0))
    screen.blit(start_message, (width // 2 -
                start_message.get_width() // 2, 100))

    start_game_text = font_small.render(
        "Aloita peli (Paina SPACE)", True, (0, 0, 0))
    screen.blit(start_game_text, (width // 2 -
                start_game_text.get_width() // 2, 200))

    see_instructions = font_small.render(
        "Katso ohjeet (Paina 1)", True, (0, 0, 0))
    screen.blit(see_instructions, (width // 2 -
                start_game_text.get_width() // 2, 300))

    quit_game_text = font_small.render(
        "Lopeta peli (Paina ESC)", True, (0, 0, 0))
    screen.blit(quit_game_text, (width // 2 -
                quit_game_text.get_width() // 2, 250))

    pygame.display.flip()


def draw_instructions_screen(screen, font_large, font_small, width):
    screen.fill((255, 255, 255))

    instructions_message = font_large.render("Ohjeet", True, (0, 0, 0))
    screen.blit(instructions_message, (width // 2 -
                instructions_message.get_width() // 2, 50))

    instructions_text2 = font_small.render(
        "Vuoron aikana pelaaja saa vuorollaan heittää noppia", True, (0, 0, 0))
    screen.blit(instructions_text2, (width // 2 -
                instructions_text2.get_width() // 2, 150))

    instructions_text3 = font_small.render(
        "enintään kolmekertaa. Pelaaja voi lukita osan nopista", True, (0, 0, 0))
    screen.blit(instructions_text3, (width // 2 -
                instructions_text3.get_width() // 2, 200))

    instructions_text4 = font_small.render(
        "ensimmäisen tai toisen heiton jälkeen", True, (0, 0, 0))
    screen.blit(instructions_text4, (width // 2 -
                instructions_text4.get_width() // 2, 250))

    instructions_text5 = font_small.render(
        "ja heittää loput uudestaan.", True, (0, 0, 0))
    screen.blit(instructions_text5, (width // 2 -
                instructions_text5.get_width() // 2, 300))

    go_start_screen = font_small.render(
        "Palaa aloitus näyttöön (Paina 2)", True, (0, 0, 0))
    screen.blit(go_start_screen, (width // 2 -
                go_start_screen.get_width() // 2, 350))

    start_game_text = font_small.render(
        "Aloita peli (Paina SPACE)", True, (0, 0, 0))
    screen.blit(start_game_text, (width // 2 -
                start_game_text.get_width() // 2, 400))

    pygame.display.flip()


def quit_game():
    pygame.quit()
    sys.exit()


def draw_game_screen(screen, font_small, dices, throws_left=None, scoreboard=""):
    screen.fill((255, 255, 255))
    for dice in dices:
        dice.draw(screen, font_small)

    dice_rolling_text = font_small.render(
        "Heitä nopppia (Paina SPACE)", True, (0, 0, 255))
    screen.blit(dice_rolling_text, (10, 10))

    quit_game_text = font_small.render(
        "Lopeta peli (Paina ESC)", True, (0, 0, 0))
    screen.blit(quit_game_text, (500 -
                quit_game_text.get_width() // 2, 450))

    if throws_left == 0:
        text_rolls_left = font_small.render(
            "Aloita uusi kierros (ENTER)", True, (255, 0, 0))   
        screen.blit(text_rolls_left, (340, 10))
    else:
        text_rolls_left = font_small.render(
            f"Heittoja jäljellä: {throws_left}", True, (255, 0, 0))
        screen.blit(text_rolls_left, (400, 10))

    text_hold_dice = font_small.render(
        "Lukitse haluamia noppia (Paina ENTER)", True, (0, 0, 255))
    screen.blit(text_hold_dice, (40, 130))

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
        text_rendered = font_small.render(text, True, (0, 0, 0))
        screen.blit(text_rendered, (50, text_y_position))
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
        text_rendered = font_small.render(text, True, (0, 0, 0))
        screen.blit(text_rendered, (120, text_y_position))
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
        text_rendered = font_small.render(text, True, (0, 0, 0))
        screen.blit(text_rendered, (300, text_y_position))
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
        text_rendered = font_small.render(text, True, (0, 0, 0))
        screen.blit(text_rendered, (500, text_y_position))
        text_y_position += 30

    pygame.display.flip()
    global game_running
    game_running = True


def draw_ones_points(screen, font_small, dices, scoreboard):
    ones_score = entities.points.PointsCounter.calculate_ones(dices)
    text_rendered = font_small.render(f"{ones_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (120, 170))
    scoreboard['ones'] = ones_score
    pygame.display.flip()


def draw_twos_points(screen, font_small, dices, scoreboard):
    twos_score = entities.points.PointsCounter.calculate_twos(dices)
    text_rendered = font_small.render(f"{twos_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (120, 205))
    scoreboard['twos'] = twos_score
    pygame.display.flip()


def draw_threes_points(screen, font_small, dices, scoreboard):
    threes_score = entities.points.PointsCounter.calculate_threes(dices)
    text_rendered = font_small.render(f"{threes_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (120, 240))
    scoreboard['threes'] = threes_score
    pygame.display.flip()


def draw_fours_points(screen, font_small, dices, scoreboard):
    fours_score = entities.points.PointsCounter.calculate_fours(dices)
    text_rendered = font_small.render(f"{fours_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (120, 275))
    scoreboard['fours'] = fours_score
    pygame.display.flip()


def draw_fives_points(screen, font_small, dices, scoreboard):
    fives_score = entities.points.PointsCounter.calculate_fives(dices)
    text_rendered = font_small.render(f"{fives_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (120, 310))
    scoreboard['fives'] = fives_score
    pygame.display.flip()


def draw_sixes_points(screen, font_small, dices, scoreboard):
    sixes_score = entities.points.PointsCounter.calculate_sixes(dices)
    text_rendered = font_small.render(f"{sixes_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (120, 345))
    scoreboard['sixes'] = sixes_score
    pygame.display.flip()


def draw_pair_points(screen, font_small, dices, scoreboard):
    pair_score = entities.points.PointsCounter.calculate_pair(dices)
    text_rendered = font_small.render(f"{pair_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (500, 170))
    scoreboard['pair'] = pair_score
    pygame.display.flip()


def draw_two_pairs_points(screen, font_small, dices, scoreboard):
    two_pair_score = entities.points.PointsCounter.calculate_two_pairs(dices)
    text_rendered = font_small.render(f"{two_pair_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (500, 200))
    scoreboard["two_pairs"] = two_pair_score
    pygame.display.flip()


def draw_three_of_a_kind_points(screen, font_small, dices, scoreboard):
    three_kind_score = entities.points.PointsCounter.calculate_three_of_a_kind(
        dices)
    text_rendered = font_small.render(f"{three_kind_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (500, 230))
    scoreboard["three_of_a_kind"] = three_kind_score
    pygame.display.flip()


def draw_four_of_a_kind_points(screen, font_small, dices, scoreboard):
    four_kind_score = entities.points.PointsCounter.calculate_four_of_a_kind(
        dices)
    text_rendered = font_small.render(f"{four_kind_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (500, 260))
    scoreboard["four_of_a_kind"] = four_kind_score
    pygame.display.flip()


def draw_small_straight_points(screen, font_small, dices, scoreboard):
    small_score = entities.points.PointsCounter.calculate_small_straight(
        dices)
    text_rendered = font_small.render(f"{small_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (500, 290))
    scoreboard["small_straight"] = small_score
    pygame.display.flip()


def draw_large_straight_points(screen, font_small, dices, scoreboard):
    large_score = entities.points.PointsCounter.calculate_large_straight(
        dices)
    text_rendered = font_small.render(f"{large_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (500, 320))
    scoreboard["large_straight"] = large_score
    pygame.display.flip()


def draw_full_house_points(screen, font_small, dices, scoreboard):
    full_house_score = entities.points.PointsCounter.calculate_full_house(
        dices)
    text_rendered = font_small.render(f"{full_house_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (500, 350))
    scoreboard["full_house"] = full_house_score
    pygame.display.flip()


def draw_chance_points(screen, font_small, dices, scoreboard):
    chance_score = entities.points.PointsCounter.calculate_chance(dices)
    text_rendered = font_small.render(f"{chance_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (500, 380))
    scoreboard["chance"] = chance_score
    pygame.display.flip()


def draw_yatzy_points(screen, font_small, dices, scoreboard):
    yatzy_score = entities.points.PointsCounter.calculate_yatzy(dices)
    text_rendered = font_small.render(f"{yatzy_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (500, 410))
    scoreboard["yatzy"] = yatzy_score
    pygame.display.flip()

def draw_bonus_points(screen, font_small, scoreboard):
    if int(scoreboard['ones'])+int(scoreboard["twos"])+int(scoreboard["threes"])+int(scoreboard["fours"])+int(scoreboard["fives"])+int(scoreboard["sixes"]) >= 63:
        bonus_score= 50
    else:
        bonus_score = 0
    scoreboard["bonus"] = bonus_score
    text_rendered = font_small.render(f"{bonus_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (200, 410))
    
    pygame.display.flip()
    
    