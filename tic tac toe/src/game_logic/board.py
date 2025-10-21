class Board:
    def __init__(self):
        self.grid = [[None] * 3 for _ in range(3)]
        self.current_player = "X"
    
    def make_move(self, row, col):
        """Faz uma jogada se a posição estiver vazia"""
        if self.grid[row][col] is None:
            self.grid[row][col] = self.current_player
            self.switch_player()
            return True
        return False
    
    def switch_player(self):
        """Alterna entre jogadores"""
        self.current_player = "O" if self.current_player == "X" else "X"
    
    def get_cell(self, row, col):
        """Retorna o valor de uma célula"""
        return self.grid[row][col]
    
    def is_full(self):
        """Verifica se o tabuleiro está cheio"""
        for row in self.grid:
            if None in row:
                return False
        return True
