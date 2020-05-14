import ghau
import time
VERSION = "v4.2.4"
REPO = "Space-Turtle0/PythonComputer"
update = ghau.Update(version=VERSION, repo=REPO, reboot=ghau.python("2019pc.py"))
update.update()
print("Complete...")
time.sleep(2)
