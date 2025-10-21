import pygame
import math  
from .base_state import BaseState

class GameOverState(BaseState):
    def __init__(self, state_manager, winner=None, game_mode="pvp", difficulty="hard"):
        super().__init__(state_manager)
        self.winner = winner
        self.game_mode = game_mode
        self.difficulty = difficulty
        
        # Cores
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 150, 0)
        self.RED = (150, 0, 0)
        self.BLUE = (0, 100, 200)
        self.GRAY = (100, 100, 100)
        self.LIGHT_GRAY = (200, 200, 200)
        
        # Fontes
        self.title_font = pygame.font.Font(None, 48)
        self.button_font = pygame.font.Font(None, 32)
        self.subtitle_font = pygame.font.Font(None, 24)
        
        # Botões
        self.play_again_button = pygame.Rect(50, 180, 200, 50)
        self.menu_button = pygame.Rect(50, 240, 200, 50)
        
        # Animação
        self.animation_timer = 0
        self.bounce_offset = 0
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            
            if self.play_again_button.collidepoint(mouse_pos):
                # Importação local para evitar circular import
                try:
                    from .game_state import GameState
                    new_game = GameState(self.state_manager, self.game_mode, self.difficulty)
                    self.state_manager.change_state(new_game)
                except ImportError as e:
                    print(f"Erro ao importar GameState: {e}")
                    # Fallback: volta ao menu
                    self._go_to_menu()
            
            elif self.menu_button.collidepoint(mouse_pos):
                self._go_to_menu()
    
    def _go_to_menu(self):
        """Volta ao menu principal"""
        try:
            from .menu_buttons import ButtonMenuState
            menu = ButtonMenuState(self.state_manager)
            self.state_manager.change_state(menu)
        except ImportError:
            print("Erro: Não foi possível voltar ao menu")
    
    def update(self):

        pass
       
    
    def render(self, screen):
        # Fundo gradient
        self._draw_gradient_background(screen)
        
        # Título principal com animação
        self._draw_title(screen)
        
        # Subtítulo
        self._draw_subtitle(screen)
        
        # Botões
        self._draw_buttons(screen)
        
    
    def _draw_gradient_background(self, screen):
        """Desenha um fundo com gradient"""
        
        screen.fill(self.BLACK)
  
    
    def _draw_title(self, screen):
        """Desenha o título principal"""
        if self.winner:
            if self.winner == 'X':
                title_text = "YOU WIN!"
                title_color = self.GREEN
            else:
                if self.game_mode in ["pvc", "pc_game", "pvcomputer", "computer"]:
                    title_text = "AI WINS!"
                else:
                    title_text = f"PLAYER {self.winner} WINS! "
                title_color = self.RED
        else:
            title_text = "DRAW!"
            title_color = self.WHITE
        
        # Renderiza com bounce
        title_surface = self.title_font.render(title_text, True, title_color)
        title_rect = title_surface.get_rect(center=(150, 60))        
        # Sombra
        shadow_surface = self.title_font.render(title_text, True, self.BLACK)
        shadow_rect = shadow_surface.get_rect(center=(152, 62 - self.bounce_offset))
        screen.blit(shadow_surface, shadow_rect)
        screen.blit(title_surface, title_rect)
    
    def _draw_subtitle(self, screen):
        pass
    
    def _draw_buttons(self, screen):
        """Desenha os botões interativos"""
        mouse_pos = pygame.mouse.get_pos()
        
        # Botão Jogar Novamente
        play_hover = self.play_again_button.collidepoint(mouse_pos)
        play_color = self.GREEN if play_hover else self.LIGHT_GRAY
        play_text_color = self.WHITE if play_hover else self.BLACK
        
        pygame.draw.rect(screen, play_color, self.play_again_button, border_radius=10)
        pygame.draw.rect(screen, self.BLACK, self.play_again_button, 3, border_radius=10)
        
        play_text = self.button_font.render("Play Again", True, play_text_color)
        play_text_rect = play_text.get_rect(center=self.play_again_button.center)
        screen.blit(play_text, play_text_rect)
        
        # Botão Menu
        menu_hover = self.menu_button.collidepoint(mouse_pos)
        menu_color = self.BLUE if menu_hover else self.LIGHT_GRAY
        menu_text_color = self.WHITE if menu_hover else self.BLACK
        
        pygame.draw.rect(screen, menu_color, self.menu_button, border_radius=10)
        pygame.draw.rect(screen, self.BLACK, self.menu_button, 3, border_radius=10)
        
        menu_text = self.button_font.render("Main Menu", True, menu_text_color)
        menu_text_rect = menu_text.get_rect(center=self.menu_button.center)
        screen.blit(menu_text, menu_text_rect)
    
    

           