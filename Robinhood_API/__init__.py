from sys import platform, path
slash = "\\" if platform == "win32" else "/"
path.append((path[0])[:path[0].rindex("\\")])