# 1024 x 600 크기의 창 만들기

import pygame, time

pygame.init()
w,h = 1024, 600
s = (w,h)

screen = pygame.display.set_mode(s)

# 창 2초간 유지
pygame.draw.rect(screen, (200,200,200), [10,10,500,50], 2)
pygame.display.flip()

time.sleep(2)