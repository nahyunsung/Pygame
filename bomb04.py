# 피하기 게임 - 덩 이미지 그리기

import pygame
import random

# 변수 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_WHDIT = 600
SCREEN_HIGHT = 800
SCREEN_SIZE = (SCREEN_WHDIT,SCREEN_HIGHT)


# 파이게임 초기화 및 설정
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.key.set_repeat(1)
clock = pygame.time.Clock()

# 이미지 불러오기
player_url = 'resources/d_image/dog.png'
player_img = pygame.image.load(player_url)
player_pos =player_img.get_rect(centerx = SCREEN_WHDIT//2, bottom = SCREEN_HIGHT)

# 적 이미지 불러오기
enemy_url = 'resources/d_image/ddong.png'
enemy_img = pygame.image.load(enemy_url)
#enemies = list()
enemies = []
for cnt in range(3):
    enemy_pos = enemy_img.get_rect(left = 150*cnt+100, top = 100)
    enemies.append(enemy_pos)
    print(enemy_pos)

#게임 루프
while True:
    #화면 배경색으로 지우기
    screen.fill(BLACK)

    #키 입력 처리
    event =pygame.event.poll()

     # 파이게임 종료 처리
    if event.type == pygame.QUIT:
        exit()
    #주인공 이동처리
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_pos.left -= 5
        elif event.key == pygame.K_RIGHT:
            player_pos.left += 5
        #주인공 벽처리하기
        if player_pos.left < 0:
            player_pos.left = 0
        elif player_pos.right > SCREEN_WHDIT:
            player_pos.right = SCREEN_WHDIT

    # 적 내려오기
    for one in enemies:
        one.top += 5
        if one.bottom > SCREEN_HIGHT:
            one.top = -100
            one.left = random.randint(0, SCREEN_WHDIT - enemy_img.get_width())

    #이미지 그리고 화면 업데이트
    screen.blit(enemy_img, enemy_pos)
    for one in enemies:
        screen.blit(enemy_img, one)
    pygame.display.flip()

    screen.blit(player_img, player_pos)
    pygame.display.flip()

    # 프레임 설정하기
    clock.tick(60)
