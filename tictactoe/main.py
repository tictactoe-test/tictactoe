from tictactoe.game.board import Board
from tictactoe.game.rules import Rules

b = Board(3)
b.place_symbol(0, 0, "X")
b.place_symbol(0, 1, "X")
b.place_symbol(0, 2, "X")

r = Rules(win_length=3)
print("X a gagné ?", r.check_winner(b, "X"))

