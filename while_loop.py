"""
Learn conditional repetition:
Two Loops: for-loops and while-loops
Right click on while_loop.py file > then run to ensure you are running this file
"""

counter = 5
while counter !=0:# while not equal to zero
    print(counter)
    #Augmented Operator
    counter -= 1 #decriment by one each time. Py does not have -- be more explicit

#print("Outside while loop")

counter = 5
while counter:
     print(counter)
     counter -= 1

#Run Forever
while True:
    print("Enter a number")
    response = input()  # take your user input
    if int(response) % 7 == 0:  # means number divisible by 7
        break   #exit loop

