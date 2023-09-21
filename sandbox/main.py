# Importing the necessary modules and classes
import os
from rich.console import Console
from rich.panel import Panel
from math_dir.addition import Addision_game  
# from general_resource.fnds_functionality import ScreenManager, User
import general_resource.fnds_functionality as fnds
from general_resource.menu import Game_menu

# Initialize variables
score = 0
console = Console(force_terminal=True)
addision_instance = Addision_game()  # Create an instanßce of the Addision_game class
manager = fnds.ScreenManager()
# Clear screen on start
manager.clear_screen()

def main():
    # Select user
    user_name = Game_menu.login()
    user_data = fnds.User(user_name)
    score = user_data.score_count()
    
    # Game menu
    select_game = Game_menu.select_game()

    
    if int(select_game) == 1:
        addision_instance.game_loop(score=score , Panel=Panel, console=console, user=user_name)
    # if int(select_game) == 2:

if __name__ == "__main__":
    main()

