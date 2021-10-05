from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y, handx, speed
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
             running = False
    x += dx/distance * speed
    y += dy/distance * speed
    sprite_change()
    random_hand(x, handx)


def get_distance():
    global x, y, handx, handy, dx, dy, distance
    dx, dy = handx - x, handy - y
    distance = math.sqrt(dx**2 + dy**2)


def sprite_change():
    global state
    if dx > 0:
        state = 1
    else:
        state = 0


def random_hand(x1, x2):
    global handx, handy, dx
    if dx < 0:
        if x1 < x2:
            handx, handy = random.randrange(0, KPU_WIDTH), random.randrange(0, KPU_HEIGHT)
            get_distance()
    if dx > 0:
        if x1 > x2:
            handx, handy = random.randrange(0, KPU_WIDTH), random.randrange(0, KPU_HEIGHT)
            get_distance()


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
handx, handy = random.randrange(200, KPU_WIDTH-200), random.randrange(200, KPU_HEIGHT-200)
dx, dy, distance = 0, 0, 0
frame, state = 0, 0
speed = 5
hide_cursor()
get_distance()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, state * 100, 100, 100, x, y)
    hand_arrow.clip_draw(0, 0, 50, 52, handx, handy)
    update_canvas()
    delay(0.01)
    frame = (frame + 1) % 8
    handle_events()

close_canvas()