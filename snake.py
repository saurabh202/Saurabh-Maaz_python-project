import pygame
import time
import random

pygame.init()

black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

SNAKE_SQUARE_DIMENSIONS = 10

TOTAL_COLS = 60
TOTAL_ROWS = 40
surface_width = TOTAL_COLS * SNAKE_SQUARE_DIMENSIONS # 60 columns
surface_height = TOTAL_ROWS * SNAKE_SQUARE_DIMENSIONS # 40 rows
SNAKE_SPEED = 15

font_style = pygame.font.SysFont("bahnschrift", 30)

surface = pygame.display.set_mode((surface_width, surface_height))
pygame.display.set_caption('SNAKE GAME')

clock = pygame.time.Clock()

def draw_single_block(snake_block,color):
    vertical_position = snake_block[0] * SNAKE_SQUARE_DIMENSIONS
    horizontal_position = snake_block[1] * SNAKE_SQUARE_DIMENSIONS
    pygame.draw.rect(surface, color, [vertical_position, horizontal_position, SNAKE_SQUARE_DIMENSIONS, SNAKE_SQUARE_DIMENSIONS]) # origin position and dimensions

def draw_snake(snake_list):
    for snake_block in snake_list:
        draw_single_block(snake_block,green)

def move_block(col, row , direction):
    if direction == "LEFT":
        col = col -1
    if direction == "RIGHT":
        col = col +1
    if direction == "UP":
        row = row - 1
    if direction == "DOWN":
        row = row + 1

    return [col,row]

def detect_direction(direction, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            return "LEFT"
        elif event.key == pygame.K_RIGHT:
            return "RIGHT"
        elif event.key == pygame.K_UP:
            return "UP"
        elif event.key == pygame.K_DOWN:
            return "DOWN"
    return direction

def create_food_block():
    foodx = round(random.randrange(0, 59))
    foody = round(random.randrange(0, 39))
    return [foodx,foody]

def draw_message(msg, color):
        message = font_style.render(msg, True, color)
        message = surface.blit(message, [surface_width / 3, surface_height / 4])
def draw_submessage(msg, color):
        submessage = font_style.render(msg, True, color)
        submessage = surface.blit(submessage, [surface_width / 2.4, surface_height / 2])
        
def gameLoop():
    game_over = False
    game_close = False
    x1 = 30
    y1 = 20
    direction = "UP"
    snake_list = [[30,21],[30,20]]
    food_block = create_food_block()
    snake_length = 2
    
    while not game_over:
        for event in pygame.event.get():
            direction = detect_direction(direction, event)
        x1,y1 = move_block(x1,y1,direction)
        
        if x1 >= TOTAL_COLS or x1 < 0 or y1 >= TOTAL_ROWS or y1 < 0:
            game_over = True
        surface.fill(black)
        draw_single_block(food_block,red)
        snake_list.append([x1,y1])
        
        if(len(snake_list)>=snake_length):
            del snake_list[0]
        draw_snake(snake_list)
        pygame.display.update()
        
        if x1 == food_block[0] and y1 == food_block[1]:
            food_block = create_food_block()
            snake_length += 1

        clock.tick(SNAKE_SPEED)

    while not game_close:
        surface.fill(black)
        draw_message("Enter to play again",green)
        draw_submessage(" Q to QUIT ", red)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_close = True
                else:
                    gameLoop()

gameLoop()
pygame.quit()
