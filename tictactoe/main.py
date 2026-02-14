from tictactoe.game.board import Board

b = Board(3)
b.place_symbol(0, 0, "X")
print(b.grid)
