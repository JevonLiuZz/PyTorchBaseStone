import os
import glob

# rootPath = 'p1/p2'
rootPath = r'p1\p2'
# rootPath = r'.\p1\p2'
# rootPath = r'..\FileRead\p1\p2'
# rootPath = '../FileRead/p1/p2'

myList = [x for x in glob.glob(os.path.join(rootPath, '*.jpg'))]
print(myList)
