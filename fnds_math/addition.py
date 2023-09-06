import random

class RandomABIntUpdater:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.a_new = 0
        self.b_new = 0
    
    def update(self):
        while self.a_new == self.a and self.b_new == self.b:
            self.a_new = random.randint(1, 9)
            self.b_new = random.randint(1, 9)
            sum_result = self.a_new + self.b_new
        
        self.a, self.b = self.a_new, self.b_new
        
        return sum_result, self.a, self.b
