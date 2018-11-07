## Function renaming file
import os
from string import maketrans # Required to call maketrans function.

def rename_files() :
	# Get file names from the folder

	#list Raw path files
	file_list = os.listdir(r"./images")
	#print(file_list)

	currPath = os.getcwd()

	print("Current Path: " + currPath)

	os.chdir(r"./images")

	# Rename each file 
	for oldname in file_list :

		trantab = maketrans("0123456789","")
		print("Old Filename:" + oldname)
		newname = oldname.translate(trantab)
		print("New Filename:" + newname)
		os.rename(oldname,newname)

	# Reset the path
	os.chdir(currPath)	

rename_files()

print("Done")
