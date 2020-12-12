import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((255, 255, 255)) # 화면 흰색 채우기

    # 빨간색 정사각형 그리기
    pygame.draw.rect(screen , (255, 0, 0), (10, 20, 100, 50))

    # 빨간색 직사각형 그리기 (굵기 3)
    pygame.draw.rect(screen, (255, 0, 0), (150, 10, 100, 30), 3)

    # 녹색 100 80 좌표에 가로 80 세로 50 사각형 그리기 (단의 픽셀)
    pygame.draw.rect(screen, (0, 255, 0), (100, 80, 80, 50) )

    # 파란색 200, 60 가로 140 세로 80 직사각형
    pygame.draw.rect(screen, (0, 0, 255), (200, 60, 140, 80))

    # 노란색 30 160 100 50 직사각형 (R+G = Y)
    pygame.draw.rect(screen, (255, 255, 0), (30, 160, 100, 50))

    # 파란선 (100, 100), (200, 200)
    pygame.draw.line(screen, (0, 0, 255), (100, 100), (200, 200))

    # 빨간선 세로 80 가로 100~200 사이의 수편선
    pygame.draw.line(screen, (255, 0, 0 ), (10, 80), (200, 80))

    # 녹색  가로 250 화면 분활 수직선 그리기
    pygame.draw.line(screen, (0, 255, 0), (250,0), (250, 300))

    # 화면 업데이트
    pygame.display.update()


pygame.quit()