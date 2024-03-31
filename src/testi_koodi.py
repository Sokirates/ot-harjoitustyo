import pygame
import sys
import random

# Alusta Pygame
pygame.init()

# Määritä näytön koko ja nimi
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Yatzy")

# Alusta fontit
font = pygame.font.SysFont("Arial", 24)

# Määritä värit
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Alusta pelin tila
dice = [0, 0, 0, 0, 0]  # Noppaluvut
rolls_left = 3  # Heittojen määrä jäljellä

# Funktio heittää noppia
def roll_dice():
    for i in range(5):
        if dice[i] == 0:
            dice[i] = random.randint(1, 6)

# Funktio tarkistaa, onko voitto
def check_win():
    return max(dice.count(i) for i in range(1, 7)) == 5

# Pääsilmukka
running = True
while running:
    # Käsittele tapahtumat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and rolls_left > 0:
                roll_dice()
                rolls_left -= 1
            elif event.key == pygame.K_r:  # Resetoi peli
                dice = [0, 0, 0, 0, 0]
                rolls_left = 3

    # Päivitä näyttö
    screen.fill(WHITE)

    # Piirrä nopat
    dice_texts = [font.render(str(d), True, BLACK) for d in dice]
    for i, text in enumerate(dice_texts):
        text_rect = text.get_rect(center=((i+1)*(width//6), height//2))
        screen.blit(text, text_rect)

    # Näytä heittojen määrä
    rolls_left_text = font.render("Rolls left: " + str(rolls_left), True, BLACK)
    screen.blit(rolls_left_text, (10, 10))

    # Näytä voitto viesti
    if check_win():
        win_text = font.render("Voitit!", True, BLACK)
        screen.blit(win_text, (width//2 - win_text.get_width()//2, height//2 + 50))

    pygame.display.flip()

# Lopeta Pygame
pygame.quit()
sys.exit()