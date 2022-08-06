def validate_index(index):
    if len(index) > 1:
        return 0
    if index.isdigit() == 0:
        return 0
    return 1 <= int(index) <= 9


def validate_user_choice(choice):
    if len(choice) > 1:
        return 0
    return choice in ['1', '0']
