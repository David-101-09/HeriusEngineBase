# tests/test_prototype.py
import sys
import os

# Adiciona o diretório principal da engine ao path para importar módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from engine.core import GameEngine
from engine.scene_manager import SceneManager, Scene
from engine.entity import Entity

def main():
    # Inicializa o GameEngine com largura e altura da janela
    engine = GameEngine(800, 600, title="Teste da Engine com Física e Colisão")
    scene_manager = SceneManager()

    # Cena 1 - Inclui um jogador controlável e duas plataformas
    scene1 = Scene("Cena 1")
    player = Entity(100, 100, 50, 50, color=(0, 0, 255), is_dynamic=True)
    platform1 = Entity(50, 300, 300, 20, color=(0, 255, 0), is_dynamic=False)
    platform2 = Entity(400, 450, 300, 20, color=(0, 255, 0), is_dynamic=False)

    scene1.add_entity(player)
    scene1.add_entity(platform1)
    scene1.add_entity(platform2)

    # Cena 2 - Apenas um objeto estático para simular uma segunda cena
    scene2 = Scene("Cena 2")
    static_entity = Entity(300, 200, 200, 100, color=(255, 0, 0), is_dynamic=False)
    scene2.add_entity(static_entity)

    # Adiciona as cenas ao gerenciador de cenas e define a cena inicial
    scene_manager.add_scene(scene1)
    scene_manager.add_scene(scene2)
    scene_manager.set_scene("Cena 1")

    # Define o gerenciador de cenas e inicia o loop principal
    engine.set_scene_manager(scene_manager)

    # Função principal de execução
    while engine.running:
        # Processa eventos
        keys = pygame.key.get_pressed()  # Captura teclas pressionadas
        player.handle_input(keys)  # Processa entrada do jogador

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                engine.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Alterna entre Cena 1 e Cena 2
                    next_scene = "Cena 2" if scene_manager.current_scene.name == "Cena 1" else "Cena 1"
                    scene_manager.set_scene(next_scene)

        # Executa o loop principal da engine com as atualizações e renderizações
        engine.run()

if __name__ == "__main__":
    main()
