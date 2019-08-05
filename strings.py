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
s6 = 'this "wow'
print(s6)
#raw strings for python: tells to take string as is (exactly as you meant it to be displayed).  has to prefix with an r
raw_string = r'C:\User\Documents\Books'
print(raw_string)
#print would hide all \\ raw will display them
#string sequence: and array of characters
s = "parrot"
print("s[4]", s[4], type(s))
#index notation is for representing the 'O' # begins at zero index notation 0,1,2,etc. [displays specific character]
#lets say we want to capitalize the first letter only. Search for a method
help(str)
print(s,s.capitalize())

