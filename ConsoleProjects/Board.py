import os


class Board:
    def __init__(self, dimensions: tuple, ticks: tuple):
        """
        Initialize the game board with specified dimensions

        :param
        dimensions: a tuple of dimensions x, y
        ticks: a tuple of two lists with the locations of the ticks from each player
        """
        self.height = dimensions[0]
        self.width = dimensions[1]
        self.tick_player_1 = ticks[0]
        self.tick_player_2 = ticks[1]

        self.show_board()

    def show_board(self):
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
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_player(self, idx):
        if idx in self.tick_player_1:
            return 'X'
        elif idx in self.tick_player_2:
            return '*'
        else:
            return "{}".format(idx)
