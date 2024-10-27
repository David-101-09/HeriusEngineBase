import pygame
import json

class SceneEditor:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Scene Editor")
        self.elements = []  # Armazena elementos da cena (posições e sprites)
        self.selected_sprite = None  # Sprite selecionado para posicionar

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and self.selected_sprite:
                    # Adiciona o elemento à cena com a posição do mouse
                    x, y = pygame.mouse.get_pos()
                    self.elements.append({
                        "type": "sprite",
                        "x": x,
                        "y": y,
                        "sprite": self.selected_sprite
                    })
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.save_scene("level1.scene")  # Salva o arquivo .scene

            self.screen.fill((200, 200, 200))
            # Desenha os elementos da cena
            for element in self.elements:
                if element["type"] == "sprite":
                    sprite = pygame.image.load(element["sprite"])
                    self.screen.blit(sprite, (element["x"], element["y"]))

            pygame.display.flip()
        
        pygame.quit()

    def save_scene(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.elements, f, indent=4)
        print(f"Scene saved as {filename}")

if __name__ == "__main__":
    editor = SceneEditor()
    editor.selected_sprite = "path/to/sprite.png"  # Caminho para o sprite escolhido
    editor.run()