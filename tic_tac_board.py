def update_and_display_board(board):
    print(f'\t\t\t\t ＿＿＿＿ ＿＿＿＿ ＿＿＿＿')
    print('\t\t\t\t｜     ｜      ｜      ｜')
    print(f'\t\t\t\t｜  {board[0]}  ｜   {board[1]}  ｜   {board[2]}  ｜')
    print('\t\t\t\t｜     ｜      ｜      ｜')
    print('\t\t\t\t ＿＿＿＿ ＿＿＿＿ ＿＿＿＿')
    print('\t\t\t\t｜     ｜      ｜      ｜')
    print(f'\t\t\t\t｜  {board[3]}  ｜   {board[4]}  ｜   {board[5]}  ｜')
    print('\t\t\t\t｜     ｜      ｜      ｜')
    print('\t\t\t\t ＿＿＿＿ ＿＿＿＿ ＿＿＿＿')
    print('\t\t\t\t｜     ｜      ｜      ｜')
    print(f'\t\t\t\t｜  {board[6]}  ｜   {board[7]}  ｜   {board[8]}  ｜')
    print('\t\t\t\t｜     ｜      ｜      ｜')
    print('\t\t\t\t ＿＿＿＿ ＿＿＿＿ ＿＿＿＿')


def check_for_win(board):
    #                   first row                           second row                              third row
    return ((board[0] == board[1] == board[2]) or (board[3] == board[4] == board[5]) or (board[6] == board[7] == board[8])) or \
           ((board[0] == board[3] == board[6]) or (board[1] == board[4] == board[7]) or (board[2] == board[5] == board[8])) or \
           (board[6] == board[4] == board[2]) or (board[0] == board[4] == board[8])


def check_for_remaining_moves(board):
    for location in board:
        if location in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return True
    return False
