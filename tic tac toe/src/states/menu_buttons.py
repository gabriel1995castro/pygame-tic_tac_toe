import pygame
from .base_state import BaseState
from .game_state import GameState
from .game_mode_menu import GameModeMenuState
from ..ui.button import Button

class ButtonMenuState (BaseState):
    
    def __init__(self, state_manager):

        super().__init__(state_manager)
        self.font =pygame.font.Font(None,28)
        self.title_font = pygame.font.Font(None,48)

        self.play_button = Button(75, 120, 150, 50, "JOGAR", self.font)
        self.about_button = Button(75, 180, 150, 50, "INSTRUÇÕES", self.font)
        self.quit_button = Button(75, 240, 150, 50, "SAIR", self.font)

    def handle_event(self, event):

        if self.play_button.handle_event(event):
            game_mode_menu = GameModeMenuState(self.state_manager)
            self.state_manager.change_state(game_mode_menu)
        
        elif self.about_button.handle_event(event):
            pass

        elif self.quit_button.handle_event(event):
            pygame.quit()
            exit()

    def render(self, screen):
        screen.fill((40, 40, 60))
        
        # Título
        title = self.title_font.render("JOGO DA VELHA", True, (255, 255, 255))
        title_rect = title.get_rect(center=(150, 60))
        screen.blit(title, title_rect)
        
        # Desenhar botões
        self.play_button.draw(screen)
        self.about_button.draw(screen)
        self.quit_button.draw(screen)

    