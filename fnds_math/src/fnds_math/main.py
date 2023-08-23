import os
from rich import print as p
from rich.console import Console
from rich.traceback import install
install()
from addition import RandomABIntUpdater

updater = RandomABIntUpdater()

def main():
    response = "run"
    score = 0
    while response != "q":
        correct, a, b = updater.update()

        os.system('clear')
        p(f"score = {score}\n\nWhat is the sum of\n\n{a} + {b} = ?\n\nquit = q\n")

        response = input()
        if response == "q":
            os.system('clear')
            p(f"Your score is {score}")
            break

        if int(response) == correct:
            os.system('clear')
            p('correct')
            score += 1
        else:
            os.system('clear')
            p('try again')

if __name__ == "__main__":
    main()