#파이게임을 이용해 줄무늬 배경 만들기
# 빨강, 녹색(20x20) 블록으로 줄무늬 만든다.
#블록 그리기 함수를 선언하고 사용한다.
# def draw_block(screen, color, position)

import pygame
import time

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

SCREEN_W = 600
SCREEN_H = 300
SCREEN_SIZE = (SCREEN_W, SCREEN_H)

BLOCK_SIZE = 10

def draw_block(screen, color, position):
    block = pygame.Rect((position[0]*BLOCK_SIZE, position[1]*BLOCK_SIZE),
                        (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)


pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(WHITE)

for bx in range(0, SCREEN_W//BLOCK_SIZE+1, 2):
    for by in range(0, SCREEN_H//BLOCK_SIZE+1, 2):
        draw_block(screen, GREEN, (bx, by))
        draw_block(screen, RED, (bx+1, by))
        draw_block(screen, RED, (bx, by+1))
        draw_block(screen, GREEN, (bx+1, by+1))
        pygame.display.flip()
        time.sleep(0.01)

