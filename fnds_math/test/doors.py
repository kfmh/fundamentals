import threading
import time
from rich.console import Console
from rich.panel import Panel
import webbrowser
from time import sleep
import pandas as pd
from tabulate import tabulate

console = Console(force_terminal=True)

def answer(correct_response, response_type):
    response = input("Enter command: ")
    cr = correct_response
    if response_type == "int":
        response = int(response)
    if response_type == "str":
        response = response.upper()
        cr = correct_response.upper()

    if response == cr:
        problem_solved = True
        print("Correct")
        sleep(2)
    else: 
        problem_solved = False

    return problem_solved, response

def show_clue(response, clue, clues):
    if response == "?":
        if clue < 4:
            console.print(f"[bold red]{clues[clue]}[/bold red]")
            console.print("[bold red]-1 minute[/bold red]")
            clue += 1
        else: 
            console.print("[bold red]No more clues[/bold red]")
            console.print("[bold red]-1 minute[/bold red]")
    return clue

class Countdonw_Threade:
    def __init__(self):
        self._thread = None

    def countdown(self, seconds):
        time.sleep(seconds)
        print("\nCountdown finished!")

    def run_in_thread(self, func, *args):
        """
        Run the given function in a separate thread.
        
        :param func: Function to be executed in a thread.
        :param args: Arguments to pass to the function.
        """
        self._thread = threading.Thread(target=func, args=args)
        self._thread.start()

    def wait_for_completion(self):
        """Wait for the thread to complete."""
        if self._thread:
            self._thread.join()

    def execute(self):
        # Start the countdown in a separate thread
        self.run_in_thread(self.countdown, 10)

        # Foreground tasks
        for i in range(1, 6):
            print(f"Foreground task: {i}")
            time.sleep(1)

        # Wait for the countdown thread to finish
        self.wait_for_completion()


class Cicada_13:
    def __init__(self) -> None:
        pass

    def game_loop(self, clear_screen):

        game_finished = False
        next_game = False

        while game_finished != True:
            
            clear_screen()

            self.game_rules(clear_screen=clear_screen, next_game=next_game)
            clear_screen()
            self.leval_1()
            clear_screen()
            self.leval_2()
            clear_screen()
            self.leval_3()
            clear_screen()
            self.leval_4()
            clear_screen()
            # self.leval_5()
            # clear_screen()
            # self.leval_6()
            # clear_screen()
            # self.leval_7()
            # clear_screen()
            # self.leval_8()
            # clear_screen()
            # self.leval_9()
            # clear_screen()
            # self.leval_10()
            # clear_screen()
            # self.leval_11()
            # clear_screen()
            # self.leval_12()
            # self.leval_13()
            # clear_screen()
            # endscreen
            game_finished = False

    def game_rules(self, clear_screen, next_game):
        while next_game == False:
            clear_screen()
            console.print("[bold red]Game Rules[/bold red]")
            console.print("- Each team starts with 130 minutes on their clock")
            console.print("- If you get stuck, each leval has 3 clues and each clue costas 1 minute time reduction")
            console.print("- Every 5 min each player has to drink 5cl of beer")
            console.print(Panel("[bold cyan]- The team with the most time left in the end wins[/bold cyan]"))

            console.print("\n[bold red]Game Commands[/bold red]")
            console.print("Type the anserw to the challange, or desired game command and hit enter")
            console.print("[[bold red]?[/bold red]] = Clue to current challenge")
            console.print("[[bold red]y[/bold red]] = Yes")
            console.print("[[bold red]n[/bold red]] = No")

            response = input("> ")
            if response == "n":
                clear_screen()
                console.print("If you have questions ask the gmae host")
                console.print("[[bold red]1[/bold red]] = Start Game")
                console.print("[[bold red]2[/bold red]] = See menu again")
                response = input("> ")
                if response == "1":
                    next_game = True
                if response == "2":
                    pass

            if response == "?":
                clear_screen()
                console.print("[bold red]This leval has no clues[/bold red]")
                console.print("[[bold red]1[/bold red]] = Start Game")
                console.print("[[bold red]2[/bold red]] = See menu again")
                response = input("> ")
                if response == "1":
                    next_game = True
                if response == "2":
                    pass

            if response == "y":
                next_game = True
         
    # ----------------------------------------------------------------
    def leval_1(self):
        # Prime facotor a number and user the secons smallest prime as key to solv a Cecar cipher
        # the responce of the scifer is a url that lead to next challange.
        clue = 1
        clues = {
            1: "This is a Caesar Cipher, and it is one of the earliest and simplest methods of encryption technique",
            2: "A Caesar Cipher is a type of substitution cipher",
            3: "Each letter of a given text is replaced by a \nletter with a fixed number of positions down the alphabet",
        }

        problem_solved = False
        console.print("[bold cyan]Challenge 1: The Cipher[/bold cyan]\n")
        console.print("[bold red]Cipher key = [/bold red]Second smallest factor to 231")
        console.print(Panel("[bold cyan]ITLM MXGLX[/bold cyan]"))

        while problem_solved == False:
            problem_solved, response = answer("PAST TENSE", "str")
            clue = show_clue(response, clue, clues)
            if response == "PAST TENSE":
                """Open the specified URL in the default web browser."""
                url = "https://cicada-game.netlify.app/pastXse"
                webbrowser.open(url)

    # ----------------------------------------------------------------
    def leval_2(self):
    # message On this screen are four numbers, find them.
    # four in the clue message, 
    # 5 as the greek letter (V), 
    # 10 the url as letters (X), 
    # 8 as a hidden in the visual as a woman that just (eight) dinner.
    # Sum up the numbers to get 27
        problem_solved = False
        clue = 1    
        clues = {
            1: "text",
            2: "two words two numerals",
            3: "What did she just do that left an empty plate behinde?",
        }

        print('Challenge 2: Steganographic Clue Hunt\n')
        print("What is the sum of all four integers you found")


        while problem_solved == False:
            problem_solved, response = answer(27, "int")
            clue = show_clue(response, clue, clues)
    
    # ----------------------------------------------------------------
    def leval_3(self):
        problem_solved = False
        print('Challenge 3: Logic Lock\n')
        console.print("[bold red]Find the key to move on[/bold red]")

        while problem_solved == False:
            # 1. Splt the numer right down the middle (2, 7)
            console.print("[bold red]Logic 1[/bold red] \nSplit the number right down the middle")
            # 2. Write the two numbers in 4bit binary (2=0010, 7=0111)
            console.print("[bold red]Logic 2[/bold red] \nWrite the two numbers in 4bit binary")
            # 3. what is the sum of (4)
            console.print("[bold red]Logic 3[/bold red] \nWhat is the squareroot of the sum of all bits")
            # 
            console.print("[bold red]Riddle = [/bold red]next key is hidden in the cube")
            problem_solved = answer(2, "int")

    # ----------------------------------------------------------------
    def leval_4(self):
        # Riddle = I am hidden in a cube of x. x^3 = 8
        # Crack another Cecar cipher with 8 as key
        # Answer = Vigenère. 
        # Button (Who am I) that only triggers a google searsh if the write message is decrypted.       
        problem_solved = False
        while problem_solved == False:
            print('Challenge 4: The Enigmatic Code')


            vigenere_table = pd.read_csv("vigenere_table.csv")
            print("\n\n")
            print(vigenere_table)
            print("\n\n")
            problem_solved = answer("vigenère", "str")


    def leval_5(self):
        pass

    def leval_6(self):
        pass
    def leval_7(self):
        pass
    def leval_8(self):
        pass
    def leval_9(self):
        pass
    def leval_10(self):
        pass
    def leval_11(self):
        pass
    def leval_12(self):
        pass
    def leval_13(self):
        pass


    # ---------------

        # Challenge 5: The Techno-Riddle

        # Challenge 6: The Virtual Maze
        # Challenge 7: The Multilayered Puzzle
        # Challenge 8: The Decoding Relay
        # Challenge 9: The Riddle of Reflection
        # Challenge 10: The Collaborative Cipher Wheel
        # Challenge 11: The Binary Quest
        # Challenge 12: The Puzzle Marathon
        # Challenge 13: The Grand Convergence

            