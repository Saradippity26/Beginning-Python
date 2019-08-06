"""
Set an alarm to remind to take a break by playing a youtube video
google: how to open a youtube video in python
"""

import webbrowser
import time
# in the python console import webbrowser then help(webbrowser)

def main():
    """
    Test function
    :return none
    """

    video_address = "https://www.youtube.com/watch?v=g8vHhgh6oM0"
    # copy and paste the youtube video address
    # delay or sleep command
    counter = 0 # initialize the loop to start at zero
    while counter < 3: # number of times you want the loop to run
        time.sleep(60*60) # sleep for ("x") amount of time then run -- (60*60) = 1 hr (sec * mins)
        webbrowser.open(video_address)
        counter += 1 # increase and run loop again if < 3
        print("It is time to take a break, is:", time.ctime()) # will print each time -- time.ctime is for system time

if __name__ == '__main__':
    #should include in every file - also need to define main above
    main()
    exit(0)

#we still need to add a timer -- google how to keep track of time in python
#(7) import time library -- PC import time -> help (time) (18) look for sleep delay for number of seconds
#(20) make a while loop of two iterations to set for every hour for then next "x" amount of time
