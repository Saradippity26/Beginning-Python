"""Learn about functions/(python: Definitions)
use the keywords: def <name> (parameters):  ((function skeleton))
Between functions you should have two spaces of blank lines
"""


def even_or_odd(number): #should return the string even or odd
    """
    Find if number is even or odd
     print "even" on even numbers
            "odd" on odd numbers
    :param number: input number
       """
    #pass    #dummy statement in python, meets requirement that you need at least one statement
    if number % 2 == 0:
        print("even")
    else:
        print("odd")

def main(): #main is not a keyword in python
    """Test function
    :return nothing
    """

#call functions
print(__name__) #two underscore and keyword name: python console -> import functions
even_or_odd(89)
even_or_odd(22)

if __name__ == "__main__":
    main()
    exit(0)

