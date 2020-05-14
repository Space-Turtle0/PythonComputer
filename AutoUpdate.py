import os
import time
import ghau
VERSION = "v4.2"
REPO = "Space-Turtle0/PythonComputer"
if "GAPI" in os.envrion:
  update = ghau.Update(version=VERSION, repo=REPO, reboot=ghau.python("2019pc.py"), auth=os.environ["GAPI"])
else:
  update = ghau.Update(version=VERSION, repo=REPO, reboot=ghau.python("2019pc.py"))
update.update()
print("Complete...")
time.sleep(2)
