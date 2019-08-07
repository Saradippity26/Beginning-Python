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




if __name__ == '__main__':
    main()
    exit(0)

