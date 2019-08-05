"""
!!!remember to right click and select your file to run this file
Strings and Collections:
A string is a immutable sequence of unicode code-points (think of them as characters but technically they are not)

"""
print('This is a string')
print("This is a string too")

#concatenational strings and Adjecent strings
s1 = "First"
s2 = "Second"
print(s1 + s2)
#same operation everything is an object
#Multi-line """ Strings and new lines
s3 = """This is a 
multi-line string"""
print(s3)
s4 = "This is \na multi-line\nstring"  #\n means new line therefore no spaces after or will print an extra space
print(s4)
#support for backslash (if you want to print the backslash)
s5 = "A\\in a string"
print(s5) # py is unicode not assci all characters are two bytes 