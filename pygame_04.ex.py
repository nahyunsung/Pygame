#파이게임 창 만들고 이미지 불러오기
#이미지 크기는 300x300이내 사이즈
# pixlr, photopea에서 편집 혹은 투명 배경 이미지 추천(png)

import pygame

pygame.init()
w = 640
h = 480
size = (w,h)
screen = pygame.display.set_mode(size)

player = pygame.image.load('exresources/image/star.png_')

while True:
    screen.fill((0,0,0))
    screen.blit(player, (100,100))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

