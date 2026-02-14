from typing import List, Optional
from .board import Board

class Rules:
    def __init__(self, win_length: int):
        self.win_length = win_length

    def check_winner(self, board: Board, symbol: str) -> bool:
        size = board.size
        grid = board.grid

        # Vérifier les lignes
        for row in range(size):
            if self._check_sequence([grid[row][col] for col in range(size)], symbol):
                return True

        # Vérifier les colonnes
        for col in range(size):
            if self._check_sequence([grid[row][col] for row in range(size)], symbol):
                return True

        # Vérifier diagonales
        for row in range(size - self.win_length + 1):
            for col in range(size - self.win_length + 1):
                # Diagonale principale
                if self._check_diagonal(grid, row, col, symbol, 1, 1):
                    return True
                # Diagonale inverse
                if self._check_diagonal(grid, row + self.win_length - 1, col, symbol, -1, 1):
                    return True

        return False

    def _check_sequence(self, sequence: List[Optional[str]], symbol: str) -> bool:
        count = 0
        for cell in sequence:
            if cell == symbol:
                count += 1
                if count >= self.win_length:
                    return True
            else:
                count = 0
        return False

    def _check_diagonal(self, grid, start_row, start_col, symbol, row_inc, col_inc):
        count = 0
        row, col = start_row, start_col
        while 0 <= row < len(grid) and 0 <= col < len(grid):
            if grid[row][col] == symbol:
                count += 1
                if count >= self.win_length:
                    return True
            else:
                count = 0
            row += row_inc
            col += col_inc
        return False
