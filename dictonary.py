"""
Hashes are access by keys, python uses dictionaries
Dictionaries map keys to values.
In some languages are known as associative arrays, or hashes, or maps.

Create them using {} containing a key-value pair.
Retrieve them by [key_value]  **access individual members with brackets []
"""
#Create a dictonary, the {} and spaces mean dictonary
# variable = {'key' : 'value', 'key' : 'value', 'key' : 'value'}
d = {'alice': '801-123-45-8988',
     'pedro': '956-445-78-8966',
     'john': '651-321-66-4477'}
print(d, type(d))
#access one element
#dictonaries are not in any order the members are access by keys (addresses)
print(d['pedro'])   #returns the value associated with the key pedro

#Add members to the dictonary, of names-> grades
roster = {} #Empty Dictonary
#help(dict) to search for a method to add members
total = 0
while total < 3:
    #get key value
    name = input("enter your name")
    #get value associated to the key
    grade = input("Enter grade")
    #add element to dictonary
    roster[name] = grade
#note: if key value exist, it will update the value otherwise it will be added to the dictonary.
    total += 1
#print dictionary
print(roster)