from tictactoe.game.game_manager import GameManager

gm = GameManager(3)
gm.start_game("X")

gm.make_move(0,0)
gm.make_move()

for row in gm.board.grid:
    print(row)

print("Current player:", gm.current_player)
print("Game over:", gm.game_over)
