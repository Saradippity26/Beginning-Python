#dot string documentation """ documentation of the file itself:
""" Learn about control flow in Python"""

#IF statement parenthesis are not required in python: True capital T means keyword
if True:
    #indentation is 4 spaces
    print("It is true")

print("Done")

if bool("eggs"):
#checks to see if the string is empty. its not so it is true
    print("Yes please!")

if "eggs":
    print("Yes, why not")

#Flat is better than nested (Python: Simple is easier to read, get away from incrypted syntax
h = 42
if h > 50:
    print("Greater than 50")
    if h > 100:
        print("Greater than 100")
elif h < 50: # Else If
    print("Less than 50")
else:
    print("Equals 50")



print("Done")