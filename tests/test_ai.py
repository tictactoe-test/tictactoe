from tictactoe.game.board import Board
from tictactoe.game.ai import RandomAI

def test_ai_move():
    b = Board(3)
    ai = RandomAI()
    row, col = ai.choose_move(b)
    assert (row, col) in b.get_empty_cells()

def test_ai_no_move():
    b = Board(1)
    b.place_symbol(0,0,"X")
    ai = RandomAI()
    import pytest
    with pytest.raises(ValueError):
        ai.choose_move(b)
