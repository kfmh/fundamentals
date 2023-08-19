import os
from rich import print as p
from rich.traceback import install
from time import sleep
import random

def random_a_b_int():
    answers_list = {}
    while len(answers_list) < 4:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        sum = a + b
        if sum not in answers_list.keys():
            if len(answers_list) == 0:
                correct = sum
            answers_list[sum] = [a, b]

    return answers_list, correct
def main():
    response = "run"
    score = 0
    while response != "quit":
        numbers_dict, correct = random_a_b_int()

        os.system('clear')
        p(f"score = {score}\n\
        What is the sum of \n\
        {numbers_dict[correct][0]}\
        + {numbers_dict[correct][1]}\n\n\
        quit = quit")

        response = input()
        if response == "quit":
            os.system('clear')
            p(f"Your score is {score}")
            break
        #if answers_dict[response] == correct:
        if int(response) == correct:
            os.system('clear')
            p('correct')
            score += 1
        else:
            os.system('clear')
            p('try again')
        sleep(1)

if __name__ == "__main__":
    main()