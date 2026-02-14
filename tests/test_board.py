import pytest
from tictactoe.game.board import Board

def test_place_symbol():
    b = Board(3)
    assert b.place_symbol(0, 0, "X") is True
    assert b.grid[0][0] == "X"

    # Essayer de placer sur la même case
    assert b.place_symbol(0, 0, "O") is False

# def test_is_full():
#     b = Board(2)
#     b.place_symbol(0,0,"X")
#     b.place_symbol(0,1,"O")
#     b.place_symbol(1,0,"X")
#     b.place_symbol(1,1,"O")

#     assert b.is_full() is True

def test_get_empty_cells():
    b = Board(2)
    b.place_symbol(0,0,"X")
    empty = b.get_empty_cells()
    
    assert empty == [(0,1), (1,0), (1,1)]
