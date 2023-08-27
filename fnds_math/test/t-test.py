import os
from rich.console import Console
from rich.panel import Panel
from addition import RandomABIntUpdater  # Importing the necessary modules and classes
from timer_ import Avg_TTA, AnswerTracker  # Importing the necessary modules and classes
from time import sleep

# Creating an instance of RandomABIntUpdater class
updater = RandomABIntUpdater()

def clear_screen():
    """Clears the terminal screen."""
    os.system('clear' if os.name == 'posix' else 'cls')

def display_intro(console):
    """
    Displays the introduction message.
    
    Args:
        console (Console): Rich Console instance for printing formatted output.
    """
    console.print(Panel("[bold cyan]Welcome to the Addition Quiz![/bold cyan]"))
    console.print("Test your addition skills. Type [bold red]q[/bold red] anytime to quit.")

def display_question(console, score, a, b):
    """
    Displays the question to the user.
    
    Args:
        console (Console): Rich Console instance for printing formatted output.
        score (int): Current score of the user.
        a (int): First integer of the addition.
        b (int): Second integer of the addition.
    """
    clear_screen()
    console.print(f"Score: [bold magenta]{score}[/bold magenta]\n")
    console.print(f"What is the sum of\n\n[bold cyan]{a} + {b} = ?[/bold cyan]")
    console.print("\nType [bold red]q[/bold red] to quit.")

def main():
    response = "run"
    score = 0
    console = Console(force_terminal=True)

    timer = Avg_TTA()

    tracker = AnswerTracker()

    clear_screen()
    display_intro(console)
    sleep(2)


    while response != "q":
        correct, a, b = updater.update()

        display_question(console, score, a, b)
        timer.start()

        response = input("> ")

        if response == "q":
            clear_screen()
            console.print(Panel(f"Your final score is [bold green]{score}[/bold green]", expand=False))
            break

        try:
            user_response = int(response)
            if user_response == correct:
                score += 1
                tracker.add_correct()
                console.print("[bold green]Correct! Well done![/bold green]\n")
                timer.log_time(console)
            else:
                tracker.add_wrong()
                console.print(f"[bold red]Oops! That's incorrect. \n{a} + {b} = {correct}[/bold red]\n")
            
        except ValueError:
            console.print("[bold yellow]Invalid input. Please enter a number or 'q' to quit.[/bold yellow]\n")

        fraction = tracker.fraction_wrong_over_correct()
        if fraction is not None:
            print(f"Fraction of wrong answers over correct answers: {fraction:.2f}")
        else:
            print("No correct answers recorded yet.")
        sleep(2)

if __name__ == "__main__":
    main()


