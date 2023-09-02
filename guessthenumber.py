import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
FONT = pygame.font.Font(None, 36)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the Number")

# Initialize game variables
number_to_guess = random.randint(1, 100)
attempts = 0
active_flag = True

# Initialize the input_text variable
input_text = ""

# Main game loop
while active_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active_flag = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                active_flag = False

            if event.key == pygame.K_RETURN:
                attempts += 1
                guess = int(input_text)
                if guess == number_to_guess:
                    active_flag = False
                elif guess < number_to_guess:
                    input_text = ""
                    message = FONT.render("Try a higher number", True, BLUE)
                else:
                    input_text = ""
                    message = FONT.render("Try a lower number", True, BLUE)
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    screen.fill(WHITE)
    input_box = pygame.Rect(100, 200, 600, 36)
    color = pygame.Color('lightskyblue3')
    pygame.draw.rect(screen, color, input_box)
    text_surface = FONT.render(input_text, True, BLUE)
    width = max(200, text_surface.get_width() + 10)
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(screen, BLUE, input_box, 2)

    attempts_text = FONT.render(f"Attempts: {attempts}", True, BLUE)
    screen.blit(attempts_text, (10, 10))

    pygame.display.flip()

# Game loop has exited
if guess == number_to_guess:
    message = FONT.render(f"Congratulations! You guessed the number in {attempts} attempts.", True, BLUE)
else:
    message = FONT.render(f"Game Over! The number was {number_to_guess}.", True, BLUE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(WHITE)
    screen.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - message.get_height() // 2))
    pygame.display.flip()
