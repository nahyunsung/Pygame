import pygame
import random

# 화면 초기화
pygame.init()
SCREEN_WIDHT = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDHT, SCREEN_HEIGHT)

# 변수 초기화
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("PYSNAKE")
clock = pygame.time.Clock()

# 색상
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)

# 셀
CELL_SIZE = 40
COL_COUNT = SCREEN_WIDHT//CELL_SIZE
ROW_COUNT = SCREEN_HEIGHT//CELL_SIZE

# 이동방향
LEFT = 0
RIGHT = 1
UP = 3
DOWN = 4
direction = DOWN

# 점수
score = 0

# 글꼴 설정
score_font = pygame.font.SysFont("comicsans", 40)

# 뱀 좌표 리스트 만들기(화면 중앙)
s_pos = (SCREEN_WIDHT//2, SCREEN_HEIGHT//2)
bodies = [s_pos]

# 먹이 생성 함수 add_food()
def add_food():
    while True:
        c_idx = random.randint(0, COL_COUNT-1)
        r_idx = random.randint(0, ROW_COUNT-1)
        f_pos = (c_idx, r_idx)

# 먹이 10개 좌표 리스트
foods = []
for _ in range(10):
    add_food()
# 게임 루프

