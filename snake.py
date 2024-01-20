import pygame
import time
import random

snake_speed = 15

window_x = 720
window_y = 480

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)

pygame.init()
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

# Load the background image
background_image = pygame.image.load('background.jpg')  # Replace 'background.jpg' with your background image file
background_image = pygame.transform.scale(background_image, (window_x, window_y))

snake_head_color = red
snake_body_image = pygame.image.load('SnakeBody.png')  # Replace 'snake_body.png' with your body image file
snake_body_image = pygame.transform.scale(snake_body_image, (10, 10))  # Scale the body image

snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
food_color = white
food_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
food_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0
game_over_flag = False

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score: ' + str(score), True, color)
    score_rect = score_surface.get_rect(center=(window_x // 2, 20))
    game_window.blit(score_surface, score_rect)

def game_over():
    global game_over_flag
    if not game_over_flag:
        game_over_flag = True
        my_font = pygame.font.SysFont('arial', 50)
        game_over_surface = my_font.render('Game Over', True, red)
        game_over_rect = game_over_surface.get_rect(midtop=(window_x // 2, window_y // 4))
        game_window.blit(game_over_surface, game_over_rect)

        final_score_surface = my_font.render('Final Score: ' + str(score), True, red)
        final_score_rect = final_score_surface.get_rect(midtop=(window_x // 2, window_y // 2))
        game_window.blit(final_score_surface, final_score_rect)

        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]

    food_spawn = True

    # Blit the background image onto the game window
    game_window.blit(background_image, (0, 0))

    # Draw the food
    pygame.draw.rect(game_window, food_color, (food_position[0], food_position[1], 10, 10))

    # Draw the snake
    for i, pos in enumerate(snake_body):
        if i == 0:
            pygame.draw.rect(game_window, snake_head_color, (pos[0], pos[1], 10, 10))
        else:
            game_window.blit(snake_body_image, (pos[0], pos[1]))

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(1, white, 'arial', 20)
    pygame.display.update()
    fps.tick(snake_speed)
