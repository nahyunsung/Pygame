import pygame

pygame.init()

w, h = 640, 480
s = (w,h)
screen = pygame.display.set_mode(s)

player = pygame.image.load('exresources/image/-YzMZYqwoH4.png')
asd = pygame.image.load('exresources/image/HZAcR-tDSCI.png_')
asdt = pygame.image.load('exresources/image/_-SwhhV7tSo.png')


while True:
    screen.fill((0,0,0))

    player_w = player.get_width()
    player_h = player.get_height()
    for x in range(h // player_h + 1):
        for y in range(w // player_w + 1):
            screen.blit(player, (x * player_w, y * player_h))

    asd_h = asd.get_height()
    for x in range(h // asd_h):
        screen.blit(asd, (0, x * asd_h))

    screen.blit(asdt, (300, 300))

    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)