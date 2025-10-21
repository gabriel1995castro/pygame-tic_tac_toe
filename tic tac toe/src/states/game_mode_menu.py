import pygame
from .base_state import BaseState
from .game_state import GameState
from ..ui.button import Button

class GameModeMenuState(BaseState):
    def __init__(self, state_manager):
        super().__init__(state_manager)
        self.font = pygame.font.Font(None, 28)
        self.title_font = pygame.font.Font(None, 40)
        
        self.multiplayer_button = Button(50, 100, 200, 40, "Player X Player", self.font, (50, 100, 150))
        self.computer_button = Button(50, 150, 200, 40, "Vs Computer", self.font, (100, 150, 50))
        self.back_button = Button(50, 200, 200, 40, "Voltar", self.font, (100, 100, 100))
    
    def handle_event(self, event):
        if self.multiplayer_button.handle_event(event):
            game_state = GameState(self.state_manager, mode="PVP")
            self.state_manager.change_state(game_state)
        
        elif self.computer_button.handle_event(event):
            game_state = GameState(self.state_manager, mode="PC_game")
            self.state_manager.change_state(game_state)
        
        elif self.back_button.handle_event(event):
            from .menu_buttons import ButtonMenuState
            main_menu = ButtonMenuState(self.state_manager)
            self.state_manager.change_state(main_menu)
    
    def update(self):
        pass
    
    def render(self, screen):
        screen.fill((60, 40, 80))
        
     
        title = self.title_font.render("ESCOLHA O MODO", True, (255, 255, 255))
        title_rect = title.get_rect(center=(150, 50))
        screen.blit(title, title_rect)
        
        self.multiplayer_button.draw(screen)
        self.computer_button.draw(screen)
        self.back_button.draw(screen)
        
       
        instruction_font = pygame.font.Font(None, 20)
        instruction = instruction_font.render("Clique para selecionar", True, (200, 200, 200))
        screen.blit(instruction, (70, 260))