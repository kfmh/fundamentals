import threading
import time
from rich.console import Console
from rich.panel import Panel
import webbrowser
from time import sleep
import pandas as pd
from tabulate import tabulate
import fnds_functionality

console = Console(force_terminal=True)
manager = fnds_functionality.ScreenManager()


def player_input(correct_response, response_type, clue, clues, input_text="Enter Command: "):
    response = input(input_text)
    cr = correct_response

    if response in ["x", "?", "y", "n"]:
        clue = show_clue(response, clue, clues)
    elif response != "?":
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

    return problem_solved, response, clue

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

    def game_loop(self):

        game_finished = False
        next_game = False

        while game_finished != True:
            
            manager.clear_screen()

            self.game_rules(next_game=next_game)
            # manager.clear_screen()
            # last_challange = self.leval_1()
            # manager.clear_screen()
            # last_challange = self.leval_2(last_challange)
            # manager.clear_screen()
            # last_challange = self.leval_3(last_challange)
            manager.clear_screen()
            self.leval_4(2)
            manager.clear_screen()
            # self.leval_5()
            # manager.clear_screen()
            # self.leval_6()
            # manager.clear_screen()
            # self.leval_7()
            # manager.clear_screen()
            # self.leval_8()
            # manager.clear_screen()
            # self.leval_9()
            # manager.clear_screen()
            # self.leval_10()
            # manager.clear_screen()
            # self.leval_11()
            # manager.clear_screen()
            # self.leval_12()
            # self.leval_13()
            # manager.clear_screen()
            # endscreen
            game_finished = False

    def game_rules(self, next_game):
        while next_game == False:
            manager.clear_screen()
            console.print("[bold red]Game Rules[/bold red]")
            console.print("- Each team starts with 130 minutes on their clock")
            console.print("- If you get stuck, each leval has 3 clues and each clue costas 1 minute time reduction")
            console.print("- Every 5 min each player has to drink 5cl of beer")
            console.print(Panel("[bold cyan]- The team with the most time left in the end wins[/bold cyan]"))

            console.print("\n[bold red]Game Commands[/bold red]")
            console.print("Type the anserw to the challange, or desired game command and hit enter")
            console.print("[[bold red]?[/bold red]] = Clue to current challenge")
            console.print("[[bold red]x[/bold red]] = Restart challenge")
            console.print("[[bold red]y[/bold red]] = Yes")
            console.print("[[bold red]n[/bold red]] = No")

            response = input("> ")
            if response == "n":
                manager.clear_screen()
                console.print("If you have questions ask the gmae host")
                console.print("[[bold red]1[/bold red]] = Start Game")
                console.print("[[bold red]2[/bold red]] = See menu again")
                response = input("> ")
                if response == "1":
                    next_game = True
                if response == "2":
                    pass

            if response == "?":
                manager.clear_screen()
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
            problem_solved, response = player_input("PAST TENSE", "str")
            clue = show_clue(response, clue, clues)
            if response == "PAST TENSE":
                """Open the specified URL in the default web browser."""
                url = "https://cicada-game.netlify.app/womanfinishedeating"
                webbrowser.open(url)
                return response

    # ----------------------------------------------------------------
    def leval_2(self, last_challange):
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
            2: "two words, two numerals",
            3: "What activity did she partake in that gave the result of an empty plate?",
        }

        print(f'Last challenge: {last_challange}\n')
        console.print(f'Challenge 2: Steganographic\n')
        print("What is the sum of all four integers you found")


        while problem_solved == False:
            problem_solved, response = player_input(27, "int")
            clue = show_clue(response, clue, clues)
            if problem_solved:
                return response
    
    # ----------------------------------------------------------------
    def leval_3(self, last_challange):
        clues = {
            1: "Use a literal interpretation",
            2: "When all 4bits are ON  (1 1 1 1 = 2^3 + 2^2 + 2^1 + 2^0)\nWhen all 4bits are OFF (0 0 0 0 = 0 + 0 + 0 + 0",
            3: "Hamming weights are the number of bits that are turned ON in a binary string",
        }

        problem_solved = False

        while problem_solved == False:
            manager.clear_screen()
            print(f'Last challenge: {last_challange} -- Commands: [?]=Clue, [x]=Restart challenge\n')
            console.print("Challenge 3: Logic Lock [bold red]Find the key to move on[/bold red]\n")

            # 1. Splt the numer right down the middle (2, 7)
            console.print(f"[bold red]Logic 1[/bold red] \nSplit {last_challange} right down the middle, what two values do you get")

            v1, v2 = None, None
            commands = ["x", "?", "y", "n"]
            while v1 == None or v1 in commands:
                xx, v1 = player_input("xx", "int", 1, clues, "value1: ")
            while v2 == None or v2 in commands:
                xx, v2 = player_input("xx", "int", 1, clues, "value2: ")

            # 2. Write the two numbers in 4bit binary (2=0010, 7=0111)
            console.print(f"\n[bold red]Logic 2[/bold red] \nWrite {v1} and {v2} respectively in 4bit binary")
            binary1, binary2 = None, None
            while binary1 == None or binary1 in commands:
                xx, binary1 = player_input("xx", "str", 2, clues, f"{v1} = ")
            while binary2 == None or binary2 in commands:
                xx, binary2 = player_input("xx", "str", 2, clues, f"{v2} = ")

            # 3. what is the sum of (4)
            console.print(f"\n[bold red]Logic 3[/bold red] \nAdd up the Hamming weights of {binary1} and {binary2}, and then devide the sum by its square root")

            response = None
            while response == None or response in commands:
                problem_solved, response = player_input(2, "int", 3, clues, "Answer: ")

            if problem_solved:
                return response
            else:
                console.print(f"\n[bold red]-----------INCORRECT TRY AGAIN-----------[/bold red]")
                sleep(1.5)


    # ----------------------------------------------------------------
    def leval_4(self, last_challange):
        # Riddle = Find a key, locked in a cube, say my name 
        # Crack another Cecar cipher with 8 as key
        # player_input = Vigenère. 
        # Button (Who am I) that only triggers a google searsh if the write message is decrypted. ß
        print(f'Last challenge: {last_challange} -- Commands: [?]=Clue, [x]=Restart challenge\n')
        print('Challenge 4: Rail Fence Cipher')
        console.print(Panel("[bold cyan]VGNR IEEE[/bold cyan]"))

        clue = 1    
        problem_solved = False

        while problem_solved == False:
            clues = {
                1: "Rail Fence Cipher is an encryption method zig-zaging letters between rails",
                2: "The key to a Rail Fence Cipher is the number of rails you need to use",
                3: "|Alternate letters| with 3 rails \n|-A-------R-------E-------T-------|\n|---L---E---N---T---L---T---E---S-|\n|-----T-------A-------E-------R---|\nARET LENTLTES TAER",
            }

            problem_solved, response, clue = player_input("vigenere", "str", clue, clues)
            if problem_solved:
                return response


    def leval_5(self, last_challange):
        print(f'Last challenge: {last_challange} -- Commands: [?]=Clue, [x]=Restart challenge\n')
        print('Challenge 5: ')

        while problem_solved == False:


            vigenere_table = pd.read_csv("vigenere_table.csv")
            print("\n\n")
            print(vigenere_table)
            print("\n\n")
            problem_solved = player_input("vigenère", "str")

            # Return riddle

    def leval_6(self):
        # solvation to riddle = "bockshelf"
        pass
    def leval_7(self):
        # solv math problem to get cordinats in booksshelf, to find envelope
        pass
    def leval_8(self):
        # In envelope is USB, decrupt password to open usb
        pass
    def leval_9(self):
        # in usb run program and crash program to get [row, colmn] in bookshelf to find phone
        pass
    def leval_10(self):
        # passcode to phone is product of coordinats for usb and phone shelf
        pass
    def leval_11(self):
        # find map inside phone
        pass
    def leval_12(self):
        # find document in garden
        pass
    def leval_13(self):
        # Solv dokument
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

            