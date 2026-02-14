from tictactoe.game.board import Board
from tictactoe.game.rules import Rules
from tictactoe.game.ai import RandomAI

b = Board(3)
ai = RandomAI()

b.place_symbol(0, 0, "X")
b.place_symbol(0, 1, "X")
b.place_symbol(0, 2, "X")

row, col = ai.choose_move(b)
b.place_symbol(row, col, "O")

r = Rules(win_length=3)
print("X a gagné ?", r.check_winner(b, "X"))
print("O a joué en :", (row, col))
