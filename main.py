import welcome
import game
import reload_or_stop


while True:
    welcome.welcome_screen()
    game.start_game()
    reload_or_stop.reload_or_stop_game()
    print('\n' * 20)
