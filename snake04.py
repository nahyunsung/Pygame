import pygame
import time

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

SCREEN_W = 400
SCREEN_H = 400
SCREEN_S = (SCREEN_W, SCREEN_H)

BLOCK_SIZE = 20

def draw_block(screen, color, position):
    block = pygame.Rect((position[0]*BLOCK_SIZE, position[1]*BLOCK_SIZE),
                        (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)

pygame.init()

screen = pygame.display.set_mode(SCREEN_S)
screen.fill(WHITE)

draw_block(screen, RED, (1, 1))
draw_block(screen, RED, (1, 3))
draw_block(screen, RED, (1, 5))
draw_block(screen, RED, (1, 7))
draw_block(screen, GREEN, (3, 1))
draw_block(screen, GREEN, (3, 3))
draw_block(screen, GREEN, (3, 5))
draw_block(screen, GREEN, (3, 7))
draw_block(screen, BLUE, (5, 1))
draw_block(screen, BLUE, (5, 3))
draw_block(screen, BLUE, (5, 5))
draw_block(screen, BLUE, (5, 7))





pygame.display.flip()

time.sleep(3)