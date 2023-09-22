from collections import deque
import pandas as pd
import time
import os
import csv


class User:
    def __init__(self, username):
        self.username = username
        self.filename = f"{self.username}.csv"
        
        # Check if the CSV file exists
        script_directory = os.path.dirname(os.path.abspath(__file__))
        self.csv_path = os.path.join(script_directory, f"user_data/{self.username}.csv")

        if not os.path.exists(self.csv_path):
            # Create the CSV file with headers if it doesn't exist
            with open(self.csv_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['response_stime', 'correct'])

        self.csv = pd.read_csv(self.csv_path)

    def append_to_csv(self, response_stime, correct):
        with open(self.csv_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([response_stime, correct])
    
    def score_count(self):
        """
        Returns:
        - Series: A pandas Series containing the counts of each unique value in the binary column.
        """
        # Using the value_counts() method on the specific column
        return self.csv['correct'].value_counts().iloc[1]

# Average Time To Answer 
class Avg_TTA:
    def __init__(self):
        self.start_time = None
        self.last_five = deque(maxlen=5)  # Will store the last 5 times.

    def start(self):
        """Starts the timer."""
        self.start_time = time.time()

    def stop(self):
        """Stops the timer and returns the elapsed time in seconds."""
        if self.start_time is None:
            raise ValueError("Timer hasn't started yet!")
        elapsed_time = time.time() - self.start_time
        self.last_five.append(elapsed_time)  # Add the time taken to the deque.
        self.start_time = None  # reset for the next start
        return elapsed_time

# Answer tracking
class AnswerTracker:
    def __init__(self):
        self.correct_count = 0
        self.wrong_count = 0

    def add_correct(self):
        """Increments the count of correct answers by 1."""
        self.correct_count += 1

    def add_wrong(self):
        """Increments the count of wrong answers by 1."""
        self.wrong_count += 1

# Clear screen function used when testingg terminal POC version
class ScreenManager:
    def __init__(self):
        pass

    @staticmethod
    def clear_screen():
        """Clears the terminal screen."""
        # Check if OS is POSIX compliant (e.g., Linux, macOS)
        if os.name == 'posix':
            print("\033c", end="")  # ANSI escape sequence to clear screen
        else:
            os.system('cls')  # Windows command to clear screen

class GameResponse:
    def __init__(self) -> None:
        pass

    @staticmethod
    def game_response(quit_command="q", special_command=None, sc_return=None):
        respone = input("> ")
        if respone == quit_command:
            return "quit"
        elif respone == special_command:
            return sc_return
        else: return respone