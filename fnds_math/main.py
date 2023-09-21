# Importing the necessary modules and classes
import os
from rich.console import Console
from rich.panel import Panel
from addition import Addision_game  
from general_resource.fnds_functionality import ScreenManager
from general_resource.menu import Game_menu

# Initialize variables
score = 0
console = Console(force_terminal=True)
addision_instance = Addision_game()  # Create an instanßce of the Addision_game class
manager = ScreenManager()

# Clear screen on start
cs = manager.clear_screen()
cs

def main():
    # Game menu
    select_game = Game_menu.select_game(console, Panel)
    
    if int(select_game) == 1:
        addision_instance.game_loop(score=score, Panel=Panel, console=console)
    # if int(select_game) == 2:

if __name__ == "__main__":
    main()

