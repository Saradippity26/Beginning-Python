""" Learn about lists:
regular python does not have arrays it has lists. reason hard to explain an array to non coders. List is easier to
explain.
performance wise arrays do better than lists because the size is set and you are not constructing and destructing objects
all the time.
Unlike lists, lists are mutable (can be replaced), you can append update elements to it
"""

l = [1, 2, 3] #use [] for defining a lists; elements are separated by commas
print("List", 1, type(1))

#can have lists of any types because it is a list of objects
a = ["apple", "orange", "pear"]
#acces by index notation
print(a, a[1])  #Note: first index is zero

#replace an element
a[0] = "tomatoes"
print(a, a[1])
a[1] = 3.14
print(a, a[1])

#Begin with an empty list : use a while loop to request three users to enter thier names. find a method
names = [] #plural is a list

#ask user to enter 3 names, and add them to the list (append is your friend)
total = 0
while total < 3:
    name = input("enter a name")
    names.append(name)
    total = total + 1
# display list
print(names)

#hashes: accessed by a key.