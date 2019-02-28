import os

dir_name = os.getcwd() 

for root, dirs, files in os.walk(dir_name, topdown=False):
    for file in files:
        file_name = os.path.splitext(file)[0]#file name no ext
        extension = os.path.splitext(file)[1]
        dir_name = os.path.basename(root)
        os.rename(root+"/"+file,root+"/"+dir_name+extension)
input()
