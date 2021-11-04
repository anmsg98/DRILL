from pico2d import *
import random
# Game object class here

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
open_canvas()
# initialization code
grass = load_image('grass.png')
running = True
class Ball:
    balls = []
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = (random.randint(50, 750), 599)
        self.dy = 0
        self.radius = self.image.h // 2
        # print('Radius = %d' % self.radius)
    def draw(self):
        self.image.draw(self.x, self.y)
    def update(self):

        gravity = random.random()
        self.dy -= gravity
        if self.y > 60:
            self.y += self.dy
        else:
            self.y = 60

Balls = [Ball() for i in range(20)]

# game main loop code
while(running==True):
    clear_canvas()
    grass.draw(400, 30)
    for ball in Balls:
        ball.draw()
        ball.update()

    update_canvas()
    get_events()

close_canvas()
# finalization code