from typing import List, Optional, Tuple


class Board:
    def __init__(self, size: int) -> None:
        self.size = size
        self.grid: List[List[Optional[str]]] = []
        self.reset()

    def reset(self) -> None:
        self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]

    def place_symbol(self, row: int, col: int, symbol: str) -> bool:
        if not self.is_cell_empty(row, col):
            return False

        self.grid[row][col] = symbol
        return True

    def is_cell_empty(self, row: int, col: int) -> bool:
        return self.grid[row][col] is None

    def get_empty_cells(self) -> List[Tuple[int, int]]:
        empty_cells = []

        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] is None:
                    empty_cells.append((row, col))

        return empty_cells

    def is_full(self) -> bool:
        return all(cell is not None for row in self.grid for cell in row)

    def get_symbol(self, row: int, col: int) -> Optional[str]:
        return self.grid[row][col]
