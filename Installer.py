from os import getcwd
from os.path import isdir, join
from shutil import copytree
from sys import path
from pip._internal import main

def lst2Str(lst: list[str]) -> str:
	'''
	Convert a list to a str

	# Params:
	lst - The string list to be converted to a str

	# Returns:
	A string with all of lst's data
	'''
	string = ""
	for itr in lst:
		string += itr + "\n"

	return string

def fixFile(PATH: str) -> None:
	'''
	Fix one of Python's packages, so it will work for our App

	# Params:
	PATH - The file to be fixed
	'''
	rFile = open(PATH, "r").read().splitlines()
	rFile[806] = "class _PluralBinding (collections.abc.MutableSequence):"
	open(PATH, "w").write(lst2Str(rFile))

def createPath(pyPackages: str) -> None:
	'''
	Create the needed paths for the app to run

	# Params:
	pyPackages - All of Python's packages
	'''
	JOINED_PATH = join(pyPackages, join("src", "lxml"))
	if isdir(JOINED_PATH) == False:
		copytree(join(pyPackages, "lxml"), JOINED_PATH)

	# edit content.py to fix error if error exists
	try:
		from collections import MutableSequence
	except:
		fixFile(join(pyPackages, "pyxb\\binding\\content.py"))

if __name__ == "__main__":
	path.append(path[0][:path[0].rfind("\\")])

	# upgrade pip and install all required dependencies
	main(["install", "--upgrade", "pip"])
	CWD = getcwd()
	for package in open(join(CWD, join(join("Dependencies",
		"requirements.txt"))), "r").readlines():
		main(["install", package])

	createPath(path[-2])
