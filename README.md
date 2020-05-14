# PythonComputer
[![Run on Repl.it](https://repl.it/badge/github/Space-Turtle0/PythonComputer)](https://repl.it/github/Space-Turtle0/PythonComputer)

Stable Version: ![version](https://img.shields.io/badge/version-4.2.3-blue)
# PythonComputer is a simple python program (no display) that simulates a computer. 
>This Program isn't a finished project yet! 


# My command line keep crashes!
Well that shouldn't be happening. Instead of using command prompt, download one of the code editors above and run it in there. If there are any syntax issues that pop up, please open an issue so we can fix it!


# Help! What do I download?

**2019pc.py**

*Download this! Most recent version and being worked on!*

- https://github.com/Space-Turtle0/PythonComputer/releases

*Why can't I just download the branch instead of a repo?*
Don't, branch files are still considered non-production ready until they are actually published as a release, many updates on there are finished but do not fit together (formatting)

**Why are there multiple branches?**
**master** - This branch is the final non-buggy product. Went through Beta Branch first before publish

**Beta-Branch-v2** - This branch is non-production ready. Yes its where all the good new features come up but its not a finished product yet.

**Repl-Support-Branch** - This branch is used for people using repl. Or an online IDE. It requires more files to operate and a run command. Which is `python 2019pc.py`


# What is AutoUpdate.py?
This file is a cool new feature that allows you to download the newest "release" without coming back to github, although its pretty important to check back for the new changelogs, its an easier tool to help you download the new version without coming back here!
In order for this module to work, please run this in a command propmt (With admin!)
`pip install ghau`
and to upgrade `pip install ghau --upgrade`

To learn more, visit: https://github.com/InValidFire/ghau


# [New Python Computer]
- If you're using the new 2019pc.py
Its straight forward. 
>>> Adding on to the file!
To setup a branch, add the following
```
if appchoice == "Your Portion Name":
    print("Move on from here")
```
Use that ^ to move on with the file!

>>> Setting up before execution
*This type of execution should be used only if you need to reset variables on startup*
*If you need to compare values inside the `while des == y` loop, place it before asking what to open*

*Import values at the very start (lines 1-6)*

**Update to 4.1.3!**
- This version now supports functions! Along with starter values, you can also define your functions!
```
#Starter Values:
filetf = False
Register = False
KeyAWOL = False
letters = string.ascii_letters
DeCode = ( ''.join(random.choice(letters) for i in range(10)) )
save = "Null"
linkpl = "Null"
```
This is an example startup as soon as you run the program.

> **If you need to reset values inside the loop**
Place your `define` statements after asking about `appchoice`!

**What do I need to change if im modifying the program?**
There are a few things you can change that will a) modify the log version and b) modify startup.
- `OSInfo` - This will change the version that appears in the logs and on startup.
- `BetaValue` - Used to mark in GitHub if the version is currently in Beta, doesn't really do anything though.
- `DEVMODE` - Need to test something but the logging in portion taking too much of your time? Well now you can skip it just by marking it as `True`!
- Everything else in the `Starter Values` are marked as False/null just so the program is marked back to default!
- Need to create a function? Well now you can pre-define it in the function workspace! There is no need to cram it in a random spot now!



***Have any questions? DM Space#1613*** 
- On Discord

Program Built by Space Turtle / Space
Test
Have fun! 😁
