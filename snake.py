import pygame
import random
import time

# Initialize pygame
pygame.init()

# Set up display
width, height = 600, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Clock to control the game speed
clock = pygame.time.Clock()

# Snake block size
block_size = 20

# Font for displaying the score and game over message
font_style = pygame.font.SysFont(None, int(width / 15))  # Proportional font size
score_font = pygame.font.SysFont(None, int(width / 20))  # Proportional font size for score

def display_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    window.blit(value, [10, 10])

def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(window, green, [block[0], block[1], block_size, block_size])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    # Center the message on the screen
    mesg_rect = mesg.get_rect(center=(width / 2, height / 2))
    window.blit(mesg, mesg_rect)

def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x = width / 2
    y = height / 2

    # Change in position
    x_change = 0
    y_change = 0

    # Snake body
    snake_list = []
    snake_length = 1

    # Food position (randomized)
    food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, height - block_size) / block_size) * block_size

    while not game_over:

        while game_close:
            window.fill(black)
            message("Game Over! Press any key to play again", red)
            display_score(snake_length - 1)
            pygame.display.update()

            # Wait for the player to press a key to restart or quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    game_loop()  # Restart the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        # Check if the snake hits the wall
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        window.fill(black)
        pygame.draw.rect(window, red, [food_x, food_y, block_size, block_size])
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if the snake collides with itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        display_score(snake_length - 1)

        pygame.display.update()

        # Check if the snake eats the food
        if x == food_x and y == food_y:
            # Generate new random food position
            food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, height - block_size) / block_size) * block_size
            snake_length += 1

        clock.tick(15)

    pygame.quit()
    quit()

# Start the game
game_loop()