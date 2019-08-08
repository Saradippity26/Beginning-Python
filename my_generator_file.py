"""
Learn about generator functions
- Describe iterable series with code functions
- Are lazy evaluated: the next value in the sequence is computed on demand
- Can model infinite series /sequences: data streams, mathematical series with no end
- Can use pipelines: output of one program can be an input for another program (used a lot in linux)
They use the yield keyword
"""


def gen123():
    yield 1
    yield 2
    yield 3


def gen246():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6
    print("About to return")


def main():
    """
    Test function
    :return: 
    """
    g = gen123()
    print(g, type(g)) # -> <generator object gen123 at 0x000002359EDD9518> <class 'generator'>
    # yield next value
    print(next(g)) # -> 1
    print(next(g)) # -> 2
    print(next(g)) # -> 3
    # print(next(g)) # -> what happens if you call again? -> Error StopIteration

    # how to go over all possible choices: Iterate over the generator function
    for v in gen123():
        print(v) # -> 1 \n 2\n 3\n

    h = gen246()
    print(next(h))
    print(next(h))
    print(next(h))
    print(next(h))
    print(next(h))




if __name__ == '__main__':
    main()
    exit(0)