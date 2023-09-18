import pygame


class pause:
    def __init__(self, screen):
        pygame.display.set_caption("Pest Control TD  --PAUSE--")
        self.map = pygame.image.load('pause.png')
        self.pos = 0, 0

    def run(self, screen):
        running = True
        screen.blit(self.map, self.pos)
        while running:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print("BATTLE!")
                        running = False
