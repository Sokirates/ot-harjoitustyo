import pygame
import sys
import random

class Dice:
    def __init__(self, x=0, y=0, size=70):
        self.x = x
        self.y = y
        self.size = size
        self.value = 1

    def roll(self):
        self.value = random.randint(1, 6)

    def draw(self, screen, font):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.size, self.size), 2)
        dice_text = font.render(str(self.value), True, (0, 0, 0))
        screen.blit(dice_text, (self.x + self.size // 2 - dice_text.get_width() // 2, self.y + self.size // 2 - dice_text.get_height() // 2))

def draw_start_screen(screen, font_large, font_small, width):
    screen.fill((255, 255, 255)) 

    start_message = font_large.render("Yatzy", True, (0, 0, 0))
    screen.blit(start_message, (width // 2 - start_message.get_width() // 2, 100))

    start_game_text = font_small.render("Aloita peli (Paina SPACE)", True, (0, 0, 0))
    screen.blit(start_game_text, (width // 2 - start_game_text.get_width() // 2, 200))

    see_instructions = font_small.render("Katso ohjeet (Paina 1)", True, (0, 0, 0))
    screen.blit(see_instructions, (width // 2 - start_game_text.get_width() // 2, 300))

    quit_game_text = font_small.render("Lopeta peli (Paina ESC)", True, (0, 0, 0))
    screen.blit(quit_game_text, (width // 2 - quit_game_text.get_width() // 2, 250))

    pygame.display.flip()

def draw_instructions_screen(screen, font_large, font_small, width):
    screen.fill((255, 255, 255))

    instructions_message = font_large.render("Ohjeet", True, (0, 0, 0))
    screen.blit(instructions_message, (width // 2 - instructions_message.get_width() // 2, 50))

    instructions_text2 = font_small.render("Vuoron aikana pelaaja saa vuorollaan heittää noppia", True, (0, 0, 0))
    screen.blit(instructions_text2, (width // 2 - instructions_text2.get_width() // 2, 150))

    instructions_text3 = font_small.render("enintään kolmekertaa. Pelaaja voi lukita osan nopista", True, (0, 0, 0))
    screen.blit(instructions_text3, (width // 2 - instructions_text3.get_width() // 2, 200))

    instructions_text4 = font_small.render("ensimmäisen tai toisen heiton jälkeen", True, (0, 0, 0))
    screen.blit(instructions_text4, (width // 2 - instructions_text4.get_width() // 2, 250))

    instructions_text5 = font_small.render("ja heittää loput uudestaan.", True, (0, 0, 0))
    screen.blit(instructions_text5, (width // 2 - instructions_text5.get_width() // 2, 300))

    go_start_screen = font_small.render("Palaa aloitus näyttöön (Paina 2)", True, (0, 0, 0))
    screen.blit(go_start_screen, (width // 2 - go_start_screen.get_width() // 2, 350))

    start_game_text = font_small.render("Aloita peli (Paina SPACE)", True, (0, 0, 0))
    screen.blit(start_game_text, (width // 2 - start_game_text.get_width() // 2, 400))

    pygame.display.flip()

def quit_game():
    pygame.quit()
    sys.exit()

def draw_game_screen(screen, font_small, dice1, dice2, dice3, dice4, dice5):
    global game_running
    screen.fill((255, 255, 255))
    dice1.draw(screen, font_small)
    dice2.draw(screen, font_small)
    dice3.draw(screen, font_small)
    dice4.draw(screen, font_small)
    dice5.draw(screen, font_small)
    game_running = True
    pygame.display.flip()
    
def main():


    pygame.init()
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Yatzy")

    game_running = False
    clock = pygame.time.Clock()

    font_large = pygame.font.SysFont("Arial", 36)
    font_small = pygame.font.SysFont("Arial", 24)


    draw_start_screen(screen, font_large, font_small, width)

    while True:
        for event in pygame.event.get():
            if not game_running:    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        dice1 = Dice(50, 50)
                        dice2 = Dice(150, 50)
                        dice3 = Dice(250, 50)
                        dice4 = Dice(350, 50)
                        dice5 = Dice(450, 50)
                        draw_game_screen(screen, font_small, dice1, dice2, dice3, dice4, dice5)
                    elif event.key == pygame.K_1:
                        draw_instructions_screen(screen, font_large, font_small, width)
                    elif event.key == pygame.K_ESCAPE:
                        quit_game()
                    elif event.key == pygame.K_2:
                        draw_start_screen(screen, font_large, font_small, width)
            else:
                if event.type == pygame.QUIT:
                    quit_game()

        clock.tick(80)

if __name__ == "__main__":
    main()