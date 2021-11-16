import random
from pico2d import *
import game_world
import game_framework


# Bird Run Speed
# 픽셀당 3cm로 고정
# 새는 시속 50km의 속도로 이동
# 속도를 Meter per sec 로 변환 (RUN_SPEED_MPS)
# 속도를 Pixel per sec 로 변환 (RUN_SPEED_PPS)
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 50.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed
TIME_PER_ACTION = 0.5  # 시간(1 프레임)당 발생하는 액션 횟수
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION  # 날개짓 속도
FRAMES_PER_ACTION = 14  # 스프라이트 프레임 개수

# dir 이동 방향
direction = [1, -1]

class Bird:
    image = None
    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.dir = direction[random.randint(0, 1)]
        self.x, self.y, = random.randint(0, 1500), random.randint(200, 550)
        self.fid = 0
        self.speed = RUN_SPEED_PPS
        self.size = (PIXEL_PER_METER * 3, PIXEL_PER_METER * 3)

    def get_bb(self):
        pass

    def draw(self):
        self.image.clip_draw(int(self.fid) * 100, 0, 100, 100, self.x, self.y, *self.size)

    def update(self):
        self.fid = (self.fid + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        if self.dir == 1 and self.x > 1600:
            self.dir = -1
            self.x = 1600
        elif self.dir == -1 and self.x < 0:
            self.dir = 1
            self.x = 0
        self.x += self.dir * self.speed * game_framework.frame_time


# class Bird