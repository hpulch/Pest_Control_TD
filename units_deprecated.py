from pygame import image, Rect
import random


class ant:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.section = 0
        self.img0 = image.load('ant_0.png')
        self.img1 = image.load('ant_1.png')
        self.health = 1000

    def animate(self, frame):
        if frame <= 12:
            return self.img0
        else:
            return self.img1

    def get_x_pos(self):
        return self.x_pos

    def get_y_pos(self):
        return self.y_pos

    def set_x_pos(self, x_pos):
        self.x_pos = x_pos

    def set_y_pos(self, y_pos):
        self.y_pos = y_pos

    def get_section(self):
        return self.section

    def set_section(self, section):
        self.section = section

    def update(self, section, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.section = section

    def get_hit_box(self):
        return Rect(self.x_pos, self.y_pos+25, 50, 25)

    def lose_health(self):
        self.health = self.health - 10

    def get_health(self):
        return self.health


class joe:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_gas = x_pos - 35
        self.y_gas = y_pos + 35
        self.section = 0
        self.img0 = image.load('joe_a.png')
        self.img1 = image.load('joe_r.png')
        self.gas = image.load('gas.png')
        self.hit_box = Rect(self.x_pos-50, self.y_pos+50, 50, 50)

    def animate(self, attacking):
        if attacking:
            return self.img0
        else:
            return self.img1

    def get_x_pos(self):
        return self.x_pos

    def get_y_pos(self):
        return self.y_pos

    def set_x_pos(self, x_pos):
        self.x_pos = x_pos

    def set_y_pos(self, y_pos):
        self.y_pos = y_pos

    def get_hit_box(self):
        return self.hit_box

    def get_attack(self):
        return self.gas
