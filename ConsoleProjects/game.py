from Board import Board
from Player import Player


def check_win(player):
    win_horizontal = [2, 5, 8]
    win_vertical = [4, 5, 6]
    win_diagonal = [5]

    for each in player.moves:
        if each in win_horizontal:
            if (each - 1) in player.moves and (each + 1) in player.moves:
                print("Player {} wins!".format(player.name))
                return True
            else:
                return False
        elif each in win_vertical:
            if (each - 3) in player.moves and (each + 3) in player.moves:
                print("Player {} wins!".format(player.name))
                return True
            else:
                return False
        elif player.moves in win_diagonal:
            if ((each - 4) in player.moves and (each + 4) in player.moves) or (
                    (each - 2) in player.moves and (each + 2) in player.moves):
                print("Player {} wins!".format(player.name))
                return True
            else:
                return False


def check_move(player):
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