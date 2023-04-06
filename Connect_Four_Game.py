"""
This program runs a game of command line connect four.
A 6x7 board is created, and the columns labelled to allow users to easily locate where they 'place' tokens.
It is created for 2 players, in place of the classic red and yellow, just '1' or '2' is used.
A seperate package is imported containing classes to run the individual players functions.
-------------------------------------------------------
The class starts by initialising the 'board' being played on, the winner (upon starting holds no value),
and the available moves (done by iterating through the board and adding each position to a list, this
way it will work for any dimensions the board holds)
"""
# import the classes for the 2 players
from Connect_Four_Player import Player_1, Player_2

class Connect_Four:
    def __init__(self):
        self.board = [([" "] * 7) for i in range(6)]
        self.winner = None
        self.available_moves = []
        for m in range(len(self.board)):
            for n in range(len(self.board[0])):
                self.available_moves.append((m, n))
    # print the board and format it to be used in the command line
    def printboard(self):
        board_index =[[str(i + 1) for i in range(7)]]
        for e in board_index:
            print("  " + "   ".join(e))
        for row in self.board:
            print("| " + " | ".join(row) + " |")
        print("-" * 29)
    # store each token location for the players
    def turn_made(self, turn, player):
        self.available_moves.remove(turn)
        player.append(turn)
    # "drop" the player's token to the bottom-most available row
    def player_turn(self, turn, player, letter):
        for i in range(6):
            slot = 5 - i, turn
            if slot in self.available_moves:
                self.board[slot[0]][slot[1]] = letter
                self.turn_made(slot, player)
                return slot
        return False
    # check for a horizontal win
    def check_horizontal(self, turn, player):
        count = 0
        while count < 4:
            for i in range(4):
                if (turn[0], turn[1] + i) in player:
                    count += 1
                else:
                    for j in range(1, 4):
                        if (turn[0], turn[1] - j) in player:
                            count += 1
                        else: return False
        return True
    # check for a vertical win
    def check_vertical(self, turn, player):
        count = 0
        while count < 4:
            for i in range(4):
                if (turn[0] + i, turn[1]) in player:
                    count += 1
                else:
                    for j in range(1, 4):
                        if (turn[0] - j, turn[1]) in player:
                            count += 1
                        else: return False
        return True
    # check for a diagonal win correlating to a line x=y
    def check_posx(self, turn, player):
        count = 0
        for i in range(4):
            if (turn[0] - i, turn[1] + i) in player:
                count += 1
                if count == 4:
                    return True
            else:
                for j in range(1, 4):
                    if (turn[0] + j, turn[1] - j) in player:
                        count += 1
                        if count == 4:
                            return True
                    else: return False
    # check for a diagonal win correlating to a line -x=y
    def check_negx(self, turn, player):
        count = 0
        for i in range(4):
            if (turn[0] - i, turn[1] - i) in player:
                count += 1
                if count == 4:
                    return True
            else:
                for j in range(1, 4):
                    if (turn[0] + j, turn[1] + j) in player:
                        count += 1
                        if count == 4:
                            return True
                    else: return False
    # run the two diagonal checks
    def check_diagonal(self, turn, player):
        check = self.check_posx(turn, player)
        if check is True:
            return True
        else:
            check = self.check_negx(turn, player)
            if check is True:
                return True
            else: return False
    # run each check to find a winner
    def check_winner(self, turn, player, letter):
        check = self.check_horizontal(turn, player)
        if check is True:
            self.winner = letter
            return True
        else:
            check = self.check_vertical(turn, player)
            if check is True:
                self.winner = letter
                return True
            else:
                check = self.check_diagonal(turn, player)
                if check is True:
                    self.winner = letter
                    return True
                else: return False


# this function runs the game, the classes for the two players, and the game are the parameters
def play(game, p1, p2, printgame=True):
    if printgame:
        game.printboard()
    letter = "1"# the game starts with player 1
    while game.available_moves:# run the game until there are no moves available
        print(f"Player {letter}...")
        turn = False
        while turn is False:
            try:
                if letter == "1":
                    move = p1.get_move()
                    player = p1.player_tokens
                    turn = game.player_turn(move, player, letter)
                else:
                    move = p2.get_move()
                    player = p2.player_tokens
                    turn = game.player_turn(move, player, letter)
                if turn is False:
                    raise ValueError
            except ValueError:
                print("Please choose an available slot.")
        slot = move + 1
        if turn:
            if printgame:
                print(f"Player {letter} plays in slot {slot}.")
                game.printboard()
            if game.check_winner(turn, player, letter):
                return print(f"Player {game.winner} is the winner!")
        letter = "2" if letter == "1" else "1"# change player when turn is made
    return print("No moves left! It is a draw.")
# assign the player classes, and game class, add the parameters to the play function
if __name__ == "__main__":
    p1 = Player_1()
    p2 = Player_2()
    four = Connect_Four()
    play(four, p1, p2, printgame=True)