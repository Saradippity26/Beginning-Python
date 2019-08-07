"""
Learn about sets
An unordered collection of unique, immutable objects
Define it using {} just like a dictionary but you do not need a key, analysis is done on a group level not an
individual key level
You can use the set constructor to create one
"""


def main():
    """
    Test function
    :return: 
    """
    p = {6, 78, 21, 45}
    print(p, type(p)) # -> [21, 45, 78, 6} <class 'set'>
    data = [1, 3, 5, 2, 88, 3, 1]
    print(data, type(data)) # -> [1, 3, 5, 2, 88, 3, 1] <class 'list'>

    # eliminate duplicates: creating a set has to have unique objects so it removes duplicates
    sdata = set(data)
    print(sdata, type(sdata)) # -> {88, 1, 2, 3, 5} <class 'set'>

    # Iterate with a for loop
    for item in sdata:
        print(item) # -> 88 \n 1 \n 2....

    # Supports membership testing: in , not in
    print(5 in sdata) # -> True

    # To add elements to set use method: add() adds individual , update() adds multiple
    sdata.add(45)
    print(sdata) # -> {1, 2, 3, 5, 45, 88}

    sdata.update([2, 99, 44, 33, 1, 2, 88]) # will only insert the unique values
    print(sdata) # -> {1, 2, 3, 99, 5, 33, 44, 45, 88}

# Method to help eliminate elements:
    # Remove() will remove a given element, raises key error if not found
    sdata.remove(44)
    print(sdata) # -> {1, 2, 3, 99, 5, 33, 45, 88}
    # example code for element not in class key error
    #sdata.remove(77) :: 77 is does not exist so when we use the remove() it will throw an error
    #print(sdata) # -> KeyError: 77  -  element is not in the set

    # Discard(): Does not raise and error
    sdata.discard(77)
    print(sdata) # -> {1, 2, 3, 99, 5, 33, 45, 88}

    # How to make a copy: Use method(): copy(),
    bk_data = sdata.copy()
    print(bk_data is sdata) # to check if it is a shallow copy (yes of the elements it points to)
    # : not same object but has the same values -> False
    print(bk_data == sdata) # -> True

    # Define some sets: s.union, s.intersection (elements in both sets), s.differences (eliminate those in the other set
    # s.superset
    blue_eyes = {"Olivia", "Harry", "Lily", "Jack"}
    long_hair = {"Harry", "Jack", "Amelia", "Mia", "Joshua"}
    smell_hcn = {"Harry", "Amelia"}
    taste_ptc = {"Harry", "Lily", "Amelia", "Lola"}
    o_blood = {"Mia", "Joshua", "Lily", "Olivia"}
    b_blood = {"Amelia", "Jack"}
    a_blood = {"Harry"}
    ab_blood = {"Joshua", "Lola"}

    print(blue_eyes.union(long_hair)) # as long the element is in one of the two sets
    # -> {'Amelia', 'Mia', 'Harry', 'Olivia', 'Joshua', 'Lily', 'Jack'}
    print(blue_eyes.intersection(taste_ptc)) # have both - > {'Lily', 'Harry'}
    print(smell_hcn.symmetric_difference(a_blood)) # who is not in both lists -> {'Amelia'}
    print(long_hair.difference(ab_blood)) # -> {'Amelia', 'Jack', 'Harry', 'Mia'}
    print(taste_ptc.issuperset(smell_hcn)) # -> True


if __name__ == '__main__':
    main()
    exit(0)