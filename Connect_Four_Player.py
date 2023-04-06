"""
This program contains the classes to allow two users to play the connect four game class.
A generic player class is created, a list containing the positions of each token of a 
particular player is initialised, and is used to check for a winning move.
"""
class Player:
    def __init__(self):
        self.player_tokens = []

    def get_move(self):
        pass
# classes for players 1 and 2 are created, the get_move function is created to only allow 
# valid inputs from the user, and is executed in the play function in the game module
class Player_1(Player):
    def __init__(self):
        super().__init__()
    
    def get_move(self):
        move = False
        while move is False:
            try:
                slot = int(input("Where will you take your turn?\t")) - 1
                if slot < 0 or slot > 6:
                    raise ValueError
                elif type(slot) != int:
                    raise TypeError
                move = True
            except (ValueError or TypeError):
                print("Invalid, please enter one of the available slots on the board...")
        return slot

class Player_2(Player):
    def __init__(self):
        super().__init__()
    
    def get_move(self):
        move = False
        while move is False:
            try:
                slot = int(input("Where will you take your turn?\t")) - 1
                if slot < 0 or slot > 6:
                    raise ValueError
                elif type(slot) != int:
                    raise TypeError
                move = True
            except (ValueError or TypeError):
                print("Invalid, please enter one of the available slots on the board...")
        return slot