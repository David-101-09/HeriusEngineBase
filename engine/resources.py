import pygame
import os

class Resources:
    def __init__(self, base_path):
        self.base_path = base_path
        self.images = {}
        self.sounds = {}

    def load_image(self, name):
        if name not in self.images:
            path = os.path.join(self.base_path, 'images', name)
            self.images[name] = pygame.image.load(path)
        return self.images[name]

    def load_sound(self, name):
        if name not in self.sounds:
            path = os.path.join(self.base_path, 'sounds', name)
            self.sounds[name] = pygame.mixer.Sound(path)
        return self.sounds[name]