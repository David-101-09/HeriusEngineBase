# engine/entity.py
import pygame
from .physics import apply_gravity, check_collision

class Entity:
    def __init__(self, x, y, width, height, color=(255, 0, 0), is_dynamic=True):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.is_dynamic = is_dynamic
        self.velocity_y = 0  # Velocidade inicial no eixo Y
        self.velocity_x = 0  # Velocidade inicial no eixo X
        self.speed = 200     # Velocidade de movimento

    def update(self, dt, entities=[]):
        """Atualiza a posição do objeto e verifica colisões."""
        # Aplica gravidade se for dinâmico
        if self.is_dynamic:
            apply_gravity(self, dt)

        # Movimento horizontal e colisões
        self.rect.x += int(self.velocity_x * dt)
        for other in entities:
            if other is not self:
                check_collision(self, other)

        # Movimento vertical e colisões
        self.rect.y += int(self.velocity_y * dt)
        for other in entities:
            if other is not self:
                check_collision(self, other)

    def draw(self, surface):
        """Desenha o objeto na superfície dada."""
        pygame.draw.rect(surface, self.color, self.rect)

    def handle_input(self, keys):
        """Lida com a entrada do jogador."""
        self.velocity_x = 0  # Redefine a velocidade horizontal para evitar movimento contínuo

        if keys[pygame.K_LEFT]:
            self.velocity_x = -self.speed
        if keys[pygame.K_RIGHT]:
            self.velocity_x = self.speed
