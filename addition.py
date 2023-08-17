import random
import os
from rich import print as p
from rich.console import Console
from rich.traceback import install
install()
from time import sleep

def random_ab_int():
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


response = "run"
score = 0
while response != "quit":
    numbers_dict, correct = random_ab_int()
#   answers = list(numbers_dict.keys())
#   random.shuffle(answers)
#   answers_dict = {'a': answers[0], 'b': answers[1], 'c': answers[2], 'd': answers[3]}
#   correct_numbers = numbers_dict[correct]

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
