from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

state = 0
radian = 270

# character pos
x, y = 400, 90

while True:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)

    if state == 0:
        x += 8
        if x > 750:
            state += 1
            x -= 8

    elif state == 1:
        y += 8
        if y > 550:
            state += 1
            y -= 8

    elif state == 2:
        x -= 8
        if x < 50:
            state += 1
            x += 8

    elif state == 3:
        y -= 8
        if y < 90:
            state += 1
            y += 8

    elif state == 4:
        x += 8
        if x > 400:
            state += 1
            x -= 8

    elif state == 5:
        x = math.cos(radian / 360 * 2 * math.pi) * 230 + 400
        y = math.sin(radian / 360 * 2 * math.pi) * 230 + 320
        radian += 2
        if radian > 630:
            state = 0
            radian = 270

    delay(0.01)

