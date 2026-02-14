from tictactoe.game.game_manager import GameManager

class TicTacToeCLI:
    def __init__(self, size=3):
        self.game = GameManager(size=size)

    def print_board(self):
        size = self.game.board.size

        print("   " + "   ".join(str(i) for i in range(size)))
        print("  " + "----" * size)
        
        for i, row in enumerate(self.game.board.grid):
            row_display = [cell if cell is not None else " " for cell in row]
            print(f"{i} | " + " | ".join(row_display) + " |")
            print("  " + "----" * size)

    def choose_symbol(self):
        symbol = ""
        while symbol not in ["X", "O"]:
            symbol = input("Choisissez votre symbole (X ou O) : ").upper()
        return symbol

    def play(self):
        while True:
            human_symbol = self.choose_symbol()
            self.game.start_game(human_symbol)
            
            print("\nLa partie commence !\n")
            self.print_board()

            while not self.game.game_over:
                if self.game.current_player == self.game.human_symbol:
                    move_valid = False
                    while not move_valid:
                        try:
                            coords = input("Entrez votre coup (row,col) : ")
                            row, col = map(int, coords.split(","))
                            result = self.game.make_move(row, col)
                            move_valid = True
                        except Exception as e:
                            print("Erreur :", e)
                else:
                    print("\nAu tour de l'ordinateur : \n")
                    result = self.game.make_move()

                self.print_board()

                if result:
                    print(result)

            replay = input("Voulez-vous rejouer ? (O/N) : ").upper()
            if replay != "O":
                print("Merci d'avoir joué !")
                break
