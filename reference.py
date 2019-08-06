"""
Learn about references and how they work
"""


def modify(k):  # define a new function that takes one parameter
    """
    Modify the content of the list
    :param k: input list
    :return: nothing
    """
    # lists are passed by reference - so i can modify external objects inside my function
    k.append(39) # changing the list inside the function
    print("k =", k)
    # Python is handling k by default is always reference


def replace(g):
    """
    Replace input list
    :param g: input list
    :return: nothing
    """
    g = [17, 48, 89] # overrides the original - replace(g)
    print("g = ", g)


def main():
    """
    test function
    :return: nothing
    """

    m = [9, 15, 24]  # create a small list to practice modifications on
    print("before modify() m =", m)
    modify(m)
    print("after modify() m = ", m)
    replace(m)
    print("after replace() m =", m)


if __name__ == '__main__':
    main()
    exit(0)