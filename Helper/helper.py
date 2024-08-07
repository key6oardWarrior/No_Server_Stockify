from sys import exit
from os.path import expanduser, join
from shutil import rmtree

from Helper.Errors import ConnectionError
from Robinhood_API.Login import UserAuth

userAuth = UserAuth()

def checkConnection():
	from socket import create_connection

	try:
		create_connection(("1.1.1.1", 443)).close()
	except:
		raise ConnectionError("Cannot connect to the internet")

from UI.PyGUI import WIN_CLOSED, Window

from robin_stocks.robinhood.authentication import logout

def killApp() -> None:
	'''
	Exit app ASAP
	'''
	rmtree(join(expanduser("~"), ".tokens"), ignore_errors=True)

	if userAuth.isLoggedIn:
		logout()

	exit(0)

def exitApp(event, window: Window, isLogout=False, rm_tree=True) -> bool:
	'''
	Determin if the event wants app to die

	# Params:
	event - If the user clicked exit or clicked the exit at the top left of
	app\n
	window - The window to close\n
	isLogout - True if you want to logout of Robinhood

	# Returns:
	True if event = Exit or WIN_CLOSED (see PyGUI) else False
	'''
	if((event == "Exit") or (event == WIN_CLOSED)):
		window.close()

		if((isLogout) and (userAuth.isLoggedIn)):
			logout() # logout of user's robinhood account on close

		if rm_tree:
			rmtree(join(expanduser("~"), ".tokens"), ignore_errors=True)

		return True
	return False

class Version:
	__major = 1
	__minor = 0
	__micro = 0

	def __init__(self, version: str=None) -> None:
		if version:
			versionLst: list[str] = version.split(".")

			self.__major = int(versionLst[0])
			self.__minor = int(versionLst[1])
			self.__micro = int(versionLst[2])

	@property
	def major(self) -> int:
		return self.__major

	@property
	def minor(self) -> int:
		return self.__minor

	@property
	def micro(self) -> int:
		return self.__micro

	@property
	def version(self) -> str:
		return "v" + str(self.__major) + "." + str(self.__minor) + "." + \
			str(self.__micro)