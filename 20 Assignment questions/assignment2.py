#Write a Python program using the os module to list all files and folders in a given directory and separate them into two lists: files and directories.

import os

#path is given explicitly
path = r'C:\Wipro\Python--Automataive--Batch9'

#declaring empty lists to store files and directories
files=[]
directories=[]

#iterating through items in the given path
for item in os.listdir(path):#os.listdir() method returns a list containing the names of the entries in the directory given by path
    item_path = os.path.join(path, item) #os.path.join() joins items in the path
     
     #checking whether the item is a file or directory and appending to respective lists
    if os.path.isdir(item_path):
        directories.append(item)
    elif os.path.isfile(item_path):
        files.append(item)

#printing files and directories separately as lists
print("Files :")
print(files)
print("Directories :")  
print(directories)
