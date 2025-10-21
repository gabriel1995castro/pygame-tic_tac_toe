class GameRules:
    @staticmethod
    def check_winner(board):
        
        grid = board.grid
        
        # Verificar linhas
        for line in grid:
            if line[0] is not None and line[0] == line[1] == line[2]:
                return line[0]
        
        # Verificar colunas
        for column in range(3):
            if grid[0][column] is not None and grid[0][column] == grid[1][column] == grid[2][column]:
                return grid[0][column]
        
        # Diagonal principal
        if grid[0][0] is not None and grid[0][0] == grid[1][1] == grid[2][2]:
            return grid[0][0]
        
        # Diagonal secundária
        if grid[0][2] is not None and grid[0][2] == grid[1][1] == grid[2][0]:
            return grid[0][2]
        
        return None
    
    @staticmethod
    def is_draw(board):
        """Verifica se o jogo terminou em empate"""
        return board.is_full() and GameRules.check_winner(board) is None
