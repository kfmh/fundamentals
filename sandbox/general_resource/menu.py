from rich.console import Console
from rich.panel import Panel

console = Console(force_terminal=True)

class Game_menu:
    def __init__(self):
        pass
    
    def input():
        print("[bold cyan]Welcome to the Addition Quiz![/bold cyan]")
        print("Type [bold red]1 = Addision[/bold red]")
        print("Type [bold red]q[/bold red] anytime to quit.")
        game_choice = input("> ")
        return game_choice


    def login():
        console.print("Type [bold red]Username: [/bold red]")
        username = input("> ")
        return username
        

    def select_game():
        """
        Displays the introduction message.
        
        Args:
            console (Console): Rich Console instance for printing formatted output.
        """
        console.print(Panel("[bold cyan]Welcome to the Addition Quiz![/bold cyan]"))
        console.print("Type [bold red]1 = Addision[/bold red]")
        console.print("Type [bold red]q[/bold red] anytime to quit.")
        game_choice = input("> ")
        return game_choice
    

