# Importing the necessary modules and classes
from rich.console import Console
from rich.panel import Panel
from addition import Addision_game  
from general_resource.fnds_functionality import *
from general_resource.menu import Game_menu

# Initialize variables
score = 0
console = Console(force_terminal=True)
addision_instance = Addision_game()  # Create an instanßce of the Addision_game class
manager = ScreenManager()

# Clear screen on start
manager.clear_screen()

def main():
    quit = False
    while quit != "quit":
        # Select user
        user_name = Game_menu.login()
        user_data = User(user_name)
        try:
            score = user_data.score_count()
        except IndexError:
            score = 0
    
        # Game menu
        select_game = Game_menu.select_game()
        quit = select_game

        if quit == "quit":
            break

        elif int(select_game) == 1:
            addision_instance.game_loop(score=score, Panel=Panel, console=console, user=user_name)
        # if int(select_game) == 2:

if __name__ == "__main__":
    main()

