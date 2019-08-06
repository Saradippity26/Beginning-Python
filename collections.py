"""
To learn about collections: tuples, strings, range, list, dictionaries, and sets
 Tuple : constant fixed list cannot change it : heterogeneous immutable sequence
    access members by [] : define by ()
    List : access [] by index : define []
    dict : [] by key : define {}
    str : "" define, access [] index
    tuple : define () ; [] access index
"""


def do_tuples():
    """
    practice tuples ; Immutable sequence of arbitrary objects
    :return: nothing
    """
    # use () to define a tuple
    t = ("Ogden", 1.99, 2)
    print(t, type(t))
    print("Size", len(t))
    print("One member", t[0]) # by index notation []
    # to iterate over a tuple
    for item in t:
        print(item)

    # single tuples, must end with a comma
    t1 = (6,) # finish with a comma to ensure it is a tuple
    print(t1, type(t1))  # t1 = (6) causes an error 6 <class 'int'> will work if you finish with a comma

    # Another way to create a tuple: Parenthesis are optional
    t2 = 1, 2, 3, 5
    print(t2, type(t2)) # will assume you want a tuple, will return all objects the same
    # use in a function : def min_max():


def min_max(items):
    """
    return the min and max elements of a collection
    :param items: collection
    :return: the min and max
    """

    # use built in functions for min and max
    return min(items), max(items)


def main():
    """
    Test function
    :return: 
    """

    # do_tuples()
    output = min_max([56, 76, 11, 12, 90])
    print("min", output[0]) # this way you have to remember the index
    print("max", output[1])

# tuple unpacking - will split on the fly
    lower, upper = min_max([56, 76, 11, 12, 90])
    print("min", lower)
    print("max", upper)


""" Challenge 1: Create a functions that will swap two values - keep in mind tuples how would that work?
    #swap values 
    a = "jelly"
    b = "bean"
    print(a,b)
    # call your function
    print(a,b)
    a, b = swap(a, b)
    # a, b = b, a alternative line 71 and 72 are the same 
    
    def swap(obj1, obj2):
    --- swap value of the objects 
    :param obj1: first
    :param obj2: second 
    :return: values swapped 
    ---
    return obj2, obj1
"""

if __name__ == '__main__':
    main()
    exit(0)