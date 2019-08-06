"""
Learn about scoping in Python
Python order L-local, E-enclosing, G-global, B-built in > else error
"""

# define a global variable
count = 0 # global object


def show_count(): # create a new function to display the current count
    """
    Display the current count
    :return: nothing
    """
    print(count)


def set_count(num): #2
    """
    Set global counter to input
    :param num: input number
    :return: nothing
    """

    global count # (25)
    count = num # = sign created a new object count. is not reflected to the global variable it goes out of scope first.
    # the global level you must use keyword global


def main():
    """
    Test function
    :return: 
    """
    show_count()
    set_count(9) #2
    show_count() #2


if __name__ == '__main__':
    main()
    exit(0)

    """ PC: 
    import scope 
    type(scope) # tells you what type scope is 
    <class 'module'> # everything is an object in Python 
    dir(scope) # give directory of attributes for this particular class 
    ['__builtins__', '__cached__', '__doc__', '__...
    scope.set_coun.__doc__ # tells you the documentation in raw plain text (no formatting)
    help(scope.set_coun.__doc__) # easier to read view 
    ## even your files are classes, inherited from a base class 
    
    
    """