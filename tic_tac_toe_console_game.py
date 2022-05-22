class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign


class InvalidInputError(Exception):
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


first_player, second_player = read_players()
