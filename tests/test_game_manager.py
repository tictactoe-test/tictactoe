# from tictactoe.game.game_manager import GameManager

# def test_human_win():
#     gm = GameManager(size=3)
#     gm.start_game("X")
#     gm.make_move(0,0)
#     gm.make_move(1,0)
#     gm.make_move(0,1)
#     gm.make_move(1,1)
#     result = gm.make_move(0,2)
#     assert result == "X a gagné !"
#     assert gm.game_over is True

# def test_draw():
#     gm = GameManager(size=2)
#     gm.start_game("X")
#     gm.make_move(0,0)
#     gm.make_move()
#     gm.make_move(0,1)
#     gm.make_move()
#     assert gm.game_over is True
