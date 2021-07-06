from os import listdir
from os.path import isfile, join
import os

def absoluteFilePaths(directory):
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))
            print(os.path.join(dirpath, f))

mypath = '/Users/Lenovo/StudioProjects/Matched-App/assets/images/personality_icons'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)

for root, dirs, files in os.walk(os.path.abspath(mypath)):
    for file in files:
        print(os.path.join(root, file))
absoluteFilePaths(mypath)


