import random

class RandomABIntUpdater:
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
