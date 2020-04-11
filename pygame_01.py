# pygame 을 이용해 윈도우 생성하기
# pygame 01 py
#2020-04-11

import pygame
import  time

#pygmae 창 만들기
pygame.init()
width = 640
height = 480
win_size = (width, height)
screen = pygame.display.set_mode(win_size)

#1초 동안 창 유지하기
time.sleep(1)