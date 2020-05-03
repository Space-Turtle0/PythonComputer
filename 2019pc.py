import time, webbrowser, os, warnings, random, math, datetime
from time import sleep
from os import system
from tqdm import tqdm
import sys
import string

'''
Well it looks like your trying to edit me!
That's great! If you want to change the OS BOOT number, change the variable below and rename it to whatever you want, this will also appear in the logs!
------------------------------------------------------------------
If you want to change some of the configuration, scroll down to find that variable and change the values. 

NOTE: MAKE SURE YOU KNOW WHAT YOU ARE CHANGING!
- You might cause some unwanted changes if you don't know what you are doing. 

'''

#OSBOOT Version 
OSInfo = "4.1.3"
BetaValue = False
#The Value above tells if the following 

#Use this to skip login start!
DEVMODE = False

#Starter Values:
filetf = False
Register = False
KeyAWOL = False
letters = string.ascii_letters
DeCode = ( ''.join(random.choice(letters) for i in range(10)) )
save = "Null"
linkpl = "Null"


#Update Notes:
print("Thank you for using PythonComputer or OSBOOTTURTLE!")
print("PatchNotes/Updates:")
print(
  "- Added secret keys and Decoder \n"
  "- Removed save as it doesn't work now... \n"
  "- Fixed some nasty bugs. \n"
)
print("Welcome to OSBOOTTURTLE " + OSInfo + "!")

#Starting Screen

print("  Starting Drivers... \n")
rangeArg1 = 0
rangeArg2 = 999999
randNum = 23
for i in tqdm(range(rangeArg1, rangeArg2)):
  randNum += 1
sleep(2)
print("  Checking Data... \n")
rangeArg1 = 0
rangeArg2 = 999999
randNum = 23
for i in tqdm(range(rangeArg1, rangeArg2)):
  randNum += 1
sleep(2)

print(" Booting OSPUBLICTURTLE" + OSInfo + "... \n")
rangeArg1 = 0
rangeArg2 = 999999
randNum = 23
for i in tqdm(range(rangeArg1, rangeArg2)):
  randNum += 1
sleep(2)
system('clear')


'''Function:
#If you want to define a function, its best to do it here if its a startup requirement!
'''

# Using for Beta Drive Gen
'''

file = open('location',"r")
print("ID" , '\t' ,"Name",'\t' ,"SM", '\t' ,"MM",'\t' ,"SoM",'\t',"TOTAL")
print("------------------------------------------")
for line in file:
    x = line.strip().split(',')
    if len(x) == 5:
        print(x[0], '\t', x[1], '\t', x[2], '\t', x[3], '\t', x[4], '\t', int(x[2]) + int(x[3]) + int(x[4]))
        #fileout = open('location',"a")
        #fileout.write(ft)

# (x[1],'\t',x[2],'\t',x[3],'\t' ,x[4], '\t', int(x[2],10)+ int(x[3],10)+ int(x[4],10))
'''

#Loading Bar Function
def LoadingBar():
  print(" Processing... \n")
  rangeArg1 = 0
  rangeArg2 = 999999
  randNum = 23
  for i in tqdm(range(rangeArg1, rangeArg2)):
    randNum += 1
  sleep(2)
  system('clear')


#Login Function
def loginstart():
  def colortext():
    class bcolors:
      HEADER = '\033[95m'
      OKBLUE = '\033[94m'
      OKGREEN = '\033[92m'
      WARNING = '\033[93m'
      FAIL = '\033[91m'
      ENDC = '\033[0m'
      BOLD = '\033[1m'
      UNDERLINE = '\033[4m'
      BLINK = '\33[6m'
currentDT = datetime.datetime.now()
PCProcessLOGS = open("PCProcessLOGS","a")
PCProcessLOGS.write("Setting up services... \n")
LoadingBar()
PCProcessLOGS.write(str(currentDT) + "\n")
PCProcessLOGS.write("------------------\n")
PCProcessLOGS.close
currentDT = datetime.datetime.now()
if DEVMODE == False:
  print(str(currentDT))
  print("Reseting Services...")
  time.sleep(2)
  print("Creating processes")
  print("No account file found... [Error Code 5] ")
  PCLOGS =open("SetupLogs.txt","a")
  time.sleep(2)
  print("New Account Required!")
  time.sleep(3)
  ssuser = input("New Username: ")
  sspass = input("New Password: ")
  print("Setting you up as the admin account...")
  print("Setup Success!")
  accountstat = 'Admin'
  PCLOGS = open("SetupLogs.txt", "a")
  currentDT = datetime.datetime.now()
  PCLOGS.write(str(currentDT) + "\n")
  # "\n"
  PCLOGS.write("Used " + ssuser + " as the Username to log in \n")
  PCLOGS.write("Used " + sspass + " as the Password to log in \n")
  PCLOGS.write("Setup is working /-")
  PCLOGS.write("Setting up files... \n")
  PCLOGS.write("No Domain Found, proceeding as root user \n")
  PCLOGS.write("Proceeding as OSTURTLESTRSPPER " + OSInfo + "\n")
  PCLOGS.write("Root User logging in...\n")
  PCLOGS.write("Closing Terminal! \n")
  PCLOGS.write("----------------\n")
  PCLOGS.close()
  AccountManager =open("AccountProcess.txt","a")
  AccountManager.write("Accounts Currently Stored: \n")
  AccountManager.write("ROOT USER: " + ssuser + "\n")
  AccountManager.write("--------------------------\n")
  AccountManager.close
  websitechoicetf = 0
  print("Booting...")
  time.sleep(2)
  print("No Domain Found...")
  class bcolors:
      HEADER = '\033[95m'
      OKBLUE = '\033[94m'
      OKGREEN = '\033[92m'
      WARNING = '\033[93m'
      FAIL = '\033[91m'
      ENDC = '\033[0m'
      BOLD = '\033[1m'
      UNDERLINE = '\033[4m'
      print(f"{OKGREEN}Attempting to log in...{ENDC}")
  usernamestart = input("Username: ")
  if usernamestart == ssuser:
      print("Acessing domain!")
  else:
      exit("Invalid Domain/Username")
  psword = input("Please enter your password ")
  if psword == (sspass):
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        print(f"{WARNING}Logging in...{ENDC}")

    time.sleep(2)
    PCLOGS = open("SetupLogs.txt", "a")
    PCLOGS.write("Logged in as ROOT USER \n")
    PCLOGS.write("---------------------\n")
    PCLOGS.close()


#Function Workspace End



if DEVMODE == False:
  loginstart()


#Not being used
'''
def colortext():
  class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\33[6m'
'''

Startboot =input("Press Enter to get started...")
if Startboot == "":
    print(
        "Welcome to the Home Screen. This computer is not built for real life useage.."
    )
    print("This computer is soley for the use of testing.")
    time.sleep(2)
    des = "y"
    while des == "y":
        print("Options:")
        print("Settings, Browser, Calculator, Console, Config, Settings-2")
        appchoice = input("What would you like to use today?")
        system('clear')
        if appchoice == ("Settings"):
            PCProcessLOGS = open("PCProcessLOGS","a")
            PCProcessLOGS.write("Setting up "+ appchoice + "\n")
            PCProcessLOGS.write(str(currentDT) + "\n")
            PCProcessLOGS.write("------------------\n")
            PCProcessLOGS.close
            print("Loading...")
            time.sleep(2)
            print("Connecting to document...")
            Logs = open(r"Logs.txt", "r")
            print(Logs.readlines())
            Logs.close()

        if appchoice == ("Browser"):
            PCProcessLOGS = open("PCProcessLOGS","a")
            PCProcessLOGS.write("Setting up "+ appchoice + "\n")
            PCProcessLOGS.write(str(currentDT) + "\n")
            PCProcessLOGS.write("------------------\n")
            PCProcessLOGS.close
            print("Loading...")
            webchoice = input("Open bookmarks?")
            if webchoice == "yes":
                print("Loading...")
                if "websitechoicetf" == 1:
                    print("Opening" + linkpl)
                    Logsweb = open(r"Logs.txt", "a")
                    webbrowser.open("www." + linkpl, new=0, autoraise=True)
                    Logsweb.write("Visited: www." + linkpl + "\n")
                else:
                    print("Sorry, you have no bookmark!")
                    print("Set it up in Config!")

            else:
                website = input(
                    "What would you like to search? Format: python.org ")
                print("Opening " + "www." + website)
                time.sleep(1)
                print("Requesting www." + website, "with chrome")
                time.sleep(1)
                webbrowser.open("www." + website, new=0, autoraise=True)
                Logsweb = open(r"Logs.txt", "a")
                Logsweb.write("Visited: www." + website + "\n")
                Logsweb.close()
        if appchoice == ("Calculator"):
            PCProcessLOGS = open("PCProcessLOGS","a")
            PCProcessLOGS.write("Setting up "+ appchoice + "\n")
            PCProcessLOGS.write(str(currentDT) + "\n")
            PCProcessLOGS.write("------------------\n")
            PCProcessLOGS.close

            def add(x, y):
                return x + y

            # This function subtracts two numbers
            def subtract(x, y):
                return x - y

            # This function multiplies two numbers
            def multiply(x, y):
                return x * y

            # This function divides two numbers
            def divide(x, y):
                return x / y

            print("Select operation.")
            print("1.Add")
            print("2.Subtract")
            print("3.Multiply")
            print("4.Divide")

            # Take input from the user
            choice = input("Enter choice(1/2/3/4):")

            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
            else:
                print("Invalid input")

        if appchoice == ("RMGame"):
            LoadingBar()
            PCProcessLOGS = open("PCProcessLOGS","a")
            PCProcessLOGS.write("Setting up "+ appchoice + "\n")
            PCProcessLOGS.write(str(currentDT) + "\n")
            PCProcessLOGS.write("------------------\n")
            PCProcessLOGS.close
            print("Please wait, downloading game...")
            time.sleep(5)
            print("Aquiring plugin...")
            print("Aquiring pip.2.py")
            print("Aquiring connection...")
            print("Testing connection...")
            print("Connection Secure")
            time.sleep(3)
            print("Starting download...")
            print("Downloading...")
            time.sleep(5)
            print("Completed.")
            print("Running file...")
            time.sleep(3)
            print("Welcome to the RM game.")
            print(
                "This game is undergoing high improvements.So please be mindful of the game.."
            )
            print("Checking status of the game...")
            print("Starting connection...")
            time.sleep(3)
            webbrowser.open(
                'www.roblox.com/games/1466995005/Ragdoll-Mayhem?refPageId=d99e069d-944a-4f48-b55c-34352d088da1',
                new=0,
                autoraise=True)
            time.sleep(2)

        if appchoice == "Console":
            PCProcessLOGS = open("PCProcessLOGS","a")
            PCProcessLOGS.write("Setting up "+ appchoice + "\n")
            PCProcessLOGS.write(str(currentDT) + "\n")
            PCProcessLOGS.write("------------------\n")
            PCProcessLOGS.close
            print("Launching a instance")

            class bcolors:
                HEADER = '\033[95m'
                OKBLUE = '\033[94m'
                OKGREEN = '\033[92m'
                WARNING = '\033[93m'
                FAIL = '\033[91m'
                ENDC = '\033[0m'
                BOLD = '\033[1m'
                UNDERLINE = '\033[4m'
                print(f"{FAIL}Instance requires credentials to start...{ENDC}")

            time.sleep(2)
            username1 = input("Username: ")
            if username1 == "BlueCore":
                password1 = input("Password: ")
                if password1 == "RedApple":
                    instancename = input("Instance Name:")
                    time.sleep(2)
                    warnings.warn("Attempting to start...")
                    time.sleep(2)
                    print("Starting " + instancename)
                    os.system('start "SSH Client":')
                    time.sleep(3)

                    class bcolors:
                        OKGREEN = '\033[92m'
                        print("Sucessfully Started " + instancename)

        if appchoice == "Settings-2":
            PCProcessLOGS = open("PCProcessLOGS","a")
            PCProcessLOGS.write("Setting up "+ appchoice + "\n")
            PCProcessLOGS.write(str(currentDT) + "\n")
            PCProcessLOGS.write("------------------\n")
            PCProcessLOGS.close
            os.system('start ms-settings:')

        if appchoice == "Prime":
            PCProcessLOGS = open("PCProcessLOGS","a")
            PCProcessLOGS.write("Setting up "+ appchoice + "\n")
            PCProcessLOGS.write(str(currentDT) + "\n")
            PCProcessLOGS.write("------------------\n")
            PCProcessLOGS.close
            num = int(input("Number to test: "))
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        print(num, "is not a prime number")
                        print(i, "times", num // i, "is", num)
                        break
                else:
                    print(num, "is a prime number")
            else:
                print(num, "is not a prime number")

        if appchoice == "Config":
            PCProcessLOGS = open("PCProcessLOGS","a")
            PCProcessLOGS.write("Setting up "+ appchoice + "\n")
            PCProcessLOGS.write(str(currentDT) + "\n")
            PCProcessLOGS.write("------------------\n")
            PCProcessLOGS.close
            print("Get your path/link ready!")
            print("If you are saving a file...")
            print("Please enter the FULL PATH!")
            print("Otherwise it will open a new file with that name!")
            websitechoiceconfig = input("What should I open? (File or Link?) ")
            if websitechoiceconfig == "File":
                print("Please wait...")
                fileopen = input("Please input a files name or path! ")
                des2009 = input("What do you want me to do with it? ")
                if des2009 == "Open":
                    print("Opening" + fileopen)
                    Bookmarkfile = open("r", fileopen, "a")
                    if des2009 == "Save":
                        print("Saving!")
                        save1 = input("What do you want this called? ")
                        save1 == fileopen
                        print("Saved as" + save1 + ".")
                        filetf = True

            if websitechoiceconfig == "Link":
                PCProcessLOGS = open("PCProcessLOGS","a")
                PCProcessLOGS.write("Setting up "+ appchoice + "\n")
                PCProcessLOGS.write(str(currentDT) + "\n")
                PCProcessLOGS.write("------------------\n")
                PCProcessLOGS.close
                linkpl = input("Copy and Paste your link here.. ")
                des2008 = input("Should I open it? ")
                websitechoicetf = 1
                if des2008 == "Open":
                    webbrowser.open("www." + linkpl, new=0, autoraise=True)
                else:
                    print("Alright, I saved the link.")
                    print("If you want to remove it, come back to this!")

        if appchoice == "Credits":
            PCProcessLOGS = open("PCProcessLOGS","a")
            PCProcessLOGS.write("Setting up "+ appchoice + "\n")
            PCProcessLOGS.write(str(currentDT) + "\n")
            PCProcessLOGS.write("------------------\n")
            PCProcessLOGS.close
            print("Loading...")
            time.sleep(2)
            print("Thank you for using my program!")
            print(
                "I've spent a lot of time on this project and its been wonderful!"
            )
            print("If you don't know what this is...")
            print(
                "Its a simple .py file that tried to show many modules/python features!"
            )
            print("Hopefully you took something away from this!")
            print("Program made by Space")
            print("aka: Space Turtle!")
            print("Check out my other stuff on GitHub!")
            time.sleep(1)
            webbrowser.open(
                "https://github.com/Space-Turtle0/PythonComputer/blob/master/2019pc.py",
                new=0,
                autoraise=True)

        if appchoice == "WEB":
            PCProcessLOGS = open("PCProcessLOGS","a")
            PCProcessLOGS.write("Setting up "+ appchoice + "\n")
            PCProcessLOGS.write(str(currentDT) + "\n")
            PCProcessLOGS.write("------------------\n")
            PCProcessLOGS.close
            print("uwu, you found this ")
            print("Well then bye!")
        if appchoice == "Domain":
            PCProcessLOGS = open("PCProcessLOGS","a")
            PCProcessLOGS.write("Setting up "+ appchoice + "\n")
            PCProcessLOGS.write(str(currentDT) + "\n")
            PCProcessLOGS.write("------------------\n")
            PCProcessLOGS.close
            print("Loading...")
            time.sleep(2)
            if Register == False:

                class bcolors:
                    HEADER = '\033[95m'
                    OKBLUE = '\033[94m'
                    OKGREEN = '\033[92m'
                    WARNING = '\033[93m'
                    FAIL = '\033[91m'
                    ENDC = '\033[0m'
                    BOLD = '\033[1m'
                    UNDERLINE = '\033[4m'
                    print(f"{FAIL}Launching Domain...{ENDC}")
                    f = open("Logs.txt", "w+")
                    domainname = input("Domain name: ")
                    domainpassword = input("Domain Password: ")
                    f.write(domainname)
                    f.write("\n")
                    f.write(domainpassword)
                    with open('Logs.txt', 'r') as f:
                        contents = [line.strip() for line in f.readlines()]
                    username = contents[0]
                    pw = contents[1]
                    print("Complete..")
                    print("Domain Username:" + username)
                    print("Domain Password:" + pw)
                    f.close()
                    Register = True
            else:
                print("You already have a Domain Setup...")
                Domaininput = input("Do you want to edit/delete this?")
                if Domaininput == "yes":
                    f = open("Logs.txt", "w+")
                    with open("Logs.txt", "w") as f:
                        f.write("")
                        print("Deleting...")
                        time.sleep(2)
                        print("Complete")
                        time.sleep(2)
                        print(
                            "To Edit this, please come back and create a new Domain!"
                        )
                        print(
                            "To Log in with this, please go to DomainConsole!")
                        Register = False
        if appchoice == "Exit":
            PCProcessLOGS = open("PCProcessLOGS","a")
            PCProcessLOGS.write("Setting up "+ appchoice + "\n")
            PCProcessLOGS.write(str(currentDT) + "\n")
            PCProcessLOGS.write("------------------\n")
            PCProcessLOGS.close
            print("...")
            time.sleep(2)
            exit("Logging out...")
        if appchoice == "DomainConsole":
            PCProcessLOGS = open("PCProcessLOGS","a")
            PCProcessLOGS.write("Setting up "+ appchoice + "\n")
            PCProcessLOGS.write(str(currentDT) + "\n")
            PCProcessLOGS.write("------------------\n")
            PCProcessLOGS.close
            print("waiting...")
            if Register == True:
                print(f"{bcolors.WARNING}Launching!{bcolors.ENDC}")
                os.system('start "Domain VENV":')
            else:
                print(
                    f"{bcolors.FAIL}You don't have a domain! Please set one up!{bcolors.ENDC}"
                )
                print(f"{bcolors.FAIL}Failed to Launch!{bcolors.ENDC}")
        if appchoice == "Notes":
            PCProcessLOGS = open("PCProcessLOGS","a")
            PCProcessLOGS.write("Setting up "+ appchoice + "\n")
            PCProcessLOGS.write(str(currentDT) + "\n")
            PCProcessLOGS.write("------------------\n")
            PCProcessLOGS.close
            print("Loading...")
            notesyn = input("Are you writting a new file? (y/n) ")
            if notesyn == "y":
                print("Loading...")
                time.sleep(2)
                notestxt = input(
                    "Name of the file:(add file ending at end! (.txt)) ")
                notesx = open("notestxt.txt", "w")
                notesx.close()
                notesx = open("notestxt.txt", "a")
                writenote = input("What would you like to write? ")
                notesx.write(writenote)
                notesx.close()

                def writenotes():
                    notesx = open("notestxt.txt", "a")
                    writenote = input("What would you like to write? ")
                    notesx.write(writenote + "\n")
                    notesx.close()

                noteagain = input("Would you like to write again?  ")
                if noteagain == "yes":
                    writenotes()
                else:
                    print("Reading you lines!")
                    notesx.close()
                    notesx = open("notestxt.txt", "r")
                    notesx.readlines(1)
                    notesx.close
        if appchoice == "Time":
            PCProcessLOGS = open("PCProcessLOGS","a")
            PCProcessLOGS.write("Setting up "+ appchoice + "\n")
            PCProcessLOGS.write(str(currentDT) + "\n")
            PCProcessLOGS.write("------------------\n")
            PCProcessLOGS.close
            print("Current Year is: %d" % currentDT.year + "\n")
            print("Current Month is: %d" % currentDT.month + "\n")
            print("Current Day is: %d" % currentDT.day + "\n")
            print("Current Hour is: %d" % currentDT.hour + "\n")
            print("Current Minute is: %d" % currentDT.minute + "\n")
            print("Current Second is: %d" % currentDT.second + "\n")
            print("Current Microsecond is: %d" % currentDT.microsecond + "\n")
        if appchoice == "Seating Chart":
            PCProcessLOGS = open("PCProcessLOGS","a")
            PCProcessLOGS.write("Setting up "+ appchoice + "\n")
            PCProcessLOGS.write(str(currentDT) + "\n")
            PCProcessLOGS.write("------------------\n")
            PCProcessLOGS.close
            '''
          numstu =int(input("How many students?"))

          words = ['Me', 'Merry', 'Help', 'Please', 'Christmas']
          random.shuffle(words)
          '''
            list = []
            i = 0
            a = 0
            maxo = int(input("Number of students: "))
            table = int(input("Number of tables? "))
            if maxo % table == 0:
                print("Check 1 complete")
                while i < maxo:
                    a = input("Please enter student" + str(i) + "'s" +
                              " name : ")
                    list.append(a)
                    i += 1
                random.shuffle(list)
                print(list)
            for x in range(table):
                  #a + 1
                  print(a)
            else:
                print(
                     "Sorry! You don't have enough tables or have a odd amount of tables"
                 )
        if appchoice == "Accounts":
          PCProcessLOGS = open("PCProcessLOGS","a")
          PCProcessLOGS.write("Setting up "+ appchoice + "\n")
          PCProcessLOGS.write(str(currentDT) + "\n")
          PCProcessLOGS.write("------------------\n")
          PCProcessLOGS.close
          print(f"{bcolors.WARNING}Please wait, loading your accounts!{bcolors.ENDC}")
          time.sleep(2)
          AccountManager =open("AccountProcess.txt","r")
          AccountManager.readlines() 
          time.sleep(2)
          print("Say n if you would like to switch accounts!")
          accountnew =input("Would you like to create a new account? (y/n)")
          if accountnew == "y":
            print("Please wait...")
            if accountstat == "Admin":
              time.sleep(2)
              print("Admin Account Registration Restricted, only 1 admin account per domain!")
              newaccount = input("Username: ")
              newpassword =input("Password: ")
              PCLOGS = open("SetupLogs.txt", "a")
              currentDT = datetime.datetime.now()
              PCLOGS.write(str(currentDT) + "\n")
              PCLOGS.write("Attempting to create an account... \n")
              PCLOGS.write("Created an account: \n")
              PCLOGS.write("Username: " + newaccount + "\n")
              PCLOGS.write("Password: " + newpassword + "\n")
              PCLOGS.write("------------------------")
              PCLOGS.close
              AccountManager =open("AccountProcess.txt","a")
              currentDT = datetime.datetime.now()
              AccountManager.write(str(currentDT) + "\n")
              AccountManager.write("Normal Account: " + newaccount + "\n")
              AccountManager.write("--------------------------\n")
              newaccount1 = True
              accountstat = "Admin"
              print("Created your account!")
              print("Username for new account:" + newaccount)
              print("To switch accounts, go back to Accounts and say n where it says to create a new account!")
              print("Forget your password? Check out Pass Helper!")
            else:
                print("Access Denied! Log into the admin account!")
          else:
            print("Fetching login details...")
            if newaccount1 == True:
              print("Restoring data...")
              if accountstat == "Admin":
                print("Logging in as " + newaccount)
                checkpass =input("Password: ")
                if checkpass == newpassword:
                  print("Logged in!")
                  accountstat = "Normal"
              else:
                print("Logging in as " + ssuser)
                checkapass =input("Password: ")
                if checkapass == sspass:
                  print("Logged in!")
                  accountstat = "Admin"

            else:
              print("No account file found!")
              print("Please go create another account and come back here to login!")

        if appchoice == "Pass Helper":
          PCProcessLOGS = open("PCProcessLOGS","a")
          PCProcessLOGS.write("Setting up "+ appchoice + "\n")
          PCProcessLOGS.write(str(currentDT) + "\n")
          PCProcessLOGS.write("------------------\n")
          PCProcessLOGS.close
          print("Accessing Account Processes")
          passhelper = input("What account do you need to access?")
          if passhelper == newaccount:
            print("Accessing Account...")
            adminpassword = input("Admin Password: ")
            if adminpassword == sspass:
              print("Granted!")
              AccountProcess =open("AccountProcess","a")
              AccountProcess.write("Used admin password to enter Pass Helper \n")
              AccountProcess.write("----------------------------\n")
              AccountProcess.close()
            else:
              print("Wrong password!")
              AccountProcess =open("AccountProcess","a")
              AccountProcess.write("Entered wrong password (Admin) \n")
              AccountProcess.write("----------------------------\n")
              AccountProcess.close()
          else:
            print("Accessing")
            time.sleep(2)
            adminrec = input("Admin Username:")
            if adminrec == ssuser:
              print("Your password: " + sspass)
              AccountProcess =open("AccountProcess","a")
              AccountProcess.write("Requested Admin Password \n")
              AccountProcess.write("----------------------------\n")
              AccountProcess.close()
              
        if appchoice == "WebConsole":
          print("Attempting to connect to the server...")
          LoadingBar()
          pythonstore =open("CodeEval.txt","a")
          print("If you would like to exit out of the program/loop please use "'exit'" in order to leave the VM" )
          des1 = "n"
          while des1 == "n":
            mycode =input("Code to execute: ")
            pythonstore.write(mycode + "\n")
            if mycode == "exit":
              pythonstore.close
              print("Exiting Console...")
              des1 = "yes"
              system('clear')
            else:
              exec(mycode)

        if appchoice == "Spam":
          for i in range(1000):
            print(" Processing... \n")
            rangeArg1 = 0
            rangeArg2 = 999
            randNum = 23
            for i in tqdm(range(rangeArg1, rangeArg2)):
              randNum += 1
            print("Did you enjoy? lol")

        if appchoice == "what":
          print("why u here?")
        if appchoice == "chatter":
          CH =open("ChatterData","a")
          CHname =input("Hello there! What should I call you?: ")
          print("Nice to meet you " + CHname)
          CH.write("Well it was nice meeting you! Here is what I asked you! \n")
          CH.write("Your name!: " + CHname + "\n")
          time.sleep(2)
          CHaction =input("Well what would you like to do? " + CHname)
          CH.write("What you wanted to do!:" + CHaction + "\n")
          time.sleep(2)
          CHfavplay =input("nice nice, well what do you like to play?")
          CH.write("You like to play " + CHfavplay + "\n")
          CHcolor =input("What is your favorite color?")
          CH.write("Your favorite color is" + CHcolor + "\n")
        if appchoice == "Reload":
          print("Are you sure you want to restart the machine?")
          restartconf =input("(y/n)")
          if restartconf == "y":
            print("Preparing to reload OS BOOT.")
            system("clear")
            print(".")
            time.sleep(2)
            system('clear')
            print("..")
            time.sleep(2)
            system('clear')
            print('...')
            time.sleep(2)
            system('clear')
            print("Removing Storage Containers....")
            time.sleep(2)
        if appchoice == "TaskManager":
          print("...")
          time.sleep(3)
          print("Loading...")
          time.sleep(2)
          print("Running Process: \n")
          #mark for auto generate keys
          #1 # printing letters
          letters = string.ascii_letters
          AcctProccessKEY = ( ''.join(random.choice(letters) for i in range(10)) )
          #2
          # printing letters
          letters = string.ascii_letters
          MainpyKEY = ( ''.join(random.choice(letters) for i in range(10)) )
          #3
          # printing letters
          letters = string.ascii_letters
          CodeEvalKEY = ( ''.join(random.choice(letters) for i in range(10)) )
          #4
          # printing letters
          letters = string.ascii_letters
          LogsKEY = ( ''.join(random.choice(letters) for i in range(10)) )
          #5
          # printing letters
          letters = string.ascii_letters
          PCProcessLOGSKEY = ( ''.join(random.choice(letters) for i in range(10)) )
          print(" Application Name | Disk Usage | Secret                 | Folder | Total lines used")
          print("1) Main.py        | 51%        |" + MainpyKEY + "       | N/A    | 1343  ")
          print("2) AcctProcess    | 4%         |" + AcctProccessKEY + " |DataLogs| 737   ")
          print("3) CodeEval       | 5%         |" + CodeEvalKEY + "     |DataLogs| 343   ")
          print("4) Logs           | 5%         |" + LogsKEY + "         |DataLogs| 7862  ")
          print("5) MPU            | 1%         | *****                  |DataLogs| ***   ")
          print("6) PCProcessLOGS  | 20%        |" + PCProcessLOGSKEY + "|DataLogs| 2323  ")
          print("7) SetupLogs      | 5%         | *****                  |DataLogs| 32786 ")
          time.sleep(2)
          #Update note
          print("Details:")
          class bcolors:
            HEADER = '\033[95m'
            OKBLUE = '\033[94m'
            OKGREEN = '\033[92m'
            WARNING = '\033[93m'
            FAIL = '\033[91m'
            ENDC = '\033[0m'
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'
            BLINK = '\033[6m'
            print(f"{OKGREEN}Any process's that have stars in their secret means you do not have enough permission to see a core process key{ENDC}")
            time.sleep(2)
            decodeAsk =input("Would you like to grant permission to see this file?")
            if decodeAsk == "y":
              KeyAWOL = True
              time.sleep(2)
              print("Generating keys...")
              time.sleep(2)
              print("Your key: \n")
              KeyAWOL = True
              #print(KeyAWOL)
              print(DeCode)
              print("------------------------------")
              print("Use this key in the `Decoder` module to get information regarding the terminal! ")

            
        if appchoice == "Decoder":
          print("Please wait...")
          time.sleep(2)
          print("Fetching key information...")
          YourKey =input("Paste your key here: ")
          if YourKey == DeCode:
            print("Checking key...")
            letters = string.ascii_letters
            MPUKEY = PCProcessLOGSKEY = ( ''.join(random.choice(letters) for i in range(10)) )
            #2
            letters = string.ascii_letters
            SetupLogsKEY = PCProcessLOGSKEY = ( ''.join(random.choice(letters) for i in range(10)) )
            time.sleep(2)
            print("Message from key: ")
            system('clear')
            print("MPU Secret: " + MPUKEY)
            print("SetupLogs Secret: " + SetupLogsKEY)

          

            
  
                


            

          
      

