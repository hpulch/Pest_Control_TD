import pygame


def Q(surf):
    key = pygame.font.Font('freesansbold.ttf', 60)
    font = pygame.font.Font('freesansbold.ttf', 12)
    blk = (0, 0, 0)

    # Q key
    q = key.render('Q', True, blk)
    rect = q.get_rect()
    rect.x = 50
    rect.y = 125

    # Q sprite
    image = pygame.image.load("joe_a.png")
    image_rect = image.get_rect()
    image_rect.x = 110
    image_rect.y = 125

    # Q Line 1
    desc1 = font.render("Joe the Exterminator", True, blk)
    desc1_rect = desc1.get_rect()
    desc1_rect.x = 170
    desc1_rect.y = 125

    # Q Line 2
    desc2 = font.render("", True, blk)
    desc2_rect = desc2.get_rect()
    desc2_rect.x = 170
    desc2_rect.y = 135

    # Q Line 3
    desc3 = font.render("D: 120 per second", True, blk)
    desc3_rect = desc3.get_rect()
    desc3_rect.x = 170
    desc3_rect.y = 145

    # Q Line 4
    desc4 = font.render("R: 50x50 area", True, blk)
    desc4_rect = desc4.get_rect()
    desc4_rect.x = 170
    desc4_rect.y = 155

    # Q Line 5
    desc5 = font.render("S: continuous", True, blk)
    desc5_rect = desc5.get_rect()
    desc5_rect.x = 170
    desc5_rect.y = 165

    surf.blit(q, rect)
    surf.blit(image, image_rect)
    surf.blit(desc1, desc1_rect)
    surf.blit(desc2, desc2_rect)
    surf.blit(desc3, desc3_rect)
    surf.blit(desc4, desc4_rect)
    surf.blit(desc5, desc5_rect)


def W(surf):
    key = pygame.font.Font('freesansbold.ttf', 60)
    font = pygame.font.Font('freesansbold.ttf', 12)
    blk = (0, 0, 0)

    # W key
    w = key.render('W', True, blk)
    rect = w.get_rect()
    rect.x = 50
    rect.y = 200

    # W sprite
    image = pygame.image.load("joe_a.png")
    image_rect = image.get_rect()
    image_rect.x = 110
    image_rect.y = 200

    # W Line 1
    desc1 = font.render("Joe the Exterminator", True, blk)
    desc1_rect = desc1.get_rect()
    desc1_rect.x = 170
    desc1_rect.y = 200

    # W Line 2
    desc2 = font.render("", True, blk)
    desc2_rect = desc2.get_rect()
    desc2_rect.x = 170
    desc2_rect.y = 210

    # W Line 3
    desc3 = font.render("D: 120 per second", True, blk)
    desc3_rect = desc3.get_rect()
    desc3_rect.x = 170
    desc3_rect.y = 220

    # W Line 4
    desc4 = font.render("R: 50x50 area", True, blk)
    desc4_rect = desc4.get_rect()
    desc4_rect.x = 170
    desc4_rect.y = 230

    # W Line 5
    desc5 = font.render("S: continuous", True, blk)
    desc5_rect = desc5.get_rect()
    desc5_rect.x = 170
    desc5_rect.y = 240

    # display W
    surf.blit(w, rect)
    surf.blit(image, image_rect)
    surf.blit(desc1, desc1_rect)
    surf.blit(desc2, desc2_rect)
    surf.blit(desc3, desc3_rect)
    surf.blit(desc4, desc4_rect)
    surf.blit(desc5, desc5_rect)

    """


    #
    r = key.render('R', True, blk)
    r_rect = w.get_rect()
    r_rect.x = 50
    r_rect.y = 350
    #
    #surf.blit(e, e_rect)
    #surf.blit(pygame.image.load('joe_a.png'), (110, 275))

    #
    #surf.blit(r, r_rect)
    #surf.blit(pygame.image.load('joe_a.png'), (110, 350))
    """


def E(surf):
    key = pygame.font.Font('freesansbold.ttf', 60)
    font = pygame.font.Font('freesansbold.ttf', 12)
    blk = (0, 0, 0)

    # E key
    e = key.render('E', True, blk)
    rect = e.get_rect()
    rect.x = 50
    rect.y = 275

    # W sprite
    image = pygame.image.load("joe_a.png")
    image_rect = image.get_rect()
    image_rect.x = 110
    image_rect.y = 275

    # W Line 1
    desc1 = font.render("Joe the Exterminator", True, blk)
    desc1_rect = desc1.get_rect()
    desc1_rect.x = 170
    desc1_rect.y = 275

    # W Line 2
    desc2 = font.render("", True, blk)
    desc2_rect = desc2.get_rect()
    desc2_rect.x = 170
    desc2_rect.y = 285

    # W Line 3
    desc3 = font.render("D: 120 per second", True, blk)
    desc3_rect = desc3.get_rect()
    desc3_rect.x = 170
    desc3_rect.y = 295

    # W Line 4
    desc4 = font.render("R: 50x50 area", True, blk)
    desc4_rect = desc4.get_rect()
    desc4_rect.x = 170
    desc4_rect.y = 305

    # W Line 5
    desc5 = font.render("S: continuous", True, blk)
    desc5_rect = desc5.get_rect()
    desc5_rect.x = 170
    desc5_rect.y = 315

    # display E
    surf.blit(e, rect)
    surf.blit(image, image_rect)
    surf.blit(desc1, desc1_rect)
    surf.blit(desc2, desc2_rect)
    surf.blit(desc3, desc3_rect)
    surf.blit(desc4, desc4_rect)
    surf.blit(desc5, desc5_rect)


def R(surf):
    key = pygame.font.Font('freesansbold.ttf', 60)
    font = pygame.font.Font('freesansbold.ttf', 12)
    blk = (0, 0, 0)

    # R key
    r = key.render('R', True, blk)
    rect = r.get_rect()
    rect.x = 50
    rect.y = 350

    # R sprite
    image = pygame.image.load("joe_a.png")
    image_rect = image.get_rect()
    image_rect.x = 110
    image_rect.y = 350

    # W Line 1
    desc1 = font.render("Joe the Exterminator", True, blk)
    desc1_rect = desc1.get_rect()
    desc1_rect.x = 170
    desc1_rect.y = 350

    # W Line 2
    desc2 = font.render("", True, blk)
    desc2_rect = desc2.get_rect()
    desc2_rect.x = 170
    desc2_rect.y = 360

    # W Line 3
    desc3 = font.render("D: 120 per second", True, blk)
    desc3_rect = desc3.get_rect()
    desc3_rect.x = 170
    desc3_rect.y = 370

    # W Line 4
    desc4 = font.render("R: 50x50 area", True, blk)
    desc4_rect = desc4.get_rect()
    desc4_rect.x = 170
    desc4_rect.y = 380

    # W Line 5
    desc5 = font.render("S: continuous", True, blk)
    desc5_rect = desc5.get_rect()
    desc5_rect.x = 170
    desc5_rect.y = 390

    # display R
    surf.blit(r, rect)
    surf.blit(image, image_rect)
    surf.blit(desc1, desc1_rect)
    surf.blit(desc2, desc2_rect)
    surf.blit(desc3, desc3_rect)
    surf.blit(desc4, desc4_rect)
    surf.blit(desc5, desc5_rect)


def Ant(surf):
    key = pygame.font.Font('freesansbold.ttf', 60)
    font = pygame.font.Font('freesansbold.ttf', 12)
    blk = (0, 0, 0)

    # Ant level
    ant = key.render('L1', True, blk)
    rect = ant.get_rect()
    rect.x = 450
    rect.y = 125

    # Ant sprite
    image = pygame.image.load("ant_0.png")
    image_rect = image.get_rect()
    image_rect.x = 510
    image_rect.y = 125

    # Q Line 1
    desc1 = font.render("Marching Ants", True, blk)
    desc1_rect = desc1.get_rect()
    desc1_rect.x = 570
    desc1_rect.y = 125

    # Q Line 2
    desc2 = font.render("", True, blk)
    desc2_rect = desc2.get_rect()
    desc2_rect.x = 570
    desc2_rect.y = 135

    # Q Line 3
    desc3 = font.render("H: 1000 hit-points", True, blk)
    desc3_rect = desc3.get_rect()
    desc3_rect.x = 570
    desc3_rect.y = 145

    # Q Line 4
    desc4 = font.render("R: 24 frames per second", True, blk)
    desc4_rect = desc4.get_rect()
    desc4_rect.x = 570
    desc4_rect.y = 155

    # Q Line 5
    desc5 = font.render("S: Basic unit", True, blk)
    desc5_rect = desc5.get_rect()
    desc5_rect.x = 570
    desc5_rect.y = 165

    surf.blit(ant, rect)
    surf.blit(image, image_rect)
    surf.blit(desc1, desc1_rect)
    surf.blit(desc2, desc2_rect)
    surf.blit(desc3, desc3_rect)
    surf.blit(desc4, desc4_rect)
    surf.blit(desc5, desc5_rect)


def Fly(surf):
    key = pygame.font.Font('freesansbold.ttf', 60)
    font = pygame.font.Font('freesansbold.ttf', 12)
    blk = (0, 0, 0)

    # Fly level
    fly = key.render('L2', True, blk)
    rect = fly.get_rect()
    rect.x = 450
    rect.y = 200

    # fly sprite
    image = pygame.image.load("fly_0.png")
    image_rect = image.get_rect()
    image_rect.x = 510
    image_rect.y = 200

    # Q Line 1
    desc1 = font.render("Marching Ants", True, blk)
    desc1_rect = desc1.get_rect()
    desc1_rect.x = 570
    desc1_rect.y = 200

    # Q Line 2
    desc2 = font.render("", True, blk)
    desc2_rect = desc2.get_rect()
    desc2_rect.x = 570
    desc2_rect.y = 210

    # Q Line 3
    desc3 = font.render("H: 1000 hit-points", True, blk)
    desc3_rect = desc3.get_rect()
    desc3_rect.x = 570
    desc3_rect.y = 220

    # Q Line 4
    desc4 = font.render("R: 24 frames per second", True, blk)
    desc4_rect = desc4.get_rect()
    desc4_rect.x = 570
    desc4_rect.y = 230

    # Q Line 5
    desc5 = font.render("S: Basic unit", True, blk)
    desc5_rect = desc5.get_rect()
    desc5_rect.x = 570
    desc5_rect.y = 240

    surf.blit(fly, rect)
    surf.blit(image, image_rect)
    surf.blit(desc1, desc1_rect)
    surf.blit(desc2, desc2_rect)
    surf.blit(desc3, desc3_rect)
    surf.blit(desc4, desc4_rect)
    surf.blit(desc5, desc5_rect)


def pause(surf):
    # Paused
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('PAUSED', True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (100, 50)

    # left box
    display_left_rect = pygame.Rect(25, 100, 350, 515)
    display_left_surf = pygame.Surface((350, 515))
    display_left_surf.set_alpha(175)
    display_left_surf.fill((255, 255, 255))

    # right box
    display_right_rect = pygame.Rect(425, 100, 350, 515)
    display_right_surf = pygame.Surface((350, 515))
    display_right_surf.set_alpha(175)
    display_right_surf.fill((255, 255, 255))

    # return
    surf.blit(text, text_rect)
    surf.blit(display_left_surf, display_left_rect)
    surf.blit(display_right_surf, display_right_rect)


def loop(surf):
    fade = pygame.image.load('pause.png')
    pos = 0, 0

    surf.blit(fade, pos)
    pause(surf)
    Q(surf)
    W(surf)
    E(surf)
    R(surf)
    Ant(surf)
    Fly(surf)

    paused = True
    while paused:
        pygame.display.flip()
        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    paused = False



