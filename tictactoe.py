from random import randint

class Game:
    def __init__(self):
        self.player = "x"
        self.computer = "o"
        self.board = [" " for n in range(9)]
        self.game_playing = True

    def draw_board(self):
        print("\n" + self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("-"*10)
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("-"*10)
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8] + "\n")

    def make_move(self, move_from):
        if " " not in self.board: # draw
            self.game_playing = False
        else:
            if self.game_playing:
                if move_from == self.player:
                    while True:
                        move = int(input())
                        if self.board[move] == " ":
                            self.board[move] = self.player
                            break
                        else:
                            continue

                else:
                    while True:
                        move = randint(0, 8)
                        if self.board[move] == " ":
                            self.board[move] = self.computer
                            break
                        else:
                            continue
            else: # win
                pass

    def check_win(self, check_from):
        wins = (
            "012", "345", "678", # across
            "036", "147", "258", # down
            "048", "246"         # diagonal
        )

        for a, b, c in wins:
            a, b, c = int(a), int(b), int(c)
            if self.board[a] == check_from and self.board[b] == check_from and self.board[c] == check_from:
                self.game_playing = False
            else:
                pass

    def game_loop(self):
        while self.game_playing:
            self.make_move(self.player)
            self.check_win(self.player)
            self.draw_board()
            self.make_move(self.computer)
            self.check_win(self.computer)
            self.draw_board()

game = Game()
game.game_loop()