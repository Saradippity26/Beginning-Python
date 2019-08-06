"""
Learn more about strings

"""


def main():
    """
    Test function
    :return: 
    """
    s1 = "This is super cool"
    print("size of s1", len(s1)) # -> size of s1 18
    # concatenation "+" with the plus operator
    s2 = "Weber" + "State" + "University"
    print(s2) # -> WeberStateUniversity
    # if you want a space you will need to add it as well


# If you need to join large string use the join() method instead of the "+" operator
    teams = ["Real Madrid", "Barcelona", "Manchester United"]    # create a list of soccer teams
    # customer request all records to be join with : as a separator
    record = ":".join(teams) # first parameter is the separator
    print(record) # -> Real Madrid:Barcelona:Manchester United
    # to separate by line record = "\n".join(teams)


# can split records as well
    print("Split rec", record.split(":")) # -> returns list: Split rec ['Real Madrid', 'Barcelona', 'Manchester United']

# partitioning strings
    departure, separator, arrival ="London:Edinburgh". partition(":")
    print(departure, arrival) # ->London Edinburgh

# dummy object _  use this if you needed to preserve the separator as well ":"
# departure, _, arrival ="London:Edinburgh". partition(":") -> London : Edinburgh
# could so a tuple as well: t = "London:Edinburgh".partition(":")
# print(t, type(t)) -> ('London', ':', 'Edinburgh') < class, 'tuple'>

# String formatting using format()
#   print("The age of {0} is {1}.format("Mario", 34)) -> The age of Mario is 34
#   print("The age of {0} is {1}, and the birthday of {0} is {2}.format("Mario", 34, "August 12th))
# -> The age of Mario is 34, and the birthday of Mario is August 12th

# omitting the index
# print('The best numbers are {} and {}'.format(4, 22)) -> The best numbers are 4 and 22

# by field name
# print("Current position {latitude} {longitude}".format(latitude="60N", longitude="5E"))
# -> Current position 60 N 5E

# print elements of list
# print("Galactic position x={pos[0]}, y={pos[1]}, z={pos[2]}.format(pos=(85.6, 23.3, 99.0)))
# -> Galactic position x=85.6, y=23.3, z=99.0


if __name__ == '__main__':
    main()
    exit(0)


