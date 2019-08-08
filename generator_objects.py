"""
Generator objects are a cross between comprehensions and generator functions
syntax: similar to a list comprehension, but with parenthesis ()
    (expression(item) for item in iterable)
"""
# calculate a list of the first one million squares numbers : can use range

from list_comprehensions import is_prime


def main():
    """
    Test function
    :return: 
    """
    m_squares = (x*x for x in range(1, 1000001)) # list with first one million square numbers
    print(m_squares, type(m_squares))
    # -> <generator object main.<locals>.<genexpr> at 0x0000018268C39518> <class 'generator'>
    # sum: sum all items of a collections
    print('The sum of the first million numbers is:', sum(m_squares))
    # -> The sum of the first million numbers is: 333333833333500000
    # or do all in one line
    print('The sum of the first million numbers is:', sum(x*x for x in range(1, 1000001)))
    # -> The sum of the first million numbers is: 333333833333500000

    # is_prime is in list_comprehensions lets call it so we can use it here, how to import
    # from list_comprehensions import is_prime

    # the sum of the prime numbers between 1 to 10K : we are using is_prime as a filter
    print('The sum of the prime numbers from 1 to 10K is:', sum(x for x in range(1, 10001) if is_prime(x)))
    # -> The sum of the prime numbers from 1 to 10K is: 5736396


if __name__ == '__main__':
    main()
    exit(0)