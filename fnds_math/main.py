import os
from rich import print as p
from rich.console import Console
from rich import pretty
pretty.install()
from rich.traceback import install
install()
from .addition import RandomABIntUpdater

updater = RandomABIntUpdater()

def main():
    response = "run"
    score = 0
    console = Console()

    while response != "q":
        correct, a, b = updater.update()

        os.system('clear')
        console.print(f"score = [bold magenta]{score}[/bold magenta]\n")
        console.print(f"What is the sum of\n\n[bold]{a} + {b} = ?[/bold]\n")
        console.print("quit = [bold red]q[/bold red]\n")

        response = input()
        if response == "q":
            os.system('clear')
            console.print(f"Your score is [bold green]{score}[/bold green]")
            break

        if int(response) == correct:
            os.system('clear')
            console.print("[bold green]correct[/bold green]")
            score += 1
        else:
            os.system('clear')
            console.print("[bold red]try again[/bold red]")

if __name__ == "__main__":
    main()