class Player:
    def __init__(self):
        self.name = '{}'.format(input('\n Name your player: '))
        self.moves = []
        self.score = 0

    def add_move(self):
        print("{}:choose an index to place your tic".format(self.name))
        move = int(input())
        self.moves.append(move)

    def remove_move(self):
        self.moves.pop()

    def add_win(self):
        self.score += 1
