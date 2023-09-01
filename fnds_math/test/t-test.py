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
    console.print("Type [bold red]1 = Addision[/bold red]")
    console.print("Type [bold red]2 = Play Doors[/bold red]")
    console.print("Type [bold red]q[/bold red] anytime to quit.")
    game_choice = input("> ")
    return game_choice


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

def doors():
# Countdown process
    # import threading
    # import time

    # def countdown(seconds):
    #     time.sleep(seconds)
    #     print("\nCountdown finished!")

    # # Start the countdown in a separate thread
    # countdown_thread = threading.Thread(target=countdown, args=(10,))
    # countdown_thread.start()

    # # Foreground tasks
    # for i in range(1, 6):
    #     print(f"Foreground task: {i}")
    #     time.sleep(1)

    # # Wait for the countdown thread to finish
    # countdown_thread.join()

# ---------------
    # Challenge 1: The Cipher Key (Caesar cipher)
    # Prime facotor a number and user the secons smallest prime as key to solv a Cecar cipher
    # the responce of the scifer is a url that lead to next challange.

    # Challenge 2: Steganographic Clue Hunt
    # message On this screen are 4 numbers, find them.
    # 4 in the clue message, 
    # 5 as the greek letter (V), 
    # 10 the url as letters (ten), 
    # 8 as a hidden in the visual as a woman tha just (eight) dinner.
    # Sum up the numbers to get 27

    # Challenge 3: Logic Lock
    # 1. Slipt the numer right down the middle
    # 2. Write the two numbers in 4bit binary
    # 3. What is the square root of the sum of all bits

    # Challenge 4: The Enigmatic Code
    # Riddle = I am hidden in a cude of x. x = 2
    # Crack another cecar cipher
    
    # Challenge 5: The Techno-Riddle
    # Challenge 6: The Virtual Maze
    # Challenge 7: The Multilayered Puzzle
    # Challenge 8: The Decoding Relay
    # Challenge 9: The Riddle of Reflection
    # Challenge 10: The Collaborative Cipher Wheel
    # Challenge 11: The Binary Quest
    # Challenge 12: The Puzzle Marathon
    # Challenge 13: The Grand Convergence
    print("Doors")

def addision_game(score, response, console):
    timer = Avg_TTA()
    tracker = AnswerTracker()

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
            print(f"Fraction of wrong answers over total answers: {fraction:.2f}")
        else:
            print("No correct answers recorded yet.")
        print(input("Press enter"))

def main():
    response = "run"
    score = 0
    console = Console(force_terminal=True)


    clear_screen()
    game_choice = display_intro(console)
    if int(game_choice) == 1:
        addision_game(score, response, console)
    else: 
        doors()



if __name__ == "__main__":
    main()


