import os
import pygame
import random

def draw_rect(object_rect):
    rect_color = (255, 0, 0)  # Màu đỏ, bạn có thể đổi sang màu khác tùy thích
    border_thickness = 3  # Độ dày của đường viền
    pygame.draw.rect(screen, rect_color, object_rect, border_thickness)

def draw_floor():
    global floor_x_pos
    floor_x_pos -= 2
    if floor_x_pos <= -SCREEN_WIDTH:
        floor_x_pos = 0
    screen.blit(floor, (floor_x_pos, SCREEN_HEIGHT - floor.get_height()))
    screen.blit(floor, (floor_x_pos + SCREEN_WIDTH, SCREEN_HEIGHT - floor.get_height()))

def draw_bird():
    global bird_movement, bird_rect
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_draw, (bird_rect.x - 4, bird_rect.y - 4))
    # draw_rect(bird_rect)

def rotate_bird():
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
    return new_bird

def create_pipe():
    random_pipe_pos = random.choice([20, 30, 40, 50, 60, 70, 80])
    bottom_pipe = pipe_surface.get_rect(
        midtop=(SCREEN_WIDTH + 50, SCREEN_HEIGHT // 100 * random_pipe_pos + 70)
    )
    top_pipe = pipe_surface.get_rect(
        midbottom=(SCREEN_WIDTH + 50, SCREEN_HEIGHT // 100 * random_pipe_pos - 70)
    )
    return bottom_pipe, top_pipe

def draw_pipe():
    global pipe_index
    if len(pipe_list) == 0:
        return
    if pipe_list[0].centerx < -50:
        pipe_list.pop(0)
        pipe_list.pop(0)
        pipe_index -=2
    for pipe_rect in pipe_list:
        pipe_rect.centerx -= 5
        if pipe_rect.bottom >= SCREEN_HEIGHT:
            screen.blit(pipe_surface, pipe_rect)
        else:
            screen.blit(flip_pipe, pipe_rect)

def check_collision():
    if len(pipe_list) == 0:
        return False
    for pipe_rect in pipe_list:
        if bird_rect.colliderect(pipe_rect):
            return False
    if bird_rect.top <= 0 or bird_rect.bottom >= SCREEN_HEIGHT - floor.get_height():
        return True
    return False

def check_passed_pipe(): 
    global score, pipe_index
    if len(pipe_list) == 0 or len(pipe_list) <= pipe_index:
        return
    pipe_rect = pipe_list[pipe_index] 
    if pipe_rect.midright[0] < bird_rect.midleft[0]:
        score += 1
        pipe_index += 2
        point_sound.play()

def score_display():
    score_text = game_font.render(f"Score: {score}", True, (255, 255, 255))
    high_score_text = game_font.render(
        f"High Score: {high_score}", True, (255, 255, 255)
    )
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 20))
    if not GAME_ACTIVE:
        screen.blit(
            high_score_text, (SCREEN_WIDTH // 2 - high_score_text.get_width() // 2, 60)
        )

# khởi tạo cửa sổ game
pygame.init()
SCREEN_WIDTH = 432
SCREEN_HEIGHT = 768
GAME_ACTIVE = True
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

script_path = os.path.realpath(__file__)
script_dir = os.path.dirname(script_path)
assets_dir = os.path.join(script_dir, "assets")
font_path = os.path.join(assets_dir, "Transformers Movie.ttf")
game_font = pygame.font.Font(font_path, 40)
score = 0
high_score = 0

# hình nền
bg_path = os.path.join(assets_dir, "background-night.png")
bg = pygame.image.load(bg_path).convert()
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

# floor
floor = pygame.image.load("./Learn python with Projects/assets/floor.png").convert()
floor = pygame.transform.scale(floor, (SCREEN_WIDTH, floor.get_height()))
floor_x_pos = 0

# bird
bird_path = "./Learn python with Projects/assets/yellowbird-%sflap.png"
bird_mid = pygame.image.load(bird_path % "mid").convert_alpha()
bird_down = pygame.image.load(bird_path % "down").convert_alpha()
bird_up = pygame.image.load(bird_path % "up").convert_alpha()
bird_list = [bird_down, bird_mid, bird_up]
bird_list = list(map(lambda x: pygame.transform.scale2x(x), bird_list))
bird_index = 2
bird = bird_list[bird_index]
bird_small = pygame.transform.scale(
    bird, (bird.get_width() - 8, bird.get_height() - 8)
)
bird_rect = bird_small.get_rect(center=(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
gravity = 0.5
bird_movement = 0
birdflap = pygame.USEREVENT + 1
pygame.time.set_timer(birdflap, 200)

#sound
flap_sound = pygame.mixer.Sound("./Learn python with Projects/sound/sfx_wing.wav")
hit_sound = pygame.mixer.Sound("./Learn python with Projects/sound/sfx_hit.wav")
point_sound = pygame.mixer.Sound("./Learn python with Projects/sound/sfx_point.wav")

# tạo pipe
pipe_path = os.path.join(assets_dir, "pipe-green.png")
pipe_surface = pygame.image.load(pipe_path).convert()
pipe_surface = pygame.transform.scale(
    pipe_surface, (pipe_surface.get_width() * 2, SCREEN_HEIGHT)
)
flip_pipe = pygame.transform.flip(pipe_surface, False, True)
spawpipe = pygame.USEREVENT
pygame.time.set_timer(spawpipe, 1000)
pipe_list = []
pipe_index = 0

#màn hình kết thúc
over_path = os.path.join(assets_dir, "message.png")
over = pygame.image.load(over_path).convert_alpha()
over = pygame.transform.scale2x(over)
over_rect = over.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

# chạy vòng lặp để update cửa sổ game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bird_movement > 7:
                    bird_movement = -5
                elif bird_movement > 0:
                    bird_movement = bird_movement - 12
                else:
                    bird_movement = -12
                flap_sound.play()
                if GAME_ACTIVE == False:
                    pipe_list.clear()
                    pipe_index = 0
                    bird_rect.center = (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2)
                    bird_movement = -10
                    score = 0
                    GAME_ACTIVE = True
        if event.type == spawpipe:
            pipe_list.extend(create_pipe())
        if event.type == birdflap:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
            bird = bird_list[bird_index]

    screen.blit(bg, (0, 0))
    if GAME_ACTIVE:
        bird_draw = rotate_bird()
        draw_bird()
        draw_pipe()
        check_passed_pipe()
        if check_collision():
            hit_sound.play()
            GAME_ACTIVE = False
            if score > high_score:
                high_score = score
    else:
        screen.blit(over, over_rect)
    score_display()
    draw_floor()
    pygame.display.update()
    clock.tick(60)
