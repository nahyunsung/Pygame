import pygame

# 파이게임 초기화
pygame.init()

# 색상 설정
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)


# 블록 클래스
# 공(타원, 이동), 패들(사각형, 이동), 벽돌(사각형)
class Block:
    # 클래스의 생성자
    def __init__(self, color, rect, speed = 0):
        self.color = color
        self.rect = rect
        self.speed = speed
        self.x_dir = 1
        self.y_dir = -1

    # 이동 (move)
    def move(self):
        self.rect.centerx += self.x_dir * self.speed
        self.rect.centery += self.y_dir * self.speed

    # 그리기(draw) 메서드
    def draw(self):
        if self.speed == 0:
            pygame.draw.rect(SCREEN, self.color, self.rect)
        else:
            pygame.draw.ellipse(SCREEN, self.color, self.rect)


# 화면 생성
SC_WIDTH, SC_HEIGHT = 600, 800
SC_SIZE = (SC_WIDTH, SC_HEIGHT)
SCREEN = pygame.display.set_mode(SC_SIZE)
pygame.display.set_caption("PY")

# block 클래스로 객테 만들기
PADDLE = Block(YELLOW, pygame.Rect(300, 700, 100, 30))
BALL = Block(YELLOW, pygame.Rect(300, 400, 20, 20), 10)
BLOCKS = []

block_colors = [(255, 0, 0), (250, 160, 0), (230, 230, 0),
                (0, 130, 0), (130, 0, 130), (0, 0, 250)]

for y_pos, color in enumerate(block_colors):
    for x_pos in range(5):
        BLOCKS.append(Block(color, pygame.Rect(x_pos * 100 + 60, y_pos * 50 + 40, 80, 30)))

# 키 반복 입력
pygame.key.set_repeat(5, 5)

# 폰트 설정
py_font = pygame.font.SysFont(None, 80)
clear = py_font.render("CLEAR", True, YELLOW)
game_over = py_font.render("GAME_OVER", True, YELLOW)


# 프레임
FPS = pygame.time.Clock()

# 게임 루프
running = True
while running:
    FPS.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and PADDLE.rect.centerx > 0:
                PADDLE.rect.centerx -= 10
            elif event.key == pygame.K_RIGHT and PADDLE.rect.centerx < SC_WIDTH:
                PADDLE.rect.centerx += 10

    # 공 이동하기
    if BALL.rect.centery < 1000:
        BALL.move()

    # 공과 벽 충돌
    if BALL.rect.centerx < 0 or BALL.rect.centerx > SC_WIDTH:
        BALL.x_dir *= -1

    if BALL.rect.centery < 0:
        BALL.y_dir *= -1

    # 공과 패들 충돌
    if PADDLE.rect.colliderect(BALL.rect):
        BALL.y_dir *= -1

    # 공과 벽돌 충돌
    pre_len = len(BLOCKS)
    BLOCKS = [one for one in BLOCKS if not one.rect.colliderect(BALL.rect)]
    if pre_len != len(BLOCKS):
        BALL.y_dir *= -1


    # 베경 색 칠하기
    SCREEN.fill(BLACK)

    PADDLE.draw()
    BALL.draw()
    for one in BLOCKS:
        one.draw()

    if BALL.rect.centery > SC_HEIGHT and len(BLOCKS) > 0:
        SCREEN.blit(game_over, ((SC_WIDTH // 2) - (game_over.get_rect().width // 2), SC_HEIGHT // 2))

    if len(BLOCKS) == 0:
        SCREEN.blit(clear, ((SC_WIDTH // 2) - (clear.get_rect().width // 2), SC_HEIGHT // 2))
    # 화면 업데이트
    pygame.display.update()


# 파이 게임 종료
pygame.quit()