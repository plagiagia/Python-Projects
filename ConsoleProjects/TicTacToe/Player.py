class Player:

    def __init__(self):
        self.name = '{}'.format(input('\n Name your player: '))
        self.moves = []
        self.score = 0

    def add_move(self):
        """
        Adds a move to a list of moves for each player
        :return:
        """
        print("{}:choose an index to place your tic".format(self.name))
        move = int(input())
        self.moves.append(move)

    def remove_move(self):
        """
        Removes the last move of a player in case the move is already played
        :return:
        """
        self.moves.pop()

    def add_win(self):
        """
        Add a point to a player in case of a win
        :return:
        """
        self.score += 1
