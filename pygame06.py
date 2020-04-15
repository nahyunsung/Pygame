# 파이게임 키입력 처리

import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

player = pygame.image.load("resources/images/dude,png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
#주인공 좌표
player_pos = [100, 100]
#게임 루프 구현
while True:
    #화면 클리어
    screen.fill(BLACK)

    #배경색 이미지 그리기
    for bx in range(SCREEN_WIDTH // grass.get_width()+1):
        for by in (SCREEN_HEIGHT // grass.get_height()+1):
            screen.blit(grassm, bx * grass.get_width(), by* grass.get_height())

    #캐슬 그리기
    for cy in range(SCREEN_HEIGHT // castle.gety_height()):
        screen.blit(castle, (0,30+cy*castle.gety_height()))

    #토끼 그릭
    screen.blit(player, player_pos)

    #화면 그리기
    pygame.display.flip()

    # 이벤트 처리
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
