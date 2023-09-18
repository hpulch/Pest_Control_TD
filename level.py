from pygame import image, Rect
from pygame import display
import units


def move_right(x_pos, fps):
    x_pos = x_pos + fps
    return x_pos


def move_down(y_pos, fps):
    y_pos = y_pos + fps
    return y_pos


def move_up(y_pos, fps):
    y_pos = y_pos - fps
    return y_pos


class credit:
    def __init__(self):
        display.set_caption("Pest Control TD  --Credits--")
        self.map = image.load('credit_page.png')
        self.pos = 0, 0


class one:
    def __init__(self):
        display.set_caption("Pest Control TD  --Level One--")
        self.map = image.load('map_level_1.png')
        self.pos = 0, 0
        self.path = (-50, 310), (170, 310), (170, 420), (330, 420), (330, 310), (450, 310), (450, 190), (680, 190), (
            680, 310), (800, 310)
        self.enemies = [range(2, 11, 2), range(30, 41, 2), range(48, 61, 2)]

    def trail(self, section, x_pos, y_pos, fps):
        if section == 0:
            x_pos = move_right(x_pos, fps)
            if x_pos >= self.path[1][0]:
                section = 1
        if section == 1:
            y_pos = move_down(y_pos, fps)
            if y_pos >= self.path[2][1]:
                section = 2
        if section == 2:
            x_pos = move_right(x_pos, fps)
            if x_pos >= self.path[3][0]:
                section = 3
        if section == 3:
            y_pos = move_up(y_pos, fps)
            if y_pos <= self.path[4][1]:
                section = 4
        if section == 4:
            x_pos = move_right(x_pos, fps)
            if x_pos >= self.path[5][0]:
                section = 5
        if section == 5:
            y_pos = move_up(y_pos, fps)
            if y_pos <= self.path[6][1]:
                section = 6
        if section == 6:
            x_pos = move_right(x_pos, fps)
            if x_pos >= self.path[7][0]:
                section = 7
        if section == 7:
            y_pos = move_down(y_pos, fps)
            if y_pos >= self.path[8][1]:
                section = 8
        if section == 8:
            x_pos = move_right(x_pos, fps)
            if x_pos >= self.path[9][0]:
                section = "Complete"
        return section, x_pos, y_pos

    def spawn(self, time, frame):
        for waves in self.enemies:
            for spawn in waves:
                if time == spawn and frame == 1:
                    return True
        return False


# def path2(self):

