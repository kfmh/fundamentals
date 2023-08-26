import os
from rich.console import Console
from rich.panel import Panel
from addition import RandomABIntUpdater
from time import sleep

updater = RandomABIntUpdater()

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def display_intro(console):
    console.print(Panel("[bold cyan]Welcome to the Addition Quiz![/bold cyan]"))
    console.print("Test your addition skills. Type [bold red]q[/bold red] anytime to quit.")
    console.print(hr())

def display_question(console, score, a, b):
    clear_screen()
    console.print(f"Score: [bold magenta]{score}[/bold magenta]\n")
    console.print(f"What is the sum of\n\n[bold cyan]{a} + {b} = ?[/bold cyan]")
    console.print("\nType [bold red]q[/bold red] to quit.")

def hr():
    return "-"*50

def main():
    response = "run"
    score = 0
    console = Console(force_terminal=True)

    display_intro(console)
    sleep(2)

    while response != "q":
        correct, a, b = updater.update()

        display_question(console, score, a, b)

        response = input("> ")

        if response == "q":
            clear_screen()
            console.print(Panel(f"Your final score is [bold green]{score}[/bold green]", expand=False))
            break

        try:
            user_response = int(response)
            if user_response == correct:
                score += 1
                console.print("[bold green]Correct! Well done![/bold green]\n")
                console.print(hr())
            else:
                console.print(f"[bold red]Oops! That's incorrect. \n{a} + {b} = {correct}[/bold red]\n")
                console.print(hr())
                
        except ValueError:
            console.print("[bold yellow]Invalid input. Please enter a number or 'q' to quit.[/bold yellow]\n")
            console.print(hr())
        sleep(2)

if __name__ == "__main__":
    main()
