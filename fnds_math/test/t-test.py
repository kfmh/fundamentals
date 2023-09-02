import os
from rich.console import Console
from rich.panel import Panel
from addition import Addision_game  # Importing the necessary modules and classes
from time import sleep
from doors import Countdonw_Threade, Cicada_13
from menu import Game_menu

score = 0
console = Console(force_terminal=True)
game_instance = Addision_game()  # Create an instance of the Addision_game class
cicada_instance = Cicada_13()

def clear_screen():
    """Clears the terminal screen."""
    # Check if OS is POSIX compliant (e.g., Linux, macOS)
    if os.name == 'posix':
        print("\033c", end="")  # ANSI escape sequence to clear screen
    else:
        os.system('cls')  # Windows command to clear screen
clear_screen()



def main():
    select_game = Game_menu.select_game(console, Panel)
    
    if int(select_game) == 1:
        game_instance.game_loop(score=score, Panel=Panel, clear_screen=clear_screen, console=console)
    if int(select_game) == 2:
        cicada_instance.game_loop(clear_screen=clear_screen) 


if __name__ == "__main__":
    main()

