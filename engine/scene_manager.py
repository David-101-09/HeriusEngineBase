# engine/scene_manager.py
import pygame

class Scene:
    def __init__(self, name):
        self.name = name
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def update(self, dt):
        """Atualiza todos os elementos da cena e verifica colisões."""
        for entity in self.entities:
            entity.update(dt, self.entities)

    def draw(self, surface):
        """Renderiza todos os elementos na superfície dada."""
        surface.fill((0, 0, 0))  # Limpa a tela
        for entity in self.entities:
            entity.draw(surface)

class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current_scene = None
        self.transition_alpha = 0
        self.is_transitioning = False

    def add_scene(self, scene):
        """Adiciona uma nova cena ao gerenciador."""
        self.scenes[scene.name] = scene

    def set_scene(self, scene_name):
        """Inicia a transição para uma nova cena."""
        if scene_name in self.scenes:
            self.is_transitioning = True
            self.next_scene = self.scenes[scene_name]

    def update(self, dt):
        """Atualiza a cena atual e gerencia transições."""
        if self.is_transitioning:
            self.transition_alpha += 255 * dt
            if self.transition_alpha >= 255:
                self.current_scene = self.next_scene
                self.transition_alpha = 0
                self.is_transitioning = False
        elif self.current_scene:
            self.current_scene.update(dt)

    def draw(self, surface):
        """Renderiza a cena e aplica efeito de transição."""
        if self.current_scene:
            self.current_scene.draw(surface)
        
        if self.is_transitioning:
            fade_surface = pygame.Surface(surface.get_size())
            fade_surface.set_alpha(int(self.transition_alpha))
            fade_surface.fill((0, 0, 0))
            surface.blit(fade_surface, (0, 0))