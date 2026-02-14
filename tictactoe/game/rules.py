from .board import Board

class Rules:
    def __init__(self, win_length: int):
        self.win_length = win_length

    def check_winner(self, board: Board, symbol: str) -> bool:
        size = board.size
        grid = board.grid

        directions = [
            (0, 1),
            (1, 0),
            (1, 1),
            (1, -1),
        ]

        for row in range(size):
            for col in range(size):
                if grid[row][col] != symbol:
                    continue

                for d_row, d_col in directions:
                    if self._check_direction(grid, row, col, symbol, d_row, d_col):
                        return True

        return False

    def _check_direction(self, grid, row, col, symbol, d_row, d_col):
        count = 0
        size = len(grid)

        while 0 <= row < size and 0 <= col < size:
            if grid[row][col] == symbol:
                count += 1
                if count == self.win_length:
                    return True
            else:
                break

            row += d_row
            col += d_col

        return False
