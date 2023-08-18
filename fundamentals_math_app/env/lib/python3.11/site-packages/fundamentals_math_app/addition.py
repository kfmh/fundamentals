
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


