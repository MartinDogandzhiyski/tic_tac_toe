class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign


class InvalidNumberError(Exception):
    pass


class InvalidPositionError(Exception):
    pass


def read_players():
    first_player_name = input(f"Player one name: ")
    second_player_name = input(f"Player two name: ")
    second_player_sign = ''
    while True:
        first_player_sign = input(f"{first_player_name}, what sign you want?: ").upper()
        if first_player_sign == 'X':
            second_player_sign = 'O'
            break
        elif first_player_sign == 'O':
            second_player_sign = 'X'
            break
        continue
    print(f"{first_player_name} sign is {first_player_sign}")
    print(f"{second_player_name} sign is {second_player_sign}")
    return Player(first_player_name, first_player_sign), Player(second_player_name, second_player_sign)


def print_board_numeration():
    print("This is the numeration of the board:")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")


def check_number(position):
    if 0 > position or position > 9:
        raise InvalidNumberError


def if_is_valid_pos(board, board_mapper, position):
    row, col = board_mapper[position]
    return row, col


def print_board(board):
    for i in board:
        print('| ', end="")
        print(' | '.join([str(x) for x in i]), end="")
        print(' |')


def is_winner(board):
    result = False
    for i in board:
        if i[0] == i[1] == i[2]:
            result = True
            break

    if board[0][0] == board[1][0] == board[2][0] or board[0][1] == board[1][1] == board[2][1] or board[0][2] == board[1][2] == board[2][2] or board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        result = True

    return result


def is_draw(board):
    result = True
    for i in board:
        for n in i:
            if n != 'X' and n != 'O':
                result = False
    return result



first_player, second_player = read_players()


print_board_numeration()

print(f"{first_player.name} starts first!")


board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
         ]
board_mapper = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2],
}

turn = 1
while True:
    current_player = first_player if turn % 2 != 0 else second_player
    try:
        position = int(input(f"{current_player.name} choose a free position [1-9]:"))
        check_number(position)
        row, col = if_is_valid_pos(board, board_mapper, position)
        if board[row][col] == 'X' or board[row][col] == 'O':
            raise InvalidPositionError
        else:
            board[row][col] = current_player.sign
    except ValueError:
        print("Please select number!")
        continue
    except InvalidNumberError:
        print("Please select number between [1-9]:")
        continue
    except InvalidPositionError:
        print("Please be sure that there is free space on this position! Input new one:")
        continue

    print_board(board)

    if is_winner(board) == True:
        winner = current_player.name
        print(f"{winner} is winner!")
        break

    if is_draw(board) == True:
        print("Draw!")
        break

    turn += 1