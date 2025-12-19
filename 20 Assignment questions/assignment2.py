import os

#path is given explicitly
path = r'C:\Wipro\Python--Automataive--Batch9'

#declaring empty lists to store files and directories
files=[]
directories=[]

#iterating through items in the given path
for item in os.listdir(path):
    item_path = os.path.join(path, item)
    if os.path.isdir(item_path):
        directories.append(item)
    elif os.path.isfile(item_path):
        files.append(item)

#printing files and directories separately as lists
print("Files :")
print(files)
print("Directories :")  
print(directories)
