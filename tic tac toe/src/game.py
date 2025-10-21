import pygame
import sys
from .state_manager import StateManager
from .states.menu_buttons import ButtonMenuState

class TicTacToeGame:
    def __init__(self):
        pygame.init()
        
        self.screen =  pygame.display.set_mode((300, 300)) 
        pygame.display.set_caption('Tic Tac Toe')
        self.clock = pygame.time.Clock()
        
        # Inicializar gerenciador de estados
        self.state_manager = StateManager()
        
        #game_state = GameState(self.state_manager)
        menu_state = ButtonMenuState(self.state_manager) 
        self.state_manager.change_state(menu_state)
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.state_manager.handle_event(event)
            
            self.state_manager.update()
            self.state_manager.render(self.screen)
            
            pygame.display.update()
        
        pygame.quit()
        sys.exit()
