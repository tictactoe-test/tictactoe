import pytest
from tictactoe.game.board import Board
from tictactoe.game.rules import Rules

def test_horizontal_win():
    b = Board(3)
    b.place_symbol(0,0,"X")
    b.place_symbol(0,1,"X")
    b.place_symbol(0,2,"X")
    r = Rules(3)
    assert r.check_winner(b, "X") is True

def test_vertical_win():
    b = Board(3)
    b.place_symbol(0,1,"O")
    b.place_symbol(1,1,"O")
    b.place_symbol(2,1,"O")
    r = Rules(3)
    assert r.check_winner(b, "O") is True

def test_diagonal_win():
    b = Board(3)
    b.place_symbol(0,0,"X")
    b.place_symbol(1,1,"X")
    b.place_symbol(2,2,"X")
    r = Rules(3)
    assert r.check_winner(b, "X") is True

def test_no_win():
    b = Board(3)
    b.place_symbol(0,0,"X")
    b.place_symbol(0,1,"O")
    b.place_symbol(0,2,"X")
    r = Rules(3)
    assert r.check_winner(b, "X") is False
