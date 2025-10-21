import pygame
from .base_state import BaseState
from ..game_logic.board import Board
from ..game_logic.game_rules import GameRules
from ..game_logic.minamax_ignite import Minimax_fuction
from ..ui.grid_ui import GridUI
from ..states.result_state import GameOverState

class GameState(BaseState):
    def __init__(self, state_manager, mode="PVP", difficulty='hard'):
        super().__init__(state_manager)
        self.game_mode = mode.lower()
        self.difficulty = difficulty.lower()
        self.board = Board()
        self.grid_ui = GridUI()
        self.game_over = False
        self.winner = None
        
        self.ai_modes = ["pvc", "pc_game", "pvcomputer", "computer"]
        if self.game_mode in self.ai_modes:
            self.ai = Minimax_fuction(ai_symbol='O', human_symbol='X')
            self.ai_thinking = False
            self.ai_think_timer = 0
            self.AI_THINK_TIME = 500
            self.game_over_timer = 0
            self.GAME_OVER_DELAY = 1500
        else:
            self.ai = None
            self.ai_thinking = False
            self.ai_think_timer = 0
            self.AI_THINK_TIME = 500

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
            
            can_play = self.game_mode == "pvp" or self._is_human_turn()
            ai_modes = ["pvc", "pc_game", "pvcomputer", "computer"]
            if can_play and not self.ai_thinking:
                x, y = pygame.mouse.get_pos()
                column = x // 100
                line = y // 100
                                
                if 0 <= line < 3 and 0 <= column < 3:
                    if self.board.make_move(line, column):
                        self._check_game_end()
                        
                        ai_modes = ["pvc", "pc_game", "pvcomputer", "computer"]
                       
                        if self.game_mode in ai_modes and not self.game_over:
                            self.ai_thinking = True
                            self.ai_think_timer = pygame.time.get_ticks()


    def _is_human_turn(self):
        is_human = self.board.current_player == 'X'
        return is_human

    def _computer_turn(self):
        
        if self.game_over:
            self.ai_thinking = False
            return
            
        if not self.ai:
            self.ai_thinking = False
            return
            
        try:
            move = self.ai.get_difficulty_move(self.board, self.difficulty)
            
            if move:
                row, col = move
                if self.board.grid[row][col] is None:
                    self.board.grid[row][col] = 'O'
                    self.board.switch_player()
                    self._check_game_end()
                else:
                    self._random_ai_move()
            
                
        except Exception as e:
            self._random_ai_move()
        self.ai_thinking = False

    def _random_ai_move(self):
        import random
        empty_positions = []
        for row in range(3):
            for col in range(3):
                if self.board.grid[row][col] is None:
                    empty_positions.append((row, col))
        
        if empty_positions:
            row, col = random.choice(empty_positions)
            self.board.grid[row][col] = 'O'
            self.board.switch_player()
            self._check_game_end()

    def _check_game_end(self):
        self.winner = GameRules.check_winner(self.board)
        if self.winner:
            self.game_over = True
        elif GameRules.is_draw(self.board):
            self.game_over = True

    def update(self):
        if self.game_over:
            current_time = pygame.time.get_ticks()
            if current_time - self.game_over_timer >= self.GAME_OVER_DELAY:
                game_over_state = GameOverState(self.state_manager, self.winner, self.game_mode, self.difficulty)
                self.state_manager.change_state(game_over_state)
            return
        if self.ai and self.ai_thinking:
            current_time = pygame.time.get_ticks()
            if current_time - self.ai_think_timer >= self.AI_THINK_TIME:
                self._computer_turn()

    def render(self, screen):
        screen.fill((255, 255, 255))  # WHITE
        self.grid_ui.draw_lines(screen)
        self.grid_ui.draw_symbols(screen, self.board)
    