import pygame
from pygame.locals import Rect

import level
import shop
import units

pygame.init()
screen = pygame.display.set_mode((800, 640))
stage = level.one()
enemies = []
allies = []

fps = 24
frame = 1
sec = 0
running = True

while running:

    screen.blit(stage.map, stage.pos)
    sec1 = Rect(-50, 330, 263, 50)
    sec2 = Rect(163, 380, 50, 110)
    sec3 = Rect(213, 440, 167, 50)
    sec4 = Rect(330, 330, 50, 130)
    sec5 = Rect(380, 330, 120, 50)
    sec6 = Rect(450, 205, 50, 140)
    sec7 = Rect(500, 205, 225, 50)
    sec8 = Rect(675, 205, 50, 175)
    sec9 = Rect(675, 330, 200, 50)

    pygame.draw.rect(screen, (255, 0, 0), Rect.union(sec1, sec2))

    # Spawn enemies, move them through the level path, animate their motion
    if stage.spawn(sec, frame):
        enemies.append(units.ant(-50, 310))

    target = []
    for bug in enemies:
        section, x_pos, y_pos = stage.trail(bug.get_section(), bug.get_x_pos(), bug.get_y_pos(), 1)
        bug.update(section, x_pos, y_pos)
        # pygame.draw.rect(screen, (255, 0, 0), bug.get_hit_box())
        screen.blit(bug.animate(frame), (bug.get_x_pos(), bug.get_y_pos()))
        target.append(bug.get_hit_box())

    dead_bugs = []
    for bug in enemies:
        for dude in allies:
            if pygame.Rect.colliderect(dude.get_hit_box(), bug.get_hit_box()):
                bug.lose_health()
        if bug.get_health() <= 0:
            dead_bugs.append(bug)
    for bug in dead_bugs:
        enemies.remove(bug)

    for dude in allies:
        attack = pygame.Rect.collidelist(dude.get_hit_box(), target) > -1
        screen.blit(dude.animate(attack), (dude.get_x_pos(), dude.get_y_pos()))
        if attack:
            screen.blit(dude.get_attack(), (dude.x_gas, dude.y_gas))
        # else:
            # pygame.draw.rect(screen, (0, 255, 0), dude.hit_box)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                shop.pause(screen).run(screen)
            elif event.key == pygame.K_q:
                place_x, place_y = pygame.mouse.get_pos()
                allies.append(units.joe(place_x - 25, place_y - 25))


    frame = frame + 1
    if frame >= 25:
        frame = 1
        sec = sec + 1
    pygame.time.Clock().tick(fps)

'''           
CODE STORAGE


    # Spawn enemies, move them through the level path, animate their motion
    if stage.spawn(sec, frame):
        enemies.append(units.ant(-50, 310))

    target = []
    for bug in enemies:
        section, x_pos, y_pos = stage.trail(bug.get_section(), bug.get_x_pos(), bug.get_y_pos(), 1)
        bug.update(section, x_pos, y_pos)
        pygame.draw.rect(screen, (255, 0, 0), bug.get_hit_box())
        screen.blit(bug.animate(frame), (bug.get_x_pos(), bug.get_y_pos()))
        if bug.get_section() == 'Complete':
            print("gone!")
        else:
            target.append(bug.get_hit_box())

    for dude in allies:
        attack = pygame.Rect.collidelist(dude.get_hit_box(), target) > -1
        screen.blit(dude.animate(attack), (dude.get_x_pos(), dude.get_y_pos()))
        if attack:
            screen.blit(dude.get_attack(), (dude.x_gas, dude.y_gas))
        else:
            pygame.draw.rect(screen, (0, 255, 0), dude.hit_box)

    dead_bugs = []
    for bug in enemies:
        for dude in allies:
            if pygame.Rect.colliderect(dude.get_hit_box(), bug.get_hit_box()):
                bug.lose_health()
            if bug.get_health() <= 0:
                dead_bugs.append(bug)

    for bug in dead_bugs:
        enemies.remove(bug)
'''
