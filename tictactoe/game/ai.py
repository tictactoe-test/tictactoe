import random
from typing import Tuple
from .board import Board

class RandomAI:
    def choose_move(self, board: Board) -> Tuple[int, int]:
        empty_cells = board.get_empty_cells()
        if not empty_cells:
            raise ValueError("No empty cells left")
        return random.choice(empty_cells)
