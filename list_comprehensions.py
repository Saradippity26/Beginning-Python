"""
List comprehensions:
Readable, expressive, and effective
"""
from math import factorial, sqrt
from pprint import pprint as pp


def is_prime(num):
    """
    Should return true if prime false if not
    :param num: number to testg
    :return: true for prime number false for non prime numbers
    """
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0: # testing for all possibilities
            return False

    return True

    # what if i want to calculate a list of all prime numbers in the range 0-100. Use a function to filter
    # works well with boolean functions




def main():
    """
    Test function
    :return: 
    """
    # list comprehensions will give you a shorthand of all of this code
    words = "Today I am very happy to learn about list comprehensions".split()
    print(words) # -> ['Today', 'I', 'am', 'very', 'happy', 'to', 'learn', 'about', 'list', 'comprehensions']
    data = [] # empty list

    for word in words: # some analysis
        print(word) # accesses individual element of the list -> Today \n I \n am...
        data.append(word)

        # Filter data
        print(data)

    # Task find the length of the first 20 factorial numbers : need to import math library and factorial\
    info = [] # empty list
    for x in range(20):
        # print(factorial(x))
        # now create an array that contains the length of each of the factorials (len works on collections not int)
        # need to cast as a string then len
        # info.append(len(str(factorial(x))))
        pp(info)

    # how to use a comprehension instead: [] for list comprehensions
    info2 = [len(str(factorial(x))) for x in range(20)]
    pp(info2)

    # Set comprehensions: {}
    info3 = {len(str(factorial(x))) for x in range(20)}
    pp(info3)

    # Dictionary Comprehensions: {}
    nba_teams = {'Jazz': 'SLC', 'Warriors': 'OAKLAND', 'Lakers': 'LA', 'Clippers': 'LA'}
    pp(nba_teams)
    teams_nba = {city:mascot for mascot, city in nba_teams.items()}
    pp(teams_nba)

    # nba_teams = {'Jazz:SLC', 'Warriors:OAKLAND', 'Lakers:LA', 'Clippers:"LA'}
    # pp(nba_teams)
    # team_nba = {city: mascot for mascot, city in nba_teams.items()}
    # pp(team_nba) # key must be unique LA is a duplicate so not a unique key

    # Filter predicates:

    primes = [x for x in range(101) if is_prime(x)]
    print(len(primes), primes)


if __name__ == '__main__':
    main()
    exit(0)