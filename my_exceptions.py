"""
Learn about exceptions:
Anytime an exception is raised the normal flow of the program is interrupted.
"""
import sys
# define a converts function that takes a string and coverts to an integer


def convert(s):
    """
    Converts a string to an integer
    :param s:
    :return:
    """
    # x = -1 # defined at beginning of function
    try:
        x = int(s)
        return int(s) # used in place of x = -1 to allow for better description
    except (ValueError, TypeError) as e:  # except ValueError: for one error
        print("Conversion error {}"\
             .format(str(e)), file=sys.stderr)

    return -1


def sqrt(x):
    """
    Compute the square root using the method of Heron of Alexandria
    :param x: Number to compute the sqrt
    :return: The sqrt of z
    """

    guess = x
    i = 0
    try:
        while guess*guess != x and i < 20:
            guess = (guess + x/guess)/2.0
            i += 1
    except ZeroDivisionError:
        raise ValueError()

    return guess


def main():
    """
    Test function
    :return: 

    print(convert(11))
    print(convert("hello")) # no rules to convert message -> ValueError: invalid literal for int() with base 10: 'hello'
    # with line 14 as x = int(s): changed to include try except block to return a -1 with an error
    print(convert([1, 4, 8])) # will cause type error cannot be a list
    # TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
    """

    try:
        print(sqrt(9))
        print(sqrt(11))
        print(sqrt(-1))
    except ValueError:
        print("Cannot commute the value of negative numbers")

    print("Done")

if __name__ == '__main__':
    main()
    exit(0)