"""
Learn about range() Collection
"""


def main():
    """
    Test function
    :return: 
    """
    for i in range(5): # default to run : even if declared does not execute until you run it
        print(i)
# if you want to set initial value start at 5 got to 10; remember it does not include the 10 because it starts at 0
    print("Now setting initial value")
    for i in range(5, 10):
        print(i)

# can create a counter, create a list of those 5-9, can create a list outside and append, or just create a list on the
# fly with the list constructor: supports concatenation
    l = list(range(5, 10))
    print(l, type(l)) # print the list and display the type -> [5, 6, 7, 8, 9] <class 'list'>
    l2 = list(range(5, 10)) + list(range(30, 40))
    print(l2, type(l2))
    # ->[5, 6, 7, 8, 9, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39] <class 'list'
# what if you want to increment by more than one at a time " Step argument" (begin, stop, increment)
    l3 = (range(0, 20, 2))
    print(l3, type(l3))
    # ->range(0, 20, 2) <class 'range'>

# lets say we have a list
    s = [0, 2, 3, 4, 6]
# could iterate over list using index notation
    for i in range(len(s)):
        print(s[i]) # c++ style
# Better way - Python clear syntax
    for v in s:
        print(v)

# lets say we need to know the index and value at any given time: "Enumerator(): returns a iterable series"
    t = [6, 789, 123, 98, 3, 22]
    for p in enumerate(t):
        print(p) # -> (0, 6)\n (1, 789)\n...
        # could do print(p, p[0], p[1])
# try to unpack it on the fly, have your two values ready to go
    for i, v in enumerate(t):
        print("i = {}, v = {}".format(i, v) # great to keep track of your index


if __name__ == '__main__':
    main()
    exit(0)



    """
    PC: range(5) -> range(0, 5) :: iterated until we reach 5
        """