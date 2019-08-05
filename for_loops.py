"""
Practice for loops:
Keyword: for
"""
#Create a list of cities
cities = ["London", "New York", "Madrid", "Ogden", "Paris"] # when it gets to the end it will exit the loop
#Iterate over this collection
for city in cities:
    print(city)
d = {'alice': '801-123-45-8988',
     'pedro': '956-445-78-8966',
     'john': '651-321-66-4477'}
#Iterate over a dictonary
for item in d:
    print(item) #is getting the key values by default not the value associated with the key
for item in d:
    print(item, "=>", d[item]) #prints them all key and value

#what about if you have a file from the web you want to count the number of times a word appears or the total number of
#words in the file.