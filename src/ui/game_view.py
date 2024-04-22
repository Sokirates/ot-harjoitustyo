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


def draw_game_screen(screen, font_small, dices):
    screen.fill((255, 255, 255))
    for dice in dices:
        dice.draw(screen, font_small)
    
    dice_rolling_text = font_small.render(
        "Heitä nopppia (SPACE)", True, (0, 0, 255))
    screen.blit(dice_rolling_text, (150 -
                dice_rolling_text.get_width() // 2, 10))

    quit_game_text = font_small.render(
        "Lopeta peli (Paina ESC)", True, (0, 0, 0))
    screen.blit(quit_game_text, (500 -
                quit_game_text.get_width() // 2, 450))

    text_rolls_left = font_small.render("Heittoja jäljellä:", True, (255, 0, 0))
    screen.blit(text_rolls_left, (400, 10))

    text_hold_dice = font_small.render("Lukitse painamalla noppia", True, (0, 0, 255))
    screen.blit(text_hold_dice, (50, 135))

    text_y_position = 170
    for i in range(1, 7):
        text_points_1_6 = font_small.render(f"{i} ({i}):", True, (0, 0, 0))
        screen.blit(text_points_1_6, (50, text_y_position))
        text_y_position += 35
    text_valisumma = font_small.render("Välisumma:", True, (0, 0, 0))
    screen.blit(text_valisumma, (50, text_y_position))
    text_bonus = font_small.render("Bonus:", True, (0, 0, 0))
    screen.blit(text_bonus, (50, text_y_position + 35))
    
    texts_points_2 = ["Yksi pari (q):", 
                      "Kaksi paria (w):", 
                      "Kolmoisluku (e):", 
                      "Neloisluku (r):", 
                      "Pieni suora (t):", 
                      "Suuri suora (y):", 
                      "Täysikäsi (u):", 
                      "Sattuma (i):", 
                      "Yatzy (o):"
                      ]
    text_y_position = 170
    for text in texts_points_2:
        text_rendered = font_small.render(text, True, (0, 0, 0))
        screen.blit(text_rendered, (300, text_y_position))
        text_y_position += 30

    pygame.display.flip()
    global game_running
    game_running = True


def draw_ones_points(screen, font_small, dices):
    ones_score = entities.points.Points_counter.calculate_ones(dices)
    text_rendered = font_small.render(f"{ones_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (120, 170))
    pygame.display.flip()

def draw_twos_points(screen, font_small, dices):
    twos_score = entities.points.Points_counter.calculate_twos(dices)
    text_rendered = font_small.render(f"{twos_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (120, 205))
    pygame.display.flip()

def draw_threes_points(screen, font_small, dices):
    threes_score = entities.points.Points_counter.calculate_threes(dices)
    text_rendered = font_small.render(f"{threes_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (120, 240))
    pygame.display.flip()

def draw_fours_points(screen, font_small, dices):
    fours_score = entities.points.Points_counter.calculate_fours(dices)
    text_rendered = font_small.render(f"{fours_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (120, 275))
    pygame.display.flip()

def draw_fives_points(screen, font_small, dices):
    fives_score = entities.points.Points_counter.calculate_fives(dices)
    text_rendered = font_small.render(f"{fives_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (120, 310))
    pygame.display.flip()

def draw_sixes_points(screen, font_small, dices):
    sixes_score = entities.points.Points_counter.calculate_sixes(dices)
    text_rendered = font_small.render(f"{sixes_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (120, 345))
    pygame.display.flip()

def draw_pair_points(screen, font_small, dices):
    pair_score = entities.points.Points_counter.calculate_pair(dices)
    text_rendered = font_small.render(f"{pair_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (500, 170))
    pygame.display.flip()

def draw_two_pairs_points(screen, font_small, dices):
    two_pair_score = entities.points.Points_counter.calculate_two_pairs(dices)
    text_rendered = font_small.render(f"{two_pair_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (500, 200))
    pygame.display.flip()

def draw_three_of_a_kind_points(screen, font_small, dices):
    three_kind_score = entities.points.Points_counter.calculate_three_of_a_kind(dices)
    text_rendered = font_small.render(f"{three_kind_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (500, 230))
    pygame.display.flip()

def draw_four_of_a_kind_points(screen, font_small, dices):
    four_kind_score = entities.points.Points_counter.calculate_four_of_a_kind(dices)
    text_rendered = font_small.render(f"{four_kind_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (500, 260))
    pygame.display.flip()

def draw_small_straight_points(screen, font_small, dices):
    small_score = entities.points.Points_counter.calculate_small_straight(dices)
    text_rendered = font_small.render(f"{small_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (500, 290))
    pygame.display.flip()

def draw_large_straight_points(screen, font_small, dices):
    large_score = entities.points.Points_counter.calculate_large_straight(dices)
    text_rendered = font_small.render(f"{large_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (500, 320))
    pygame.display.flip()

def draw_full_house_points(screen, font_small, dices):
    full_house_score = entities.points.Points_counter.calculate_full_house(dices)
    text_rendered = font_small.render(f"{full_house_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (500, 350))
    pygame.display.flip()

def draw_chance_points(screen, font_small, dices):
    chance_score = entities.points.Points_counter.calculate_chance(dices)
    text_rendered = font_small.render(f"{chance_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (500, 380))
    pygame.display.flip()

def draw_yatzy_points(screen, font_small, dices):
    yatzy_score = entities.points.Points_counter.calculate_yatzy(dices)
    text_rendered = font_small.render(f"{yatzy_score}", True, (0, 0, 0))
    screen.blit(text_rendered, (500, 410))
    pygame.display.flip()