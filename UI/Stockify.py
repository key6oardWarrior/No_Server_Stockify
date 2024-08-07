from sys import path, platform
path.append(path[0][:path[0].rfind("\\")]) # not production

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
from UpdateApp import updateScreen
from TradeInfo import dataScreen
from Helper.helper import exitApp, exit
from Helper.creds import winName
from Uninstaller import uninstall

layout = [
	[Button("Login", pad=((5, 5), (0, 0))), Button("Check for Updates", pad=((0, 0), (0, 0))), Button("Uninstall")],
	[Text("Powered by Robin_Stocks and PySimpleGUI", pad=((20, 0), (0, 0)), text_color="light gray")],
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
	elif event == "Uninstall":
		uninstall()
		exit(0)

dataScreen()