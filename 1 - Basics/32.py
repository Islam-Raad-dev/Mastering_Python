# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------

import os

myFile = open("Islam.txt", "a")
myFile.truncate(5)

myFile = open("Islam.txt", "a")
print(myFile.tell())

myFile = open("Islam.txt", "r")
myFile.seek(11)
print(myFile.read())

os.remove("Islam.txt")
