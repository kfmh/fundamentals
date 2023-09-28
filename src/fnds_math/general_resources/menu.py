from rich.console import Console
from rich.panel import Panel
from .fnds_functionality import *
import os
console = Console(force_terminal=True)
gr = GameResponse()

class Game_menu:
    def __init__(self):
        pass
    
    # def input():
    #     print(f"[bold cyan]Welcome to the Addition Quiz![/bold cyan]")
    #     print("Type [bold red]1 = Addision[/bold red]")
    #     print("Type [bold red]q[/bold red] anytime to quit.")
    #     game_choice = gr.game_response()
    #     return game_choice


    def login():
        console.print("Type [bold red]Select user: [/bold red]")
        
        # Directory path where you want to search for CSV files
        # directory_path = "/path/to/your/directory"
        # Check if the CSV file exists
        directory_path = os.path.dirname(os.path.abspath(__file__))

        # Get a list of all files in the directory
        file_list = os.listdir(f"{directory_path}/user_data")

        # Filter the list to include only CSV files
        csv_files = [file for file in file_list if file.endswith(".csv")]

        # Print the list of CSV files
        for csv_file in csv_files:
            print(csv_file[0:-4])

        username = gr.game_response() 
        return username
        

    def select_game(user_name, new_player):
        """
        Displays the introduction message.
        
        Args:
            console (Console): Rich Console instance for printing formatted output.
        """
        if new_player:
            console.print(Panel(f"[bold cyan]Welcome {user_name}! To the Fundamentals Dojo![/bold cyan]"))
        else:
            console.print(Panel(f"[bold cyan]Nice to se you again {user_name}! \nLets Go![/bold cyan]"))
        console.print("Type [bold red]1 = Addision[/bold red]")
        console.print("Type [bold red]q[/bold red] anytime to quit.")
        game_choice = gr.game_response()
        return game_choice
    

