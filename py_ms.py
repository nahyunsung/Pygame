import pygame

# 파이게임 초기화
pygame.init()

# 변수 선언
COL_COUNT = 20
ROW_COUNT = 15
CELL_SIZE = 50
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
# 화면 생성
SCREEN_SIZE = (COL_COUNT * CELL_SIZE, ROW_COUNT * CELL_SIZE)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("py_ms")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # 격자 그리기
    '''
    for x in range(ROW_COUNT):
        for y in range(COL_COUNT):
            a = pygame.Rect((CELL_SIZE * y, CELL_SIZE * x), (CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, GRAY, a, 3)
    '''

    for x in range(ROW_COUNT):
        pygame.draw.line(screen, GRAY, (0, CELL_SIZE * x), (COL_COUNT * CELL_SIZE, x * CELL_SIZE))

    for x in range(COL_COUNT):
        pygame.draw.line(screen, GRAY, (x * CELL_SIZE, 0), (x * CELL_SIZE, ROW_COUNT * CELL_SIZE))

    pygame.display.update()

    # 화면 업데이트

# 파이 게임 종료
pygame.quit()