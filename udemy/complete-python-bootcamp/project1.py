# from IPython.display import clear_output

is_end = False
# clear_output()
game_board = {}
player_turn = 1

players = {
    '1': {
        'history': [],
        'symbol': 'X'
    },
    '2': {
        'history': [],
        'symbol': 'O'
    }
}
turn_count = 0


def check_for_winners():
    # print('check_for_winners')
    if turn_count <= 4:
        return False
    if (check_for_winner(players['1']['history'])):
        return 1
    if (check_for_winner(players['2']['history'])):
        return 2
    return False

def check_for_winner(player_moves):
    # print('check_for_winner')
    # horizontal
    # 0,1,2  3,4,5  6,7,8
    # vertical
    # 0,3,6  1,4,7  1,5,8
    # cross
    # 0,4,8  2,4,6
    win_move_sets = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    # print(player_moves)
    
    for moves in win_move_sets:
        is_win = True
        for m in moves:
            if m not in player_moves:
                is_win = False
                break
        if is_win:
            print('win by', moves)
            return True
    return False


def get_player_symbol(player_no):
    if player_no != 1 and player_no != 2:
        raise Exception('Invalid player no.')
    return players[str(player_no)]['symbol']


def set_player_history(player_no, move):
    if player_no != 1 and player_no != 2:
        raise Exception('Invalid player no.')
    return players[str(player_no)]['history'].append(move)


def print_game_board():
    print('---------')
    for x in range(9):
        cell = str((x + 1)) if x not in game_board else game_board[x]
        print(cell, end="")
        if ((x + 1) % 3 == 0):
            print('\n---------')
        else:
            print(' | ', end="")


while not is_end:
    # clear_output(wait=True)
    print_game_board()
    move = 0
    while True:
        step = input(
            'Player {} - {} [1-9]: '.format(
                player_turn, 
                get_player_symbol(player_turn)
            )
        )
        try:
            move = int(step) - 1
            if (move in game_board):
                pass
            elif move >= 0 and move <= 8:
                break
        except Exception as ex:
            pass
        print('Wrong move!')

    game_board[move] = get_player_symbol(player_turn)
    set_player_history(player_turn, move)
    # print output
    turn_count += 1
    
    is_win = check_for_winners()
    if (is_win):
        is_end = True
        print_game_board()
        print('Player {} - {}\nWIN! Congraturation!'.format(is_win, get_player_symbol(is_win)))

    player_turn = 2 if player_turn == 1 else 1

    if (turn_count >= 9):
        # end game
        is_end = True
        print('DRAW!')

# else:
#     print('Thank you')

