from sys import path
from shutil import rmtree
from os.path import join, expanduser
path.append(path[0][:path[0].rfind("\\")])

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