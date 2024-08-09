from os import walk, system, mkdir, getcwd, rename
from os.path import join, isdir
from shutil import copy2

from pyshortcuts import make_shortcut

# compile main dir
system("py -m compileall -b")

dirTree: tuple = next(walk("."))

if isdir("bins") == False:
	mkdir("bins")

# compile sub dirs
for itr in dirTree[1]:
	system(f"cd {itr} && py -m compileall -b")

	# copy all compiled (non-unit test) files into bins folder
	if((itr != ".git") and (itr != "bins") and (itr != ".vscode") and
		(itr != "UnitTest")):
		dirName = join("bins", itr)

		if isdir(dirName) == False:
			mkdir(dirName)

		for file in next(walk(itr))[2]:
			if file[-4:] == ".pyc":
				copy2(join(itr, file), dirName)

# copy main compiled files to bins folder
for itr in dirTree[2]:
	if itr[-4:] == ".pyc":
		if((itr != "compile.pyc") and (itr != "setup.pyc")):
			copy2(itr, "bins")

# move the pyw file into the UI folder
CWD: str = getcwd()
PATH: str = join(CWD, join("UI", "Stockify.py"))
rename(PATH + "c", PATH + "w")
BINS_PATH: str = join(CWD, join("bins", "UI"))
copy2(PATH + "w", BINS_PATH)

make_shortcut(join(BINS_PATH, "Stockify.pyw"), "Stockify", startmenu=False, executable="pyw")
