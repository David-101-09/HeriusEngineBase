# core.py
import pygame
import sys
from engine.scene_manager import SceneManager, Scene
from engine.entity import Entity

class GameEngine:
    def __init__(self, width, height, title="HIGE"):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True
        self.scene_manager = None

    def set_scene_manager(self, scene_manager):
        self.scene_manager = scene_manager

    def run(self, fps=60):
        while self.running:
            dt = self.clock.tick(fps) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.scene_manager:
                        next_scene = "Cena 2" if self.scene_manager.current_scene.name == "Cena 1" else "Cena 1"
                        self.scene_manager.set_scene(next_scene)

            if self.scene_manager:
                self.scene_manager.update(dt)
                self.scene_manager.draw(self.screen)

            pygame.display.flip()

        pygame.quit()
        sys.exit()

# Inicialização da engine e cenas
engine = GameEngine(800, 600, "Game Engine with Physics and Scene Transitions")
scene_manager = SceneManager()

# Cena de teste com uma entidade dinâmica e uma plataforma fixa
scene1 = Scene("Cena 1")
dynamic_entity = Entity(100, 100, 50, 50, color=(255, 0, 0), is_dynamic=True)
platform = Entity(100, 400, 200, 20, color=(0, 255, 0), is_dynamic=False)

scene1.add_entity(dynamic_entity)
scene1.add_entity(platform)
scene_manager.add_scene(scene1)
scene_manager.set_scene("Cena 1")

# Configura o scene manager na engine e inicia o loop principal
engine.set_scene_manager(scene_manager)
engine.run()
