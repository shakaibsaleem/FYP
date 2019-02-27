import os

dir_name = os.getcwd() 

for root, dirs, files in os.walk(dir_name, topdown=False):
    count = 0
    for file in files:
        count += 1
        file_name = os.path.splitext(file)[0]#file name no ext
        extension = os.path.splitext(file)[1]
        dir_name = os.path.basename(root)
        os.rename(root+"/"+file,root+"/"+dir_name+'-'+str(count)+extension)
input()
