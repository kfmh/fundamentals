import threading
import time
from rich.console import Console
from rich.panel import Panel
import webbrowser

console = Console(force_terminal=True)

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

        challenge = 0
        game_finished = False
        next_game = False

        while game_finished != True:
            
            clear_screen()

            if challenge == 0:
                self.game_rules(clear_screen=clear_screen, next_game=next_game)
            if challenge == 1:
                self.leval_1()
            
            challenge += 1

    def game_rules(self, clear_screen, next_game):
        while next_game == False:
            clear_screen()
            console.print("[bold red]Game Rules[/bold red]")
            console.print("- Each team starts with 130 points")
            console.print("- Every minute 1 point is deducted")
            console.print("- If you get stuck, each leval has 3 clues and each clue costas 1 point")
            console.print("- Each clue costs 1 point")
            console.print("- Every 5 min each player has to drink 5cl of beer")
            console.print(Panel("[bold cyan]- The team with the most points left in the end wins[/bold cyan]"))

            console.print("\n[bold red]Game Controls[/bold red]")
            console.print("Type the anserw to the challange, or desired game control and hit enter")
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

            
    

    # Prime facotor a number and user the secons smallest prime as key to solv a Cecar cipher
    # the responce of the scifer is a url that lead to next challange.
    def leval_1(self):
        console.print("[bold cyan]Challenge 1: The Cipher Key[/bold cyan]\n")
        console.print("[bold red]Cipher key:[/bold red] \nSecond smallest prime that is a divisor to 231")
        console.print(Panel("[bold cyan]Cipher text[/bold cyan]"))
        

        decrypted_cipher = input("> ")
        if decrypted_cipher == "test":
            """Open the specified URL in the default web browser."""
            url = "https://undrwolf.com/"
            webbrowser.open(url)

    def leval_2(self):
        print('Challenge 2: Steganographic Clue Hunt')
        # message On this screen are 4 numbers, find them.
        # 4 in the clue message, 
        # 5 as the greek letter (V), 
        # 10 the url as letters (ten), 
        # 8 as a hidden in the visual as a woman tha just (eight) dinner.
        # Sum up the numbers to get 27
    
    def leval_3(self):
        print('Challenge 3: Logic Lock')
        # 1. Slipt the numer right down the middle (2, 7)
        # 2. Write the two numbers in 4bit binary (2=0010, 7=0111)
        # 3. what is the sum of 

    def leval_4(self):
        print('Challenge 4: The Enigmatic Code')
        # Riddle = I am hidden in a cube of x. x^3 = 8
        # Crack another Cecar cipher with 8 as key
        # Answer = Vigenère. 
        # Button (Who am I) that only triggers a google searsh if the write message is decrypted.       

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

            