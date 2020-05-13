import ghau

VERSION = "v4.1.3"
REPO = "Space-Turtle0/PythonComputer"
update = ghau.Update(version=VERSION, repo=REPO, reboot=ghau.python("2019pc.py"))
update.update()
