import os
import shutil
path=input("what is the folder  name")
path2=input("enter your destantion folder")
print(path)
print(path2)
path=path+'/'
path2=path2+'/'

list=os.listdir(path)

for i in list:
    shutil.copy((path+i),path2)
    