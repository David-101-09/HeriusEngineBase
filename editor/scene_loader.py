import pygame
import json

class SceneLoader:
    def __init__(self, scene_file):
        self.elements = self.load_scene(scene_file)

    def load_scene(self, scene_file):
        with open(scene_file, 'r') as f:
            return json.load(f)

    def draw(self, screen):
        for element in self.elements:
            if element["type"] == "sprite":
                sprite = pygame.image.load(element["sprite"])
                screen.blit(sprite, (element["x"], element["y"]))
