"""
When working with iterators, generators, etc.
Loot at the documentation for the itertools module: it is a built in module
"""
from itertools import islice, count, chain
from list_comprehensions import is_prime



def main():
    """
    Test function
    :return: 
    """
    # generate the first 1000 primes
    thousand_primes = islice((x for x in count() if  is_prime(x)), 1000)
    print(thousand_primes, type(thousand_primes))
    print("List of first 1K prime numbers:", list(thousand_primes))
    # what if we want to add them? wrap it all up with a sum, need to regenerate you data set
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print("Sum of first 1K prime numbers:", sum(thousand_primes))
    # other built-ine use with itertools: like any ("or"), or all ("and") : boolean statements T of F
    print(any([False, False, True])) # should get true back -> True: : can use to test for empty strings
    print(all([False, False, True])) # -> False

    # Lets say we have the range 1328, 1361 are there any prime numbers in this range?
    print("Are there prime numbers between 1328 and 1361?",
          any(is_prime(x) for x in range(1328, 1362))) # -> True : the is_prime is producing a list of booleans
    # if we used ( x for x in... it would produce a list of integers (warning: false positive any nonzero int is true
    # Print the prime numbers within that range
    print("Are there prime numbers between 1328 and 1361?",
          any(is_prime(x) for x in range(1328, 1362)), list(x for x in range(1328, 1362) if is_prime(x)))
    # -> Are there prime numbers between 1328 and 1361? True [1361]

    # Check if all names in the iterable are in title form: First letter capitalized
    names = ["London", "New York", "Ogden"] # all must be first letter CAPS
    print(all(name == name.title() for name in names)) # -> True
    names = ["London", "New York", "ogden"] # all must be first letter CAPS
    print(all(name == name.title() for name in names))  # -> False

    # Another built-in: zip():
    sunday  = [2, 2, 5, 7, 9, 10, 9, 6, 4, 4]
    monday  = [12, 14, 14, 15, 15, 16, 15, 13, 10, 9] # degrees in celsius
    tuesday = [13, 14, 15, 15, 16, 17, 16, 16, 12, 12]
    # lets iterate over data set: compare first M to first T without keeping track of the index
    for item in zip(monday, tuesday): # -> Prints as tuples
        print(item)
    # what was the average temp for each reading? Unpack the tuples
    for mon, tues in zip(monday, tuesday):
        print("average = ", (mon + tues/2))
        """ ->
        average =  18.5
        average =  21.0
        average =  21.5 ...
        """
        # calculate the min, max and avg of all points.
    for temps in zip(sunday, monday, tuesday):
               print("min = {:4.1f}", "max = {:4.1f}", "avg = {:4.1f}".format(
            min(temps), max(temps), sum(temps)/len(temps)))
        # {:indent 4(WIDTH OF FIELD)    . one floating point
        # what happens when your data set is not even. it stops when it does not have an even set to continue with
        # example: if we added wednesday = [2, 2] all of our sets would only report 2 values

    # Chain from itertools: combine all data sets
    all_temps = chain(sunday, monday, tuesday)
    print("All temperatures > 0", all(t > 0 for t in all_temps))

if __name__ == '__main__':

    main()
    exit(0)