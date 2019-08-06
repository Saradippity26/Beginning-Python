"""
Template creation: File -> settings -> search template -> Python script
"""
"""
Learn about return semantics and function arguments in Python
"""

import time

def egg(var):
    """
    Dummy function with one variable: Returns the variable back to the user
    :param var: input object
    :return: input object
    """
    return var


def sum_two(num1, num2 = 8): # first example was done with def sum_two(num1, num2):
    """
    Sum two input integer objects # tailored by adding integer
    :param num1: object 1
    :param num2: object 2 (if optional parameter you must provide a value (num2 = 8) must document default is  = 8
    :return: sum of objects
    required parameters must come first, optional parameters after required parameters
    """
    total = num1 + num2
    print(num1, " + ", num2, " = ", total)

    return num1 + num2


def banner(message, border='*'): # need to figure out a way to dynamically determine the size of the border
    """banner is the name of the function, message is a parameter, border is a defined parameter
    Hint PC: s = "weber" + "state" -> 'weberstate' -> s *3 -> 'weberstateweberstateweberstate'
     a string will support multiplication -- need length of the string  - use three print statements
    Print message in banner form
    :param message: string to print
    :param border: border character for the string
    :return: nothing
    """
    print(border *len(message))
    print(message)
    print(border * len(message))


def add_spam(menu=[]): # challenge 3 =[] guarantees it goes into a list
    """
    add spam to the menu list
    :param menu:
    :return: menu list
    """
    if menu is None: # ch 4
        menu = []   # ch4
    menu.append('spam')
    return menu


"""  PC: from return_semantics import add_spam
>>> (no error good)
add_spam
['spam']
will add one each time you call (twice ['spam', 'spam'])
-- Challenge 4 How to test if the pointer is pointing to the correct place. use null (means free) Python uses none instead of null
def add_spam(menu=None): # default to test again 
Challenge 5: PC: def add(n1, n2):
...     return n1 + n2
>>> add (2, 5)
7
>>> works with floating points, strings, and lists as long as they are the same  type 
"""


def main():
    """
    Test function
    :return:
    """

    c = [6, 10, 20]
    e = egg(c)
    print(c is e) # do you think c and e are the same?  yes, passing by reference and returning the same reference
    # c and e are both pointing at the same list
    # when you have optional parameters you should have a default parameter (ex. print() has a bunch of defaults)
    # PC: help(print): print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    # not have a new line: print("same line", end=' ')

    n1 = 3
    n2 = 9
    # EX:  print(n1, " + ", n2, " = ", sum_two(n1, n2)) # passing two objects (not really numbers)
    # try this function with two lists, strings, dictionaries:  works as long as the two objects are the same
    sum_two(n1, n2)
    sum_two(n1)

    banner("Weber State")
    banner("Weber State University", "$") # , separates the strings: there is a space default after ,
    # \ is used to separate code to another line over 80 characters

    breakfast = ['eggs', 'bacon'] # challenge 3
    print("Before", breakfast)
    add_spam(breakfast)
    print("After", breakfast)
#    print("only one input", sum_two(n1)) # keep track of the required parameters by name

"""Challenge 3 with input parameters: (8) import time: get current system time: time.ctime()
# PC: def show_time(t - time.ctime()):
# ...  print(t) # press enter twice to exit to get back to prompt >>>
# call the function: show_time()
# Tue Aug 6 13:39:09 2019  the arguments are being evaluated the first time it is called, does not update: if you 
# call it again it will display the same time Tue Aug 6 13:39:09 2019
# how to fix:  add new function 
def add_spam(menu):
    ---add spam to menu list
    :param menu:
    :return menu list---
    menu.append('spam') # adding items to a list (append)
    return(menu)
"""


if __name__ == '__main__':
    main()
    exit(0)

# task: define def banner(message, border = ' * ')
# xxxxxxxxxxxxxxxxxxxxxx
# Weber State University
# xxxxxxxxxxxxxxxxxxxxxx