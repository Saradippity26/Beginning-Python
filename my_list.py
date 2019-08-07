"""
Template creation: File -> settings -> search template -> Python script 
"""


def main():
    """
    Test function
    :return: 
    """
    s = "show how to do it".split()
    print(s, type(s)) # -> ['show', 'how', 'to', 'do', 'it'] <class 'list'>
    # access by index
    print("s[3]", s[3]) # should print if true -> s[3] do
    print("Last member:", s[len(s) - 1]) # very unpythonic -> Last member: it
    # use negative index
    print("s[-1]", s[-1]) # -> s[-1] it  : useful if your list is indexed by type
    # slicing : chucks of the string in ranges of the collection, string in this case
    print("from 1 to one before the last member", s[1:-1]) # -> from 1 to one before the last member ['how', 'to', 'do']
    # only want the in between (not the 0 not the end) how to do? add this to the print statement , s[1:-1])
    print("from 1 to three members", s[1:3]) # -> from 1 to three members ['how', 'to']
    print("from the 2nd to the end", s[1:]) # to include the end -> from the 2nd to the end ['how', 'to', 'do', 'it']
    print("from beginning to three", s[:3]) # from beginning to three ['show', 'how', 'to']
    print("access to everything", s[:]) # -> access to everything ['show', 'how', 'to', 'do', 'it']
    # used to produce a new list
    # Make a copy of list
    t = s # shallow copy only copy the reference
    print("s:", s) # -> s: ['show', 'how', 'to', 'do', 'it']
    print("t", t) # -> t ['show', 'how', 'to', 'do', 'it']
    print("t is s:", t is s) # true or false -> t is s: True
    # now try below slice, we want t as it own because we are modifying data we need t as its own list
    t = s[:] # deep copy includes the values
    print("t is s:", t is s) # same as calling the copy list method -> t is s: False
    print("t == s", t == s) # == checks values -> t == s True
    # other ways: t = s.copy() or t = list(s) will produce a new list

    # shallow copies
    a = [[1, 2], [3, 4]]  # a list of list
    print(a, type(a)) # -> [[1, 2], [3, 4]] <class 'list'>
    print(a[0]) # -> [1, 2]
    print("a[0]:", a[0]) # -> a[0]: [1, 2]
    print("a[0][1]:", a[0][1]) # use for two dimensions -> a[0][1]: 2

    # copy the list of list
    b = a[:]
    print("b is a", b is a) # -> b is a False
    print("a[0]:", a[0]) # -> a[0]: [1, 2]
    print("b[0]:", b[0]) # -> b[0]: [1, 2]
    print("a[0] is b[0]", a[0] is b[0]) # they are the same object -> a[0] is b[0] True

    # lets change one element
    a[0] = [8, 9]
    print("change a[0] to [8, 9]") # -> change a[0] to [8, 9]
    print("b is a", b is a) # -> b is a False
    print("a[0]:", a[0]) # -> a[0]: [8, 9]
    print("b[0]:", b[0]) # -> b[0]: [1, 2]
    print("a[0] is b[0]", a[0] is b[0])  # helps with performance -> a[0] is b[0] False

    print("a[1] is b[1]", a[1] is b[1]) # -> a[1] is b[1] True
    # modify a[1]
    a[1].append(5)
    print("a[1]:", a[1]) # -> a[1]: [3, 4, 5]
    print("b[1]:", b[1]) # -> b[1]: [3, 4, 5]
    print("a[1] is b[1]", a[1] is b[1]) # -> a[1] is b[1] True
    print("a:", a) # -> a: [[8, 9], [3, 4, 5]]
    print("b:", b) # -> b: [[1, 2], [3, 4, 5]]

    # Repetition with lists
    c = [21, 37]
    d = c * 4
    print("c", c) # -> c [21, 37]
    print("d", d) # created another space in memory with four references -> d [21, 37, 21, 37, 21, 37, 21, 37]
    # while they are the same values they all point to the same reference: d is a list of references that points to a
    # list. d has four elements pointing at one object

    s = [[-1, 1]] * 5 # creates a list of lists: references all point to the same object
    print(s) # -> [[-1, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 1]]
    s[1].append(7) # all elements will be effected: All elements (7) will be changed
    print(s) # -> [[-1, 1, 7], [-1, 1, 7], [-1, 1, 7], [-1, 1, 7], [-1, 1, 7]]

    # index method() for list
    w = "the quick brown fox jumps over the lazy dog".split() # .split creates a list by splitting the string
    i = w.index('fox') # index will search and give you the value of where 'fox' is at
    print("the index of the 'fox' entry is:", i) # -> the index of the 'fox' entry is: 3

    # or we can get the value of 'fox' by w[i]
    w = "the quick brown fox jumps over the lazy dog".split()
    i = w.index('fox')
    print("the index of the 'fox' entry is:", i, w[i])  # -> the index of the 'fox' entry is: 3 fox

    # i = w.index('cat') # exception error will be thrown if value is not in index list
    # print("the index of the 'cat' entry is:", w[i])

    # Membership testing with count() method : used to find duplicates
    print("'the' value is ", w.count("the")) # how many 'the' are in the list? -> 'the' value is  2

    # can also test membership with "in" and "not in"
    print(37 in [12, 22, 37, 99]) # -> True
    print(78 not in [12, 22, 37, 99]) # -> True

    # Removing elements from a list: index and del
    w = "the quick brown fox jumps over the lazy dog".split()
    print(w) # -> ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
    del w[3] # delete using index
    print(len(w), w) # -> 8 ['the', 'quick', 'brown', 'jumps', 'over', 'the', 'lazy', 'dog']

    # Remove using remove() method
    w.remove("over")
    print(len(w), w) # -> 7 ['the', 'quick', 'brown', 'jumps', 'the', 'lazy', 'dog']

    # same as
    del w[w.index('dog')] # del can be used with dictionaries for particular element removal,
    # works to remove an element in any collection
    print(len(w), w)  # -> 6 ['the', 'quick', 'brown', 'jumps', 'the', 'lazy']

    # Rearranging the list of elements
    g = [1, 11, 21, 1211, 11211]
    print("g:", g) # -> g: [1, 11, 21, 1211, 11211]
    g.reverse() # permanent changes order of array! if you don't want it to be permanently changed make a copy
    print("reverse g:", g) # -> reverse g: [11211, 1211, 21, 11, 1]
    g.reverse()
    print("reverse again g:", g) # -> reverse again g: [1, 11, 21, 1211, 11211]

    # Sort method accepts two arguments, key and reverse
    d = [21, 31, 11, 77, 88, 33, 101, 1]
    print("d:     ", d) # -> d:      [21, 31, 11, 77, 88, 33, 101, 1]
    d.sort() # permanent changes
    print("sort d:", d) # -> sort d: [1, 11, 21, 31, 33, 77, 88, 101]

    d = [21, 31, 11, 77, 88, 33, 101, 1]
    d.sort(reverse=True)
    print("sort.reverse d:", d) # default sorts in ascending order -> sort.reverse d: [101, 88, 77, 33, 31, 21, 11, 1]

    # Sort by Key
    w = "the quick brown fox jumps over the lazy dog".split()
    print(w) # -> ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
    w.sort(key=len) # how many characters each member has len
    print(w) # -> ['the', 'fox', 'the', 'dog', 'over', 'lazy', 'quick', 'brown', 'jumps']


if __name__ == '__main__':
    main()
    exit(0)

