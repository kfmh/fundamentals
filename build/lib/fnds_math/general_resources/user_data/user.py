import os
import csv
import pandas as pd

class User:
    def __init__(self, username):
        self.username = username
        self.filename = f"{self.username}.csv"
        
        # Check if the CSV file exists
        script_directory = os.path.dirname(os.path.abspath(__file__))
        self.csv_path = os.path.join(script_directory, f"{self.username}.csv")

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