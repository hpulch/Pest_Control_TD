import pygame

import Units
import Levels
import Pause


def frames(f):
    f += 1
    if f >= 25:
        f = 1
    return f


pygame.init()
screen = pygame.display.set_mode((800, 640))
current_level = 1
level = [0, Levels.One(screen), Levels.Two(screen)]

enemies = pygame.sprite.Group()
allies = pygame.sprite.Group()
count = 0


frame = 1

running = True
while running:
    screen.fill((0, 128, 0))

    level[current_level].draw(screen)
    if level[current_level].update(frame):
        enemies.add(Units.Ant(level[current_level].get_waypoints()))

    enemies.update(frame)

    for ally in allies:
        if len(enemies) == 0:
            ally.reset()
        for bug in enemies:
            # For each ally compare it's hit_box to every bug and update its attack status
            ally.update(bug.hit_box)
            if ally.get_status():
                # If ally if attacking, stop checking bugs and do not update so he continues to attack first bug
                break

    for bug in enemies:
        for ally in allies:
            # For each bug compare it's hit_box to every ally and update its attack status
            if bug.update_hit(ally.hit_box, ally.damage) == -1:
                level[current_level].track_points(bug.dead_bug())
                break

    allies.draw(screen)

    # blit the transparent overlay first and then blit the sprite image overtop
    for bug in enemies:
        bug.overlay(screen)
    enemies.draw(screen)

    # blit the transparent overlay overtop allies
    for joe in allies:
        joe.overlay(screen)

    # update display surface to the screen
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Pause.loop(screen)
            elif event.key == pygame.K_q:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                on_path = level[current_level].path_mask.get_at((mouse_x, mouse_y + 20))
                if on_path:
                    print("Cannot place allies on path!")
                else:
                    allies.add(Units.Joe(mouse_x, mouse_y))

    current_level = level[current_level].next_level(screen)
    frame = frames(frame)
    pygame.time.Clock().tick(24)
    print(current_level)
    print(level[current_level])
pygame.quit()

# pygame.draw.lines(screen, "grey0", False, one.waypoints)
