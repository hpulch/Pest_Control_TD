import pygame
import random


def Completed(surf):

    # Level
    font = pygame.font.Font('freesansbold.ttf', 70)
    text = font.render("Level Completed!", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (400, 320)

    for i in range(170):
        display_rect = pygame.Rect(0, 0, 800, 640)
        display_surf = pygame.Surface((800, 640))
        display_surf.set_alpha(i)
        display_surf.fill((50, 50, 50))
        surf.blit(display_surf, display_rect)
        surf.blit(text, text_rect)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.time.Clock().tick(24)


def Intermediate(surf, title):
    # Level
    font = pygame.font.Font('freesansbold.ttf', 100)
    text = font.render(title, True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (400, 320)
    surf.fill((50, 50, 50))
    surf.blit(text, text_rect)

    # Press any key to begin
    font = pygame.font.Font('freesansbold.ttf', 25)
    text = font.render('Press any key to begin', True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (400, 400)
    surf.blit(text, text_rect)

    pygame.display.flip()
    begin = False
    while not begin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                begin = True


class One:
    def __init__(self, surface):
        self.image = pygame.image.load("path1.png").convert_alpha()
        self.path_mask = pygame.mask.from_surface(self.image)
        self.path = self.path_mask.to_surface()
        self.waypoints = [[-50, 353], [185, 353], [191, 444], [357, 444], [357, 355], [470, 355], [470, 235],
                          [693, 232], [708, 345], [800, 345]]
        self.enemies = [range(2, 11, 2), range(30, 41, 2), range(48, 61, 2)]
        self.points = 0
        self.time = 0

        Intermediate(surface, "Level 1")

    def update(self, frame):
        if frame == 24:
            self.time += 1
        for waves in self.enemies:
            for spawn in waves:
                if self.time == spawn and frame == 1:
                    return True
        return False

    def draw(self, surface):
        time_text = str(120 - self.time)
        font = pygame.font.Font('freesansbold.ttf', 10)
        text = font.render("Time Remaining: "+time_text, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (700, 20)
        surface.blit(text, text_rect)
        surface.blit(self.image, (0, 0))

    def get_waypoints(self):
        scatter = []
        for point in self.waypoints:
            x = point[0] + random.randint(0, 15) - random.randint(0, 15)
            y = point[1] + random.randint(0, 15) - random.randint(0, 15)
            tup = (x, y)
            scatter.append(tup)
        return scatter

    def track_points(self, points):
        self.points += points
        print(self.points)

    def next_level(self, surface):
        if self.time == 120:
            Completed(surface)
            Intermediate(surface, "Level 2")
            return 2
        else:
            return 1


class Two:
    def __init__(self, surface):
        self.image = pygame.image.load("path1.png").convert_alpha()
        self.path_mask = pygame.mask.from_surface(self.image)
        self.path = self.path_mask.to_surface()
        self.waypoints = [[-50, 353], [185, 353], [191, 444], [357, 444], [357, 355], [470, 355], [470, 235],
                          [693, 232], [708, 345], [800, 345]]
        self.enemies = [range(2, 11, 2), range(30, 41, 2), range(48, 61, 2)]
        self.points = 0
        self.time = 0

    def update(self, frame):
        if frame == 24:
            self.time += 1
        for waves in self.enemies:
            for spawn in waves:
                if self.time == spawn and frame == 1:
                    return True
        return False

    def draw(self, surface):
        time_text = str(120 - self.time)
        font = pygame.font.Font('freesansbold.ttf', 10)
        text = font.render("Time Remaining: "+time_text, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (700, 20)
        surface.blit(text, text_rect)
        surface.blit(self.image, (0, 0))

    def get_waypoints(self):
        scatter = []
        for point in self.waypoints:
            x = point[0] + random.randint(0, 15) - random.randint(0, 15)
            y = point[1] + random.randint(0, 15) - random.randint(0, 15)
            tup = (x, y)
            scatter.append(tup)
        return scatter

    def track_points(self, points):
        self.points += points
        print(self.points)

    def next_level(self, surface):
        if self.time == 120:
            Completed(surface)
            return 3
        else:
            return 2
