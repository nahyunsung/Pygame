import pygame

WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#화면 크기 상수 설정
SCREEN_W = 400
SCREEN_H = 400
SCREEN_S = (SCREEN_W, SCREEN_H)


# 블록 크기 설정
BLOCK_S = 20

#블록 그리기 함수 설정
def draw_block(screen, color, position):
    block = pygame.Rect((position[0]*BLOCK_S, position[1]*BLOCK_S),
                        (BLOCK_S, BLOCK_S))
    pygame.draw.rect(screen, color, block)

pygame.init()
screen = pygame.display.set_mode(SCREEN_S)

#블록 위치 초기화
block_p = [0,0]

while True:
    #이벤트 처리
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            # 블록 이동 코드 작성
            if event.key == pygame.K_RIGHT:
                block_p[0] += 1
            if event.key == pygame.K_LEFT:
                block_p[0] -= 1
            if event.key == pygame.K_UP:
                block_p[1] -= 1
            if event.key == pygame.K_DOWN:
                block_p[1] += 1

    screen.fill(WHITE)
    draw_block(screen, GREEN, block_p)
    pygame.display.flip()
