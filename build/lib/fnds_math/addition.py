import random
from .general_resources.fnds_functionality import *  # Importing the necessary modules and classes
from .general_resources.user_data.user import *

manager = ScreenManager()
gr = GameResponse()

# Clear screen on start
cs = manager.clear_screen()


class Addision_game:
    """
    Class for updating random integers a and b for addition questions.
    """
    def __init__(self):
        """
        Initializes the RandomABIntUpdater instance.
        """
        self.a = 0
        self.b = 0
        self.a_new = 0
        self.b_new = 0
    
    def update(self):
        """
        Updates the random integers a and b while ensuring they are not the same as before.
        
        Returns:
            tuple: A tuple containing the sum of the updated integers, the updated a, and the updated b.
        """
        while self.a_new == self.a and self.b_new == self.b:
            self.a_new = random.randint(1, 9)
            self.b_new = random.randint(1, 9)
            sum_result = self.a_new + self.b_new
        
        self.a, self.b = self.a_new, self.b_new
        
        return sum_result, self.a, self.b

    def display_question(self, console, score, a, b):
        """
        Displays the question to the user.
        
        Args:
            console (Console): Rich Console instance for printing formatted output.
            score (int): Current score of the user.
            a (int): First integer of the addition.
            b (int): Second integer of the addition.
        """
        console.print(f"Score: [bold magenta]{score}[/bold magenta]\n")
        console.print(f"What is the sum of\n\n[bold cyan]{a} + {b} = ?[/bold cyan]")
        console.print("\nType [bold red]q[/bold red] to quit.")
    
    def game_loop(self, score, Panel, console, user):
        response = "run"
        timer = Avg_TTA()
        tracker = AnswerTracker()
        user_data = User(user)
        while response != "q":
            manager.clear_screen()

            correct, a, b = self.update()

            self.display_question(console, score, a, b)
            timer.start()

            response = gr.game_response()

            if response == "quit":
                manager.clear_screen()
                console.print(Panel(f"Your final score is [bold red]{score}[/bold red]", expand=False))
                break

            try:
                user_response = int(response)
                elapsed_time = timer.stop()
                if user_response == correct:
                    correct_answer = 1
                    score += 1
                    tracker.add_correct()
                    console.print("[bold red]Correct! Well done![/bold red]\n")
                else:
                    correct_answer = 0
                    tracker.add_wrong()
                    console.print(f"[bold red]Oops! That's incorrect. \n{a} + {b} = {correct}[/bold red]\n")
                user_data.append_to_csv(elapsed_time, correct_answer)
                
            except ValueError:
                console.print("[bold yellow]Invalid input. Please enter a number or 'q' to quit.[/bold yellow]\n")

