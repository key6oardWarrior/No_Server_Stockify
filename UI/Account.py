from PyGUI import Button, Input, Text, Window

from Helper.creds import winName
from Helper.helper import exitApp, exit, checkConnection, \
	userAuth

from shutil import rmtree
from os.path import join, expanduser

def attemptLogin(email: str, password: str) -> None:
	userAuth.login(email, password)

def loginScreen() -> bool:
	'''
	# Returns:
	True if user has logged in successfuly. False if user clicks back button
	'''
	layout = [
		[Text("Enter your robinhood email address:"), Input(key="email", size=(30, 1))],
		[Text("Enter your password:"), Input("",
			key="password", password_char="*", size=(15, 1), do_not_clear=False)],
		[Button("Submit", key="submit"), Button("Back", key="back")]
	]

	login = Window(winName, layout)
	SIZE = len(layout)

	while userAuth.isLoggedIn == False:
		rmtree(join(expanduser("~"), ".tokens"), ignore_errors=True)
		event, values = login.read()

		if exitApp(event, login, True):
			exit(0)

		if len(layout) > SIZE:
			del layout[-1]

		try:
			checkConnection()
		except:
			layout.append([Text("Check Internet Connection", text_color="red")])
			login.close()
			login = Window(winName, layout)
			continue

		if event == "submit":
			values["email"] = values["email"].strip().lower()

			if((values["email"] == "") or (values["password"] == "")):
				layout.append([Text("Enter your email and password to login", text_color="red")])
				login.close()
				login = Window(winName, layout)
				continue

			attemptLogin(values["email"], values["password"])
			if userAuth.isLoggedIn == False:
				login.close()
				layout.append([Text(userAuth.loginInfo, text_color="red")])
				login = Window(winName, layout)

		elif event == "back":
			login.close()
			return True

	login.close()
	return False
