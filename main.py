import validations
import tic_tac_board
import welcome


def start_game():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    round_no = 1
    left_positions = dict()

    while True:

        tic_tac_board.update_and_display_board(board)
        print('\n\t\t\t\t\t  X\'s 1 turn') if round_no % 2 else print('\n\t\t\t\t\t  0\'s 2 turn')

        index = input('\t\t\t\t   Choose position: ')
        if validations.validate_index(index):
            if int(index) not in left_positions:
                left_positions[int(index)] = 1
                index = int(index)
                if round_no % 2:
                    board[index - 1] = 'X'
                else:
                    board[index - 1] = '0'
                print('\n\n')
                tic_tac_board.update_and_display_board(board)
                if not tic_tac_board.check_for_remaining_moves(board):
                    print("\n\t\t\t    No more moves left. Tie!")
                    break
                if round_no >= 3:
                    if tic_tac_board.check_for_win(board):
                        print('\n\n\t\t\t\t   ┍━━━━━━━♔━━━━━━━┑\
                               \n\t\t\t\t\t     X won!\
                               \n\t\t\t\t   ┕━━━━━━━♔━━━━━━━┙') if round_no % 2 else print('\n\n\t\t\t\t   ┍━━━━━━━♔━━━━━━━┑\
                                                                                             \n\t\t\t\t\t     0 won!\
                                                                                              \n\t\t\t\t   ┕━━━━━━━♔━━━━━━━┙')
                        break
                round_no += 1
                print('\n' * 13)
            else:
                print('⚠The position is already occupied. Choose another position.⚠\n\n\n\n')
        else:
            print('  ⚠The position must be a number between 1 and 9. Choose again.⚠\n\n\n\n')


while True:
    welcome.welcome_screen()
    start_game()
    print('\n' * 7)
    print('\n\n\t\t   ╔═══════════ ∘◦ ☆ ◦∘ ════════════╗\
           \n\n\t\t       Do you want to play again?\
            \n\n\t\t              1 for yes\
             \n\n\t\t              0 for no\
           \n\n\t\t   ╚═══════════ ∘◦ ❉ ◦∘ ════════════╝')
    user_choice = input('\n\t\t\t\tType your option here: ')
    while validations.validate_user_choice(user_choice) == 0:
        print('\n' * 13)
        print('\t   ⚠Invalid answer. You should choose 0 if you\n\t   want to stop and 1 if you want to continue.⚠')
        print('\n\n\t\t   ╔═══════════ ∘◦ ☆ ◦∘ ════════════╗\
               \n\n\t\t       Do you want to play again?\
                \n\n\t\t              1 for yes\
                 \n\n\t\t              0 for no\
               \n\n\t\t   ╚═══════════ ∘◦ ❉ ◦∘ ════════════╝')
        user_choice = input('\n\t\t\t\tType your option here: ')

    if user_choice == '0':
        break

    print('\n' * 20)
