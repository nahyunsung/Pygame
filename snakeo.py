import pygame
import time

w = (255, 255, 255)
ba = (0,0,0)
r = (255, 0, 0)
g = (0, 255, 0)
bl = (0,0,255)

s_w = 400
s_h = 400
s_s = (s_w, s_h)

pygame.init()
screen = pygame.display.set_mode(s_s)
screen.fill(w)

#블록 그리기
BLOCK_SIZE = 20
block_red = pygame.Rect((1*BLOCK_SIZE, 1*BLOCK_SIZE),
                        (BLOCK_SIZE, BLOCK_SIZE))
pygame.draw.rect(screen, r, block_red)

block_green = pygame.Rect((1*BLOCK_SIZE, 3*BLOCK_SIZE),
                        (BLOCK_SIZE, BLOCK_SIZE))
pygame.draw.rect(screen, g, block_green)

block_blue = pygame.Rect((1*BLOCK_SIZE, 5*BLOCK_SIZE),
                        (BLOCK_SIZE, BLOCK_SIZE))
pygame.draw.rect(screen, bl, block_blue)

pygame.display.flip()

time.sleep(3)