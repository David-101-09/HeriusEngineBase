import sys
import json
import pygame
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFileDialog, QSpinBox, QSlider, QColorDialog, QCheckBox
)
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtCore import Qt

# Configuração de Pygame
pygame.init()
pygame.display.set_caption("Pré-visualização")

class SceneEditorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scene Editor with PyQt5 UI")
        self.setGeometry(100, 100, 1200, 700)

        # Variáveis principais
        self.elements = []  # Elementos da cena
        self.selected_element = None

        # Interface principal
        self.init_ui()

    def init_ui(self):
        # Widget central e layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        main_layout = QHBoxLayout(self.central_widget)

        # Layout de pré-visualização
        self.canvas_widget = QLabel("Pré-visualização")
        self.canvas_widget.setFixedSize(800, 600)
        main_layout.addWidget(self.canvas_widget)

        # Layout lateral de propriedades
        self.property_panel = QVBoxLayout()
        main_layout.addLayout(self.property_panel)

        # Botões para carregar e salvar cena
        load_button = QPushButton("Carregar Cena")
        load_button.clicked.connect(self.load_scene)
        self.property_panel.addWidget(load_button)

        save_button = QPushButton("Salvar Cena")
        save_button.clicked.connect(self.save_scene)
        self.property_panel.addWidget(save_button)

        # Controles de posição, rotação e escala
        self.add_property_controls()

    def add_property_controls(self):
        # Controle de posição X e Y
        self.x_spin = QSpinBox()
        self.x_spin.setRange(-1000, 1000)
        self.x_spin.setPrefix("X: ")
        self.property_panel.addWidget(self.x_spin)

        self.y_spin = QSpinBox()
        self.y_spin.setRange(-1000, 1000)
        self.y_spin.setPrefix("Y: ")
        self.property_panel.addWidget(self.y_spin)

        # Controle de rotação
        self.rotation_slider = QSlider(Qt.Horizontal)
        self.rotation_slider.setRange(0, 360)
        self.rotation_slider.setValue(0)
        self.rotation_slider.setTickInterval(15)
        self.rotation_slider.setTickPosition(QSlider.TicksBelow)
        self.property_panel.addWidget(QLabel("Rotação:"))
        self.property_panel.addWidget(self.rotation_slider)

        # Controle de escala
        self.scale_slider = QSlider(Qt.Horizontal)
        self.scale_slider.setRange(1, 200)
        self.scale_slider.setValue(100)
        self.property_panel.addWidget(QLabel("Escala (%):"))
        self.property_panel.addWidget(self.scale_slider)

        # Checkbox para colisão
        self.collision_checkbox = QCheckBox("Habilitar Colisão")
        self.property_panel.addWidget(self.collision_checkbox)

    def add_element(self, x, y, sprite_path):
        """Adiciona um novo elemento à cena."""
        element = {
            "type": "sprite",
            "x": x,
            "y": y,
            "sprite": sprite_path,
            "rotation": 0,
            "scale": 1.0,
            "collision": False
        }
        self.elements.append(element)

    def save_scene(self):
        """Salva a cena atual em um arquivo JSON."""
        options = QFileDialog.Options()
        file, _ = QFileDialog.getSaveFileName(
            self, "Salvar Cena", "", "Arquivo de Cena (*.scene);;Todos os Arquivos (*)", options=options
        )
        if file:
            with open(file, 'w') as f:
                json.dump(self.elements, f, indent=4)
            print(f"Cena salva como: {file}")

    def load_scene(self):
        """Carrega uma cena de um arquivo JSON."""
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(
            self, "Carregar Cena", "", "Arquivo de Cena (*.scene);;Todos os Arquivos (*)", options=options
        )
        if file:
            with open(file, 'r') as f:
                self.elements = json.load(f)
            print(f"Cena carregada de: {file}")

    def update_preview(self):
        """Renderiza a pré-visualização da cena."""
        screen = pygame.display.set_mode((800, 600))
        screen.fill((200, 200, 200))

        for element in self.elements:
            sprite = pygame.image.load(element["sprite"])
            sprite = pygame.transform.scale(sprite, (int(100 * element["scale"]), int(100 * element["scale"])))
            screen.blit(sprite, (element["x"], element["y"]))
        
        pygame.display.flip()

# Executa a aplicação
app = QApplication(sys.argv)
window = SceneEditorUI()
window.show()
sys.exit(app.exec_())
