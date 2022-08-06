import validations


def reload_or_stop_game():
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
