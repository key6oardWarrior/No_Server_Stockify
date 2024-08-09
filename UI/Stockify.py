from sys import path, platform
from shutil import rmtree
from os.path import join
path.append(path[0][:path[0].rfind("\\")])

# add path to needed libs
if platform == "win32":
	from os.path import expanduser
	path.append(expanduser("~") + "\\AppData\\Local\\Stockify\\UI")
	path.append(expanduser("~") + "\\AppData\\Local\\Stockify")
elif((platform == "linux") or (platform == "linux2")):
	path.append("/usr/local/Stockify/UI")
	path.append("/usr/local/Stockify")
else: # darwin
	path.append("/usr/local/bin/Stockify/UI")
	path.append("/usr/local/bin/Stockify")

from PyGUI import Button, Text, Window

from Account import loginScreen
from TradeInfo import dataScreen
from Helper.helper import exitApp, exit
from Helper.creds import winName

layout = [
	[Button("Login", pad=((110, 5), (0, 0)))],
	[Text("Powered by Robin_Stocks and PySimpleGUI", pad=((0, 0), (0, 0)), text_color="light gray")],
]
isBack = True

while isBack:
	landingPage = Window(winName, layout)
	event, values = landingPage.read()

	if exitApp(event, landingPage, True):
		exit(0)

	landingPage.close()
	if event == "Login":
		isBack = loginScreen()

rmtree(join(expanduser("~"), ".tokens"), ignore_errors=True)
dataScreen()