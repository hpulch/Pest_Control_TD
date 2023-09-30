import pygame


class level:
    def __init__(self):
        self.image = pygame.image.load("path1.png")

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, (0, 0))


# Sprite class to be used for the enemies group
class Ant(pygame.sprite.Sprite):

    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ant_0.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
        self.velocity = [1, 0]

        self.hit_box = pygame.Rect(x_pos-25, y_pos, 50, 25)
        self.hit_zone = pygame.Surface((50, 25))
        self.hit_zone.set_alpha(50)
        self.hit_zone.fill((255, 255, 255))

    def update(self, f):
        self.rect.move_ip(self.velocity)
        self.hit_box.move_ip(self.velocity)
        if frame <= 12:
            self.image = pygame.image.load("ant_0.png")
        else:
            self.image = pygame.image.load("ant_1.png")

    def overlay(self, surface):
        surface.blit(self.hit_zone, (self.hit_box.x, self.hit_box.y))


class Fly(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("fly_0.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
        self.velocity = [3, 0]

        self.hit_box = pygame.Rect(x_pos-25, y_pos, 50, 25)
        self.hit_zone = pygame.Surface((50, 25))
        self.hit_zone.set_alpha(50)
        self.hit_zone.fill((255, 255, 255))

    def overlay(self, surface):
        print("HEY!")
        surface.blit(self.hit_zone, (self.hit_box.x, self.hit_box.y))

    def update(self, f):
        self.rect.move_ip(self.velocity)
        self.hit_box.move_ip(self.velocity)
        if frame <= 8:
            self.image = pygame.image.load("fly_0.png")
        else:
            self.image = pygame.image.load("fly_1.png")


class Joe(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)

        # Initialize attributes for the actual sprite Joe
        self.image = pygame.image.load("joe_r.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
        self.attack_status = False
        self.gas = pygame.image.load("gas.png")
        self.hit_box = pygame.Rect(x_pos-60, y_pos+10, 50, 50)

        # Create the attack zone overlay
        self.hit_zone = pygame.Surface((50, 50))
        self.hit_zone.set_alpha(50)
        self.hit_zone.fill((255, 255, 255))

    def update(self, sprite):

        # update Joe to toggle between resting and attacking
        if pygame.Rect.colliderect(self.hit_box, sprite):

            # Joe is attacking
            self.attack_status = True
            self.image = pygame.image.load("joe_a.png")
        else:

            # Joe is resting
            self.attack_status = False
            self.image = pygame.image.load("joe_r.png")

    def overlay(self, surface):
        # blit an image to the attacking position
        if self.attack_status:
            # Gas attack
            surface.blit(self.gas, (self.hit_box.x, self.hit_box.y))
        else:
            # Target area but no gas
            surface.blit(self.hit_zone, (self.hit_box.x, self.hit_box.y))

    def get_status(self):
        if self.attack_status:
            return True
        else:
            return False


def frames(f, s):
    """
    Refresh rate is set to 24 FPS
    Track frames to use for animating objects
    Track time in seconds to generate waves of enemies
    """
    f += 1
    if f >= 25:
        f = 1
        s = s + 1
    return f, s


pygame.init()
screen = pygame.display.set_mode((800, 640))
L1 = level()

ant = Ant(-50, 310)
fly = Fly(-200, 300)
enemies = pygame.sprite.Group()
allies = pygame.sprite.Group()

enemies.add(fly)
enemies.add(ant)

frame = 1
sec = 1
running = True
while running:

    screen.fill((0, 128, 0))
    L1.draw(screen)
    enemies.update(frame)

    for ally in allies:
        for bug in enemies:
            # For each ally compare it's hit_box to every bug and update its attack status
            ally.update(bug)
            if ally.get_status():
                # If ally if attacking, stop checking bugs and do not update so he continues to attack first bug seen
                break

    # blit the transparent overlay first and then blit the sprite image overtop
    for bug in enemies:
        bug.overlay(screen)
    enemies.draw(screen)

    # blit the sprite image first and blit the transparent overlay overtop
    allies.draw(screen)
    for joe in allies:
        joe.overlay(screen)



    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pass
            elif event.key == pygame.K_q:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                allies.add(Joe(mouse_x, mouse_y))

    frame, sec, = frames(frame, sec)
    pygame.time.Clock().tick(24)
