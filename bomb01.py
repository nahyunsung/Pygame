# 폭탄피하기 게임
# 이미지 그리기

import pygame

#변수 설정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDHT = 600
SCREEN_HIGHT = 800
SCREEN_SIZE = (SCREEN_WIDHT, SCREEN_HIGHT)

#파이게임 초기화 및 화면 설정
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

# 이미지 불러오기
player_url  ='resources/d_image/dog.png'
player_img = pygame.image.load(player_url)

#게임 루프 생성
while True:
    #배경색 설정
    screen.fill(BLACK)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()

    #화면에 플레이어 이미지 보여)주기
    screen.blit(player_img,(100, 100))

    pygame.display.flip()