"""
Learn about iterable, iterator objects
use the built-in:and to access them next()
iter(): create an iterable object
next(): fetch the next element in teh iterable object
"""


def first(iterable):
    """
    Return the next member on the list if available
    :param iterable: iterable object
    :return: next member or
    :except: ValueError for stop iteration
    """
    iterator = iter(iterable) # iterator = iter(iterable) creating a new one every time
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")


def main():
    """
    Test function
    :return: 
    """
    iterable = ["Spring", "Summer", "Fall", "Winter"]
    iterator = iter(iterable) # give me an iterator
    print(type(iterator), iterator) # -> <class 'list_iterator'> <list_iterator object at 0x000002AAA443A908>
    print(next(iterator)) # -> Spring
    # print(next(iterator)) # -> Summer
    # print(next(iterator)) # -> Fall
    # print(next(iterator)) # -> Winter
    # #print(next(iterator)) will give an error you are at the end of the list



if __name__ == '__main__':
    main()
    exit(0)