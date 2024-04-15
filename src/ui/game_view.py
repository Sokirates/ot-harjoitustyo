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


def draw_game_screen(screen, font_small, dice1, dice2, dice3, dice4, dice5):
    screen.fill((255, 255, 255))
    dice1.draw(screen, font_small)
    dice2.draw(screen, font_small)
    dice3.draw(screen, font_small)
    dice4.draw(screen, font_small)
    dice5.draw(screen, font_small)

    dice_rolling_text = font_small.render(
        "Heitä nopppia (SPACE)", True, (0, 0, 0))
    screen.blit(dice_rolling_text, (150 -
                dice_rolling_text.get_width() // 2, 10))
    
    quit_game_text = font_small.render(
        "Lopeta peli (Paina ESC)", True, (0, 0, 0))
    screen.blit(quit_game_text, (500 -
                quit_game_text.get_width() // 2, 450))
    
    pygame.display.flip()
    global game_running
    game_running = True

