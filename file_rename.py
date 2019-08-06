"""
Rename the files from a folder (to follow a naming convention, add time stamp. etc.)
Get: http://icarus.cs.weber.edu/~hvalle/hafb/prank.zip
we want to rename all the files to not include the numbers, so it displays city name only
"""
import os

def rename_files():
    """
    Rename files in a folder
    :return: nothing
    """
    folder_dir = r"C:\Users\sarahnelson1\Desktop\HAFB - Python Code\Beginning-Python\prankOrig"
    # r mean raw this will include the \ not include them as special characters

    files = os.listdir(folder_dir) # get a list of the files

    saved_path = os.getcwd() # save the current working directory see notes (26)
# Go get the files directory
    os.chdir(folder_dir) # return back home "original directory"

    for file in files: # change from a string output['.DS_Store', '16los angeles.jpg',...
        # to a list output
        # 16los angeles.jpg
        # 17cairo.jpg
        # ...
        new_file = file.lstrip('0123456789') # define the variable new_file -- ('0123456789') still all specified digits
        print("old name", file, "new name", new_file) # print the list of files display old name and new name
        # need to strip the numbers from the names -- help(str.lstrip)
        os.rename(file, new_file) # does not work because need to add (16,20) the file name is a string the files are
        # not in a string it does not know what directories -- 1. provide the absolute path or 2. change the directories
        # google: how to change directories in Python:



def main():
    """
    test function
    :return: nothing
    """
    pass # pass is a dummy place holder to main block is valid
    rename_files() # need to define first (8)


if __name__ == '__main__':
    main()
    exit(0)

# google: how to display the content of the folder in Python : import os for importing operating system
# import os -> PC import os -> help(os) ** can go to python.org as well for help -- help(os.listdir)