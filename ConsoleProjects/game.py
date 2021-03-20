from Board import Board
from Player import Player


def check_win(player):
    """

    :param player: An object of Player class, representing each player who makes a move
    :return: True if player has won else False
    """
    win_horizontal = [2, 8]
    win_vertical = [4, 6]
    win_center = [5]

    last_move = player.moves[-1]

    if last_move in win_horizontal:
        if (last_move - 1) in player.moves and (last_move + 1) in player.moves:
            print("Player {} wins!".format(player.name))
            return True
        else:
            return False

    if last_move in win_vertical:
        if (last_move - 3) in player.moves and (last_move + 3) in player.moves:
            print("Player {} wins!".format(player.name))
            return True
        else:
            return False

    if last_move in win_center:
        diagonal = ((last_move - 4) in player.moves and (last_move + 4) in player.moves) or (
                (last_move - 2) in player.moves and (last_move + 2) in player.moves)
        horizontal = (last_move - 1) in player.moves and (last_move + 1) in player.moves
        vertical = (last_move - 3) in player.moves and (last_move + 3) in player.moves
        if diagonal or horizontal or vertical:
            print("Player {} wins!".format(player.name))
            return True
        else:
            return False

    if len(b.boxes) == 0:
        print("Draw!!!")
        return True


def check_move(player):
    """
    Checks if the move is valid if mot removes the last move and prompts player to make a new one
    :param player: The player who made the move
    """
    last_move = player.moves[-1]
    try:
        b.boxes.remove(last_move)
    except ValueError:
        print("This move is already taken")
        player.add_move()
        check_move(player)


if __name__ == "__main__":
    player1 = Player()
    player2 = Player()
    b = Board((3, 3))
    b.show_board(player1.moves, player2.moves)

    while True:
        player1.add_move()
        check_move(player1)
        b.show_board(player1.moves, player2.moves)
        if check_win(player1):
            break

        player2.add_move()
        check_move(player2)
        b.show_board(player1.moves, player2.moves)
        if check_win(player2):
            break
