# 피하기 게임 - bomb03
#플레이어 이동하기

import pygame

#변수 설정
WHITE = (0, 0, 0)
BLACK = (255, 255, 255)

SCREEN_WIDHT = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDHT, SCREEN_HEIGHT)

#파이게임 초기화 및 화면 설정
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

# 키 반복 설정하기
pygame.key.set_repeat(1)

#이미지 불러오기(화면 중앙 하단: centerx, bottom 속성 사용하기
player_url = 'resources/d_image/dog.png'
player_img = pygame.image.load(player_url)
player_pos = player_img.get_rect(centerx = SCREEN_WIDHT//2, bottom = SCREEN_HEIGHT)

#게임 루프 생성
while True:
    #화면 배경 설정
    screen.fill(BLACK)

    #키 입력 처리
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()
    elif event.type == pygame.KEYDOWN:
        #방향키로 캐릭터 이동하기
        if event.key == pygame.K_LEFT:
            player_pos.left -= 5
        elif event.key == pygame.K_RIGHT:
            player_pos.left += 5
        # 벽 충돌 처리
        if player_pos.left < 0:
            player_pos.left = 0
        if player_pos.right > SCREEN_WIDHT:
            player_pos.right = SCREEN_WIDHT
    #주인공 이미지 출력하기
    screen.blit(player_img, player_pos)
    pygame.display.flip()

    #초당 프레임 설정
    clock.tick(60)