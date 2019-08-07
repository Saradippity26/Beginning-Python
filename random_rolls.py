"""
Simulate 6000 rolls of a dice  (1-6 sides to the die)
"""

    # Google: How do you randomize a number in Python: this case between one and six
    # Generate a random number: include library : import random

import random
import statistics

# create a function


def roll_die(num):
    """
    random roll of a dice
    :param num: number of rolls
    :return: a list of frequencies
    Index 0 maps to 1
    Index 1 maps to 2 ....
    """
    freq = [0] * 6  # initial values to zero
    for roll in range(num):
        n = random.randrange(1, 7)
        freq[n - 1] += 1 # need to check if the value exists, if not then append
# print(random.randrange(1, 7)) - used in an example but changed code

    return freq

    # how to calculate the mean (avg): import statistics -- remember to import statistics then help(statistics) for PC.


def main():
    """
    Test function
    :return: 
    """
    num = int(input(" Enter how many times you need to roll")) # -> Enter 6000 -> [978, 1011, 1012, 973, 1024, 1002]
    result = roll_die(num)
    for roll, total in enumerate(result):
        print("Total rolls of {} = {}".format(roll + 1, total))

    print("average = {}".format(sum(result)/len(result)))
    print("mean = {}".format(statistics.mean(result)))
    print("average = {}".format(statistics.median(result)))


if __name__ == '__main__':
    main()
    exit(0)