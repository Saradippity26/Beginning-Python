"""
get a file from the web, https://icarus.cs.weber.edu/~hvalle/hafb/words.txt

Task: 1 Count the number of words in document
"""
from urllib.request import urlopen #package url
file = "https://icarus.cs.weber.edu/~hvalle/hafb/words.txt"

#with urlopen(file) as story: #give nickname
#connects to file on web and creates an object and is now in story
   # print(story) -- we want to iterate over this
# for line in story:
#            print(line)

#notice output you are getting bytes not strings you will need to decode it
#use the split method for strings , decode it first"C:\Program Files\Python35\python.exe" C:/Users/CCEClass1/Desktop/Beginning-Python/words.py
#b'It was the best of times\n'
#b'it was the worst of times\n'

count = 0
data = {} # empty dictonary
with urlopen(file) as story: #give nickname
    #connects to file on web and creates an object and is now in story
   # print(story) -- we want to iterate over this
   for line in story:
        words = line.decode('utf-8').split() #split with space as
      #print(words)
        for word in words:
            #check if key is already in dictonary
            if word in data:
                data[word] += 1
            else:
                data[word] = 1
            count += 1
print("Total number of words", count)
#print("Total data", data) -- to count the number of times each value appears
#Total data {'us': 2, 'the': 14, 'on': 1, 'of': 12, 'evil': 1, 'present': 1, 'best': 1, 'good': 1, 'degree': 1,

#sort by keys
for key in sorted(data.keys()):
    print(key, data[key])
#how do you test if the value exists in the dictonary: keyword "in"
#get the total count
