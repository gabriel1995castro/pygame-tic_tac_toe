from ..game_logic.game_rules import GameRules
import random

class Minimax_fuction:
    def __init__(self, ai_symbol='O', human_symbol='X'):
        self.computer_symb = ai_symbol
        self.playe_symbol = human_symbol
        self.ai_symbol = ai_symbol
        self.human_symbol = human_symbol
    
    def random_move(self, board):
        empty_positions = []
        for row in range(3):
            for col in range(3):
                if board.grid[row][col] is None:
                    empty_positions.append((row, col))
        return random.choice(empty_positions) if empty_positions else None
    
    def find_best_move(self, board):
        best_score = float('-inf')
        best_move = None
        
        for row in range(3):
            for column in range(3):
                if board.grid[row][column] is None:
                    board.grid[row][column] = self.ai_symbol
                    score = self.minimax(board, 0, False)
                    board.grid[row][column] = None
                    
                    if score > best_score:
                        best_score = score
                        best_move = (row, column)
        
        return best_move
    
    def minimax(self, board, depth, maximizing):
        winner = GameRules.check_winner(board)
        
        if winner == self.ai_symbol:
            return 1
        elif winner == self.human_symbol:
            return -1
        elif GameRules.is_draw(board):
            return 0
        
        if maximizing:
            max_score = float('-inf')
            for row in range(3):
                for col in range(3):
                    if board.grid[row][col] is None:
                        board.grid[row][col] = self.ai_symbol
                        score = self.minimax(board, depth + 1, False)
                        board.grid[row][col] = None
                        max_score = max(score, max_score)
            return max_score
        else:
            min_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if board.grid[row][col] is None:
                        board.grid[row][col] = self.human_symbol
                        score = self.minimax(board, depth + 1, True)
                        board.grid[row][col] = None
                        min_score = min(score, min_score)
            return min_score
    
    def get_difficulty_move(self, board, difficulty='hard'):
        if difficulty == 'easy':
            return self.random_move(board)
        elif difficulty == 'medium':
            if random.random() < 0.7:
                return self.find_best_move(board)
            else:
                return self.random_move(board)
        else: 
            return self.find_best_move(board)