import pygame

class GridUI:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 100)
        self.line_width = 15
    
    def draw_lines(self, screen):

        black = (0, 0, 0)
        
        # Linhas verticais
        pygame.draw.line(screen, black, (100, 0), (100, 300), self.line_width)
        pygame.draw.line(screen, black, (200, 0), (200, 300), self.line_width)
        
        # Linhas horizontais
        pygame.draw.line(screen, black, (0, 100), (300, 100), self.line_width)
        pygame.draw.line(screen, black, (0, 200), (300, 200), self.line_width)
    
    def draw_symbols(self, screen, board):
        
        red = (255, 0, 0)
        
        for line in range(3):
            for column in range(3):
                cell_value = board.get_cell(line, column)
                if cell_value is not None:
                    text = self.font.render(cell_value, True, red)
                    screen.blit(text, (column * 100 + 25, line * 100 + 10))
