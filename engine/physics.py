# engine/physics.py
def apply_gravity(entity, dt, gravity=9.8):
    """Aplica gravidade ao objeto dinâmico."""
    entity.velocity_y += gravity * dt  # Aumenta a velocidade de queda
    entity.rect.y += int(entity.velocity_y)  # Move o objeto no eixo Y

def check_collision(entity, other):
    """Verifica colisão e resolve se detectada."""
    if entity.rect.colliderect(other.rect):
        # Resolve colisão ajustando a posição e velocidade
        if entity.rect.bottom > other.rect.top and entity.velocity_y > 0:
            entity.rect.bottom = other.rect.top
            entity.velocity_y = 0  # Para a velocidade ao colidir
        return True
    return False
