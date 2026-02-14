from .board import Board
from .rules import Rules
from .ai import RandomAI
from typing import Optional

class GameManager:
    def __init__(self, size):
        self.size = size
        self.board = Board(size)
        self.rules = Rules(size)
        self.ai = RandomAI()
        self.current_player: str = "X"
        self.human_symbol: Optional[str] = None
        self.ai_symbol: Optional[str] = None
        self.game_over: bool = False

    def start_game(self, human_symbol: str):
        self.board.reset()
        self.human_symbol = human_symbol
        self.ai_symbol = "O" if human_symbol == "X" else "X"
        self.current_player = "X"
        self.game_over = False
        self.move_count = 0

    def make_move(self, row: int = None, col: int = None):
        if self.game_over:
            return

        if self.current_player == self.human_symbol:
            if row is not None and col is not None:
                success = self.board.place_symbol(row, col, self.human_symbol)
                if not success:
                    raise ValueError("Case déjà occupée")
        else:
            r, c = self.ai.choose_move(self.board)
            self.board.place_symbol(r, c, self.ai_symbol)

        self.move_count += 1
        
        # Vérifier victoire
        if self.move_count >= (self.rules.win_length * 2 - 1):
            if self.rules.check_winner(self.board, self.current_player):
                self.game_over = True
                return f"{self.current_player} a gagné !"


        # Vérifier égalité
        if self.move_count == self.size * self.size:
            self.game_over = True
            return "Égalité !"

        # Changer de joueur
        self.current_player = self.ai_symbol if self.current_player == self.human_symbol else self.human_symbol
        return None
