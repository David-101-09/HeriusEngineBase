import pygame

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(self.camera.width / 2)
        y = -target.rect.centery + int(self.camera.height / 2)
        self.camera = pygame.Rect(x, y, self.camera.width, self.camera.height)