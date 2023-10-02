import pygame
from pygame.math import Vector2


# Sprite class to be used for the enemies group
class Ant(pygame.sprite.Sprite):

    def __init__(self, waypoints):
        pygame.sprite.Sprite.__init__(self)
        # initialize sprite
        self.image = pygame.image.load("ant_0.png")
        self.rect = self.image.get_rect()
        self.waypoints = waypoints
        self.points = 1

        # initialize vector parameters
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.target = Vector2(self.waypoints[self.target_waypoint])
        self.movement = self.target - self.pos
        self.rect.center = self.pos
        self.velocity = 1

        # Parameters for the hit box overlay
        self.hit_box = pygame.Rect(self.rect.centerx, self.rect.centery, 50, 25)
        self.hit_zone = pygame.Surface((50, 25))
        self.hit_zone.set_alpha(50)
        self.hit_zone.fill((255, 255, 255))

        # Parameters for the red background life-bar
        self.health = 1000
        self.life_box_red = pygame.Rect(self.rect.centerx, self.rect.centery, 50, 5)
        self.life_bar_red = pygame.Surface((50, 5))
        self.life_bar_red.fill((255, 0, 0))
        bar_width = 50 * (self.health / 1000)
        self.life_box_green = pygame.Rect(self.rect.centerx, self.rect.centery, bar_width, 5)
        self.life_bar_green = pygame.Surface((bar_width, 5))
        self.life_bar_green.fill((0, 255, 0))

    def update(self, f):
        try:
            # Try to update vector parameters
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        except IndexError:
            # Except if the waypoint list has ended and the sprite completed path, remove it from the game
            self.kill()

        if self.movement.length() >= self.velocity:
            # translate sprite position in the normalized direction at the set speed
            self.pos += self.movement.normalize() * self.velocity
        else:
            # sprite is close enough, update to the next waypoint
            self.target_waypoint += 1

        # animate the sprite image by toggling the pictures
        if f <= 12:
            self.image = pygame.image.load("ant_0.png")
        else:
            self.image = pygame.image.load("ant_1.png")

        # update other parameters
        self.pos = self.pos
        self.rect.center = self.pos
        self.hit_box.center = (self.rect.centerx, self.rect.centery + 10)
        self.life_box_red.center = (self.rect.centerx, self.rect.centery - 25)
        self.life_box_green.center = (self.rect.centerx, self.rect.centery - 25)

    def overlay(self, surf):
        surf.blit(self.hit_zone, (self.hit_box.x, self.hit_box.y))
        surf.blit(self.life_bar_red, (self.life_box_red.x, self.life_box_red.y))
        surf.blit(self.life_bar_green, (self.life_box_red.x, self.life_box_red.y))

    def update_hit(self, rect, damage):
        if pygame.Rect.colliderect(self.hit_box, rect):
            # update the displayed health bar parameters
            self.health = self.health - damage
            if self.health <= 0:
                return -1
            else:
                bar_width = 50 * (self.health / 1000)
                self.life_box_green = pygame.Rect(self.rect.centerx, self.rect.centery, bar_width, 5)
                self.life_bar_green = pygame.Surface((bar_width, 5))
                self.life_bar_green.fill((0, 255, 0))
                return 0

    def dead_bug(self):
        self.kill()
        return self.points


class Fly(pygame.sprite.Sprite):
    def __init__(self, waypoints):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("fly_0.png")
        self.rect = self.image.get_rect()
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.target = Vector2(self.waypoints[self.target_waypoint])
        self.movement = self.target - self.pos
        self.rect.center = self.pos
        self.velocity = 3

        # Parameters for the hit box overlay
        self.hit_box = pygame.Rect(self.rect.centerx - 50, self.rect.centery, 50, 25)
        self.hit_zone = pygame.Surface((50, 25))
        self.hit_zone.set_alpha(50)
        self.hit_zone.fill((255, 255, 255))

        # Parameters for the life bar overlay
        self.health = 500
        self.life_box_red = pygame.Rect(self.rect.centerx, self.rect.centery, 50, 5)
        self.life_bar_red = pygame.Surface((50, 5))
        self.life_bar_red.fill((255, 0, 0))
        bar_width = 50 * (self.health / 500)
        self.life_box_green = pygame.Rect(self.rect.centerx, self.rect.centery, bar_width, 5)
        self.life_bar_green = pygame.Surface((bar_width, 5))
        self.life_bar_green.fill((0, 255, 0))

    def overlay(self, surf):
        surf.blit(self.hit_zone, (self.hit_box.x, self.hit_box.y))
        surf.blit(self.life_bar_red, (self.life_box_red.x, self.life_box_red.y))
        surf.blit(self.life_bar_green, (self.life_box_red.x, self.life_box_red.y))

    def update(self, f):
        try:
            # Try to update vector parameters
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        except IndexError:
            # Except if the waypoint list has ended and the sprite completed path, remove it from the game
            self.kill()

        if self.movement.length() >= self.velocity:
            # translate sprite position in the normalized direction at the set speed
            self.pos += self.movement.normalize() * self.velocity
        else:
            # sprite is close enough to target waypoint, update to the next waypoint
            self.target_waypoint += 1

        # update the position of other parameters
        self.pos = self.pos
        self.rect.center = self.pos
        self.hit_box.center = (self.rect.centerx, self.rect.centery + 10)
        self.life_box_red.center = (self.rect.centerx, self.rect.centery - 25)
        self.life_box_green.center = (self.rect.centerx, self.rect.centery - 25)

        # animate the sprite image by toggling the pictures
        if f <= 8:
            self.image = pygame.image.load("fly_0.png")
        else:
            self.image = pygame.image.load("fly_1.png")

    def update_hit(self, rect, damage):
        if pygame.Rect.colliderect(self.hit_box, rect):
            # update the displayed health bar parameters
            self.health = self.health - damage
            if self.health <= 0:
                self.kill()
                return -1
            else:
                bar_width = 50 * (self.health / 500)
                self.life_box_green = pygame.Rect(self.rect.centerx, self.rect.centery, bar_width, 5)
                self.life_bar_green = pygame.Surface((bar_width, 5))
                self.life_bar_green.fill((0, 255, 0))
                return 0


class Joe(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)

        # Initialize attributes for the actual sprite Joe
        self.image = pygame.image.load("joe_r.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
        self.attack_status = False
        self.gas = pygame.image.load("gas.png")
        self.hit_box = pygame.Rect(self.rect.centerx - 60, self.rect.centery + 10, 50, 50)

        # Create the attack zone overlay
        self.hit_zone = pygame.Surface((50, 50))
        self.hit_zone.set_alpha(50)
        self.hit_zone.fill((255, 255, 255))
        self.damage = 5

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

    def reset(self):
        self.attack_status = False
        self.image = pygame.image.load("joe_r.png")
