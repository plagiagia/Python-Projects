import os


class Board:
    def __init__(self, dimensions: tuple):
        """
        Initialize the game board with specified dimensions

        :param
        dimensions: a tuple of dimensions x, y
        ticks: a tuple of two lists with the locations of the ticks from each player
        """
        self.height = dimensions[0]
        self.width = dimensions[1]
        self.boxes = [i for i in range(1, (self.height * self.width) + 1)]
        self.tick_player_1 = []
        self.tick_player_2 = []

    def show_board(self, player1_moves, player2_moves):
        """

        :param player1_moves: Moves of first player
        :param player2_moves: Moves of second player
        :return: A board of w x h dimensions
        """
        self.tick_player_1 = player1_moves
        self.tick_player_2 = player2_moves
        self.clear_screen()
        right = "__{}__|"
        left = "__{}__"
        bottom_right = "  {}  |"
        bottom_left = "  {} "

        mul = 0
        for h in range(self.height):
            for w in range(self.width):
                if h == self.height - 1:
                    if (w + 1) % self.height == 0:
                        print(bottom_left.format(self.draw_player((h + w + 1) + mul)), end='\n')
                    else:
                        print(bottom_right.format(self.draw_player((h + w + 1) + mul)), end='')
                else:
                    if (w + 1) % self.width == 0:
                        print(left.format(self.draw_player((h + w + 1) + mul)), end='\n')
                        mul += 2
                    else:
                        print(right.format(self.draw_player((h + w + 1) + mul)), end='')

    @staticmethod
    def clear_screen():
        """
        Clears the screen each time is called also checks the OS
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_player(self, idx):
        """
        :param idx: index of the move
        :return: Prints the a appropriate symbol for each player
        """
        if idx in self.tick_player_1:
            return 'X'
        elif idx in self.tick_player_2:
            return '*'
        else:
            return "{}".format(idx)
