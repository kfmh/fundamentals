import threading
import time
from rich.console import Console
from rich.panel import Panel
import webbrowser
from time import sleep
import pandas as pd
from general_resource.fnds_functionality import ScreenManager
import json
import os

# Get the directory containing the current script (doors.py)
script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to clues.json and gmae_menu.json in that directory
clues_path = os.path.join(script_directory, 'clues.json')
with open(clues_path, 'r') as infile:
    clues = json.load(infile)

game_menu_path = os.path.join(script_directory, 'game_menu.json')
with open(game_menu_path, 'r') as infile:
    game_menu = json.load(infile)


manager = ScreenManager()
console = Console(force_terminal=True)

def c_print(print_text):

    console.print(print_text)

def player_input(correct_response, response_type, clue, level, input_text="Enter Command: "):
    response = input(input_text)
    cr = correct_response

    if response in ["x", "?", "y", "n"]:
        clue = show_clue(response, clue, level)
    elif response != "?":
        if response_type == "int":
            response = int(response)
        if response_type == "str":
            response = str(response).upper()
            cr = correct_response.upper()

    if response == cr:
        problem_solved = True
        print("Correct")
        sleep(2)
    else: 
        problem_solved = False

    return problem_solved, response, clue

def show_clue(response, clue, level):
    clue_text = clues[level][clue]
    clue = int(clue)
    if response == "?":
        if clue < 4:
            console.print(f"[bold red]{clue_text}[/bold red]")
            console.print("[bold red]-1 minute[/bold red]")
            clue += 1
        else: 
            console.print("[bold red]No more clues[/bold red]")
            console.print("[bold red]-1 minute[/bold red]")
    return str(clue)

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
            manager.clear_screen()
            last_challange = self.level_1()
            manager.clear_screen()
            last_challange = self.level_2(last_challange)
            manager.clear_screen()
            last_challange = self.level_3(last_challange)
            manager.clear_screen()
            last_challange = self.level_4(last_challange)
            manager.clear_screen()
            last_challange = self.level_5(last_challange)
            manager.clear_screen()
            # last_challange = self.level_6(last_challange)
            # manager.clear_screen()
            # last_challange = self.level_7(last_challange)
            # manager.clear_screen()
            # last_challange = self.level_8(last_challange)
            # manager.clear_screen()
            # last_challange = self.level_9(last_challange)
            # manager.clear_screen()
            # last_challange = self.level_10(last_challange)
            # manager.clear_scre41jen()
            # last_challange = self.level_11(last_challange)
            # manager.clear_screen()
            # last_challange = self.level_12(last_challange)
            # self.level_13(last_challange)
            manager.clear_screen()
            # endscreen
            game_finished = False

    def game_rules(self, next_game):
        while next_game == False:
            manager.clear_screen()
            for i in game_menu["information"]:
                c_print(game_menu["information"][i])
                
            # console.print("[bold red]Game Rules[/bold red]")
            # console.print("- Each team starts with 130 minutes on their clock")
            # console.print("- If you get stuck, each level has 3 clues and each clue costas 1 minute time reduction")
            # console.print("- Every 5 min each player has to drink 5cl of beer")
            # console.print(Panel("[bold cyan]- The team with the most time left in the end wins[/bold cyan]"))

            # console.print("\n[bold red]Game Commands[/bold red]")
            # console.print("Type the anserw to the challange, or desired game command and hit enter")
            # console.print("[[bold red]?[/bold red]] = Clue to current challenge")
            # console.print("[[bold red]x[/bold red]] = Restart challenge")
            # console.print("[[bold red]y[/bold red]] = Yes")
            # console.print("[[bold red]n[/bold red]] = No")

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
                console.print("[bold red]This level has no clues[/bold red]")
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
    def level_1(self):
        # Prime facotor a number and user the secons smallest prime as key to solv a Cecar cipher
        # the responce of the scifer is a url that lead to next challange.
        clue, level = "1", "level_1"
        problem_solved = False

        console.print("[bold cyan]Challenge 1: The Cipher[/bold cyan]\n")
        console.print("[bold red]Cipher key = [/bold red]Second smallest factor to 231")
        console.print(Panel("[bold cyan]ITLM MXGLX[/bold cyan]"))

        while problem_solved == False:
            problem_solved, response, clue = player_input("PAST TENSE", "str", clue, level)
            clue = show_clue(response, clue, level)
            if response == "PAST TENSE":
                """Open the specified URL in the default web browser."""
                url = "https://cicada-game.netlify.app/womanfinishedeating"
                webbrowser.open(url)
                return response

    # ----------------------------------------------------------------
    def level_2(self, last_challange):
    # message On this screen are four numbers, find them.
    # four in the clue message, 
    # 5 as the greek letter (V), 
    # 10 the url as letters (X), 
    # 8 as a hidden in the visual as a woman that just (eight) dinner.
    # Sum up the numbers to get 27
        problem_solved = False
        clue, level = "1", "level_2"
        print(f'Last challenge: {last_challange}\n')
        console.print(f'Challenge 2: Steganographic\n')
        print("What is the sum of all four integers you found")


        while problem_solved == False:
            problem_solved, response, clue = player_input(27, "int", clue, level)
            clue = show_clue(response, clue, clues)
            if problem_solved:
                return response
    
    # ----------------------------------------------------------------
    def level_3(self, last_challange):     
        problem_solved = False
        clue, level = "1", "level_3"

        while problem_solved == False:
            manager.clear_screen()
            print(f'Last challenge: {last_challange} -- Commands: [?]=Clue, [x]=Restart challenge\n')
            console.print("Challenge 3: Logic Lock [bold red]Find the key to move on[/bold red]\n")

            # 1. Splt the numer right down the middle (2, 7)
            console.print(f"[bold red]Logic 1[/bold red] \nSplit {last_challange} right down the middle, what two values do you get")

            v1, v2 = None, None
            commands = ["x", "?", "y", "n"]
            while v1 == None or v1 in commands:
                _ , v1, zz = player_input("xx", "int", clue, level, "value1: ")
            while v2 == None or v2 in commands:
                _ , v2, zz = player_input("xx", "int", clue, level, "value2: ")

            # 2. Write the two numbers in 4bit binary (2=0010, 7=0111)
            console.print(f"\n[bold red]Logic 2[/bold red] \nWrite {v1} and {v2} respectively in 4bit binary")
            binary1, binary2 = None, None
            while binary1 == None or binary1 in commands:
                _, binary1, _   = player_input("xx", "str", "2", level, f"{v1} = ")

            while binary2 == None or binary2 in commands:
                _ , binary2, zz = player_input("xx", "str", "2", level, f"{v2} = ")

            # 3. what is the sum of (4)
            console.print(f"\n[bold red]Logic 3[/bold red] \nAdd up the Hamming weights of {binary1} and {binary2}, and then devide the sum by its square root")

            response = None
            while response == None or response in commands:
                problem_solved, response, clue = player_input(2, "int", 3, clues, "Answer: ")

            if problem_solved:
                return response
            else:
                console.print(f"\n[bold red]-----------INCORRECT TRY AGAIN-----------[/bold red]")
                sleep(1.5)


    # ----------------------------------------------------------------
    def level_4(self, last_challange):
        # Riddle = Find a key, locked in a cube, say my name 
        # Crack another Cecar cipher with 8 as key
        # player_input = Vigenère. 
        # Button (Who am I) that only triggers a google searsh if the write message is decrypted. ß
        print(f'Last challenge: {last_challange} -- Commands: [?]=Clue, [x]=Restart challenge\n')
        print('Challenge 4: Rail Fence Cipher')
        console.print(Panel("[bold cyan]VGNR IEEE[/bold cyan]"))

        clue, level = "1", "level_4"
        problem_solved = False

        while problem_solved == False:
            problem_solved, response, clue = player_input("vigenere", "str", clue, clues)
            if problem_solved:
                return response


    def level_5(self, last_challange):
        print(f'Last challenge: {last_challange} -- Commands: [?]=Clue, [x]=Restart challenge\n')
        print('Challenge 5: ')

        clue, level = 1, 1    
        while problem_solved == False:


            vigenere_table = pd.read_csv("vigenere_table.csv")
            print("\n\n")
            print(vigenere_table)
            print("\n\n")
            problem_solved, response, clue = player_input("vigenère", "str", clue, clues)

            # Return riddle

    # def level_6(self, last_challange):
        # solvation to riddle = "bookshelf"
    # def level_7(self, last_challange):
    #     # solv math problem to get cordinats in booksshelf, to find envelope
    #     pass
    # def level_8(self, last_challange):
    #     # In envelope is USB, decrupt password to open usb
    #     pass
    # def level_9(self, last_challange):
    #     # in usb run program and crash program to get [row, colmn] in bookshelf to find phone
    #     pass
    # def level_10(self, last_challange):
    #     # passcode to phone is product of coordinats for usb and phone shelf
    #     pass
    # def level_11(self, last_challange):
    #     # find map inside phone
    #     pass
    # def level_12(self, last_challange):
    #     # find document in garden
    #     pass
    # def level_13(self, last_challange):
    #     # Solv dokument with somehting that relefct all the previous challenges
    #     pass


    # ---------------
