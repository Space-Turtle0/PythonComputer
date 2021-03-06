import time, webbrowser, os, warnings, random, math, datetime
from time import sleep
from os import system, name
from tqdm import tqdm
import logging
import sys
import string

Perm = os.path.realpath(os.path.dirname(sys.argv[0]))
'''
Well it looks like your trying to edit me!
That's great! If you want to change the OS BOOT number, change the variable below and rename it to whatever you want, this will also appear in the logs!
------------------------------------------------------------------
If you want to change some of the configuration, scroll down to find that variable and change the values. 

NOTE: MAKE SURE YOU KNOW WHAT YOU ARE CHANGING!
- You might cause some unwanted changes if you don't know what you are doing. 

'''

#Logging Setup:
logging.basicConfig(filename ='app.log', 
                        level = logging.ERROR)
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 

#OSBOOT Version 
OSInfo = "4.3"
#Public Build
BetaValue = True
if BetaValue == True:
  OSInfoB = "4.1.6"
  #Beta build
#The Value above tells if the following 

#Use this to skip login start!
DEVMODE = True

#Starter Values:
filetf = False
Register = False
KeyAWOL = False
SecurityBlocked = False
letters = string.ascii_letters
DeCode = ( ''.join(random.choice(letters) for i in range(10)) )
save = "Null"
linkpl = "Null"
newaccount1 = False
WebConsoleSec = False
WarnWebC = 0

#Security Values
FileShield = True
BehaviorShield = True
WebShield = True
MailShield = True
accountstat = "admin"

#Use this to bypass warning...
DevStat2 = "Turtle2020"

#Update Notes:
print("Thank you for using PythonComputer or OSBOOTTURTLE!")
print("Patch Notes/Updates:")
print(
  "- Security Module was updated! \n"
  "- Added a new RegEdit app so you can modify applications! \n"
  "- Fixed some nasty bugs. \n"
)
print("Welcome to OSBOOTTURTLE " + OSInfo + "!")

#Required Function prior to setup!
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

#Slow tyoe
def cool_print(str):
  for char in str:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)

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

print(" Booting OSPUBLICTURTLE " + OSInfo + "... \n")
rangeArg1 = 0
rangeArg2 = 999999
randNum = 23
for i in tqdm(range(rangeArg1, rangeArg2)):
  randNum += 1
sleep(2)
clear()

if DEVMODE == True:
  cool_print("WARNING!: You have DEVMODE Turned on! \n")
  time.sleep(2)
  warningdev = input("Turn off DEVMODE? (y/n): \n")
  if warningdev == "y":
    print("Turning off DEVMODE...")
    DEVMODE = False
    print("DEVMODE is now: ")
    print(DEVMODE)
  else:
    cool_print("In order to protect un-published data, please enter the global DEV Password! \n")
    DEVPass2 = input("Password: ")
    if DEVPass2 == DevStat2:
      cool_print("Proceeding with DEVMODE on... \n")
    else:
      cool_print("Failed to authorize, try again later. Proceeding with DEVMODE off. ")

'''Function:
#If you want to define a function, its best to do it here if its a startup requirement!
'''

# Using for Beta Drive Gen 2
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
  clear()

#Universal Bar
def UBar():
   rangeArg1 = 0
   rangeArg2 = 999999
   randNum = 23
   for i in tqdm(range(rangeArg1, rangeArg2)):
    randNum += 1
   sleep(2)


  

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
PCProcessLOGS = open(os.path.join(Perm, "PCProcessLOGS.txt"), "a")
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
  logger.error("No account file, proceeding with account setup...")
  time.sleep(2)
  print("New Account Required!")
  time.sleep(3)
  ssuser = input("New Username: ")
  sspass = input("New Password: ")
  print("Setting you up as the admin account...")
  print("Setup Success!")
  accountstat = 'Admin'
  currentDT = datetime.datetime.now()
  # "\n"
  logger.info("Used " + ssuser + " as the Username to log in \n")
  logger.info("Used " + sspass + " as the Password to log in \n")
  logger.info("Setup is working /-")
  logger.info("Setting up files... \n")
  logger.info("No Domain Found, proceeding as root user \n")
  logger.info("Proceeding as OSTURTLESTRSPPER " + OSInfo + "\n")
  logger.info("Root User logging in...\n")
  logger.info("Closing Terminal! \n")
  logger.info("----------------\n")
  logger.info("Accounts report:")
  logger.info("Accounts Currently Stored: \n")
  logger.info("ROOT USER: " + ssuser + "\n")
  logger.info("--------------------------\n")
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
    logger.info("Logged in as ROOT USER \n")
    logger.info("---------------------\n")


#Function Workspace End



if DEVMODE == False:
  loginstart()




#Not being used

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



Startboot =input("Press Enter to get started...")
if Startboot == "":
    print(
        "Welcome to the Home Screen. This computer is not built for real life useage.."
    )
    print("This computer is ran by the command line!")
    time.sleep(2)
    des = "y"
    while des == "y":
        print("Options:")
        print("Settings, Browser, Calculator, Console, Config, Settings-2")
        appchoice = input("What would you like to use today?")
        clear()
        if appchoice == ("Settings"):
            logger.info("Setting up "+ appchoice + "\n")
            logger.info(str(currentDT) + "\n")
            logger.info("------------------\n")
            PCProcessLOGS.close
            print("Loading...")
            time.sleep(2)
            print("Connecting to document...")
            Logs = open(os.path.join(Perm, "Logs.txt"), "r")
            print(Logs.readlines())
            Logs.close()

        if appchoice == ("Browser"):
            logger.info("Setting up "+ appchoice + "\n")
            logger.info(str(currentDT) + "\n")
            logger.info("------------------\n")
            print("Loading...")
            website = input(
              "What would you like to search? Format: python.org ")
            print("Opening " + "www." + website)
            time.sleep(1)
            print("Requesting www." + website, "with chrome")
            time.sleep(1)
            webbrowser.open("www." + website, new=0, autoraise=True)
            Logsweb = open(os.path.join(Perm,"Logs.txt"), "a")
            Logsweb.write("Visited: www." + website + "\n")
            Logsweb.close()
        if appchoice == ("Calculator"):
            logger.info("Setting up "+ appchoice + "\n")
            logger.info(str(currentDT) + "\n")
            logger.info("------------------\n")

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

            Cacl =input("What would you like to open? (Calculator or Prime)?")
            if Cacl == "Prime":
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
                  
            else:

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

        

        if appchoice == "Console":
            logger.info("Setting up "+ appchoice + "\n")
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
            print("This Instance requires different credentials! ")
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


        if appchoice == "Config":
            logger.info.write("Setting up "+ appchoice + "\n")
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
                    print("failed... [Error 5]")
                    if des2009 == "Save":
                        print("Saving!")
                        save1 = input("What do you want this called? ")
                        save1 == fileopen
                        print("Saved as" + save1 + ".")
                        filetf = True

            if websitechoiceconfig == "Link":
                logger.info("Setting up "+ appchoice + "\n")
                linkpl = input("Copy and Paste your link here.. ")
                des2008 = input("Should I open it? ")
                websitechoicetf = 1
                if des2008 == "Open":
                    webbrowser.open("www." + linkpl, new=0, autoraise=True)
                else:
                    print("Alright, I saved the link.")
                    print("If you want to remove it, come back to this!")

        if appchoice == "Domain":
            logger.info("Setting up "+ appchoice + "\n")
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
                    f = open(os.path.join(Perm, "Logs.txt"), "a")
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
            logger.info("Setting up "+ appchoice + "\n")
            print("...")
            time.sleep(2)
            exit("Logging out...")

        if appchoice == "DomainConsole":
            logger.info("Setting up "+ appchoice + "\n")
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
            logger.info("Setting up "+ appchoice + "\n")
            print("Loading...")
            notesyn = input("Are you writting a new file? (y/n) ")
            if notesyn == "y":
                print("Loading...")
                time.sleep(2)
                notestxt = input(
                    "Name of the file:(add file ending at end! (.txt)) ")
                notesx = open(os.path.join(Perm, "notestxt.txt"), "w")
                notesx.close()
                notesx = open(os.path.join(Perm, "notestxt.txt"), "a")
                writenote = input("What would you like to write? ")
                notesx.write(writenote)
                notesx.close()

                def writenotes():
                  notesx = open(os.path.join(Perm, "notestxt.txt"), "a")
                  writenote = input("What would you like to write? ")
                  notesx.write(writenote + "\n")
                  notesx.close()
                noteagain = input("Would you like to write again?  ")
                if noteagain == "yes":
                    writenotes()
                else:
                    print("Reading you lines!")
                    notesx.close()
                    notesx = open(os.path.join(Perm, "notestxt.txt"), "r")
                    notesx.readlines(1)
                    notesx.close
                    
        if appchoice == "Time":
            logger.info("Setting up "+ appchoice + "\n")
            print("Current Year is: %d" % currentDT.year + "\n")
            print("Current Month is: %d" % currentDT.month + "\n")
            print("Current Day is: %d" % currentDT.day + "\n")
            print("Current Hour is: %d" % currentDT.hour + "\n")
            print("Current Minute is: %d" % currentDT.minute + "\n")
            print("Current Second is: %d" % currentDT.second + "\n")
            print("Current Microsecond is: %d" % currentDT.microsecond + "\n")

        if appchoice == "Accounts":
          if DEVMODE == True:
            print("You are not allowed to access this component with DEVMODE on")
            exit("Access Denied: DEVMODE can not be used with this config!")
          logger.info("Setting up "+ appchoice + "\n")
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
              if newaccount1 == True:
                print("Warning! You already have an account registered, filling this out will overwrite your other account!")
                newwarn =input("Are you sure you want to proceed?: ")
                if newwarn == "y":
                  print("Exitting...")
                  break
              print("Admin Account Registration Restricted, only 1 admin account per domain!")
              newaccount = input("Username: ")
              newpassword =input("Password: ")
              logger.warning("Attempting to create an account... \n")
              logger.info("Created an account: \n")
              logger.info("Username: " + newaccount + "\n")
              logger.info("Password: " + newpassword + "\n")
              logger.info("Normal Account: " + newaccount + "\n")
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
          logger.info("Setting up "+ appchoice + "\n")
          print("Accessing Account Processes")
          passhelper = input("What account do you need to access?")
          if passhelper == newaccount:
            print("Accessing Account...")
            adminpassword = input("Admin Password: ")
            if adminpassword == sspass:
              print("Granted!")
              logger.info("Used admin password to enter Pass Helper \n")
            else:
              print("Wrong password!")
              logger.info("Entered wrong password (Admin) \n")
          else:
            print("Accessing")
            time.sleep(2)
            adminrec = input("Admin Username:")
            if adminrec == ssuser:
              print("Your password: " + sspass)
              logger.info("Requested Admin Password \n")


              
        if appchoice == "WebConsole":
          print("Attempting to connect to the server...")
          LoadingBar()
          if BehaviorShield == True:
            if WarnWebC == 0:
              print("Security has blocked a threat from establishing a connection to your PC!")
              print("THREAT: WebConsole 3.2")
              AllowTh = input("Allow Access?")
              if AllowTh == "y":
                print("Allowing program...")
              else:
                des = "y"
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
              clear()
            else:
              exec(mycode)


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
            clear()
            print("..")
            time.sleep(2)
            clear()
            print('...')
            time.sleep(2)
            clear()
            print("Removing Storage Containers....")
            time.sleep(2)
            filetf = False
            Register = False
            KeyAWOL = False
            SecurityBlocked = False
            letters = string.ascii_letters
            DeCode = ( ''.join(random.choice(letters) for i in range(10)) )
            newaccount1 = False
            WebConsoleSec = False
            WarnWebC = 0
            #Security Values
            FileShield = True
            BehaviorShield = True
            WebShield = True
            MailShield = True 
            accountstat = "admin"
            print("Restarted values...")
            time.sleep(2)
            print("Reverted to " + OSInfo)


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
            clear()
            print("MPU Secret: " + MPUKEY)
            print("SetupLogs Secret: " + SetupLogsKEY)
            print("Closing out of Decoder")

        if appchoice == "Reboot":
          print("Please wait...")
          time.sleep(2)
          RebootConfirm =input("Are you sure you want to reinstall TurtleOS?")
          if RebootConfirm == "y":
            print("Preparing to reinstall... \n") 
            LoadingBar()
            print("Connecting...")
            time.sleep(2)
            print("Downloading Data... \n")
            LoadingBar()
            print("Extracting Data...")
            LoadingBar()
            print("Mounting Drive...")
            print("This will take a bit!")
            time.sleep(10)
            print("Applying Changes....")
            print("Checking Build...")
            exit("Restarting Machine...")

        if appchoice == "RegEdit":
          print("Checking build date...")
          if DEVMODE == True:
            print("This application is in beta and you may experience bugs!")
            time.sleep(2)
            RegFile = open(os.path.join(Perm, "RegEdit.txt"), "r")
            print(RegFile.read())
            time.sleep(2)
    

          else:
            print("Failed to open...")
            print("You aren't in DEVMODE!")



        if appchoice == "Security":
          print("Loading...")
          LoadingBar()
          if SecurityBlocked == False:
            print("Loading Turtle Anti-Malware...")
            time.sleep(2)
            logger.info("Opening Security...")
            print("There is an update, please wait while we update your system...")
            logger.debug("Updating System...")
            time.sleep(2)
            print("Extracting TurtleAnti-Malware_6.2.7 \n")
            rangeArg1 = 0
            rangeArg2 = 999999
            randNum = 23
            for i in tqdm(range(rangeArg1, rangeArg2)):
              randNum += 1
            sleep(2)
            print("Updating... \n")
            UBar()
            time.sleep(5)
            print("Core Shields:")
            print("1) File Shield     - ON")
            print("2) Behavior Shield - ON")
            print("3) Web Shield      - ON")
            print("4) Mail Shield     - ON")
            print("--------------------")
            print("Scans:   ")
            print("1a) Quick Scan:          ")
            print("2a) Full Disk Scan       ")
            time.sleep(2)
            print("What would you like to modify/run?")
            sec =input("Use the numbers to select an option... ")
            if sec == "1":
              print("Please wait...")
              if FileShield == True:
                FSQ = input("Are you sure you want to turn off this module? (File Shield)")
                if FSQ == "y":
                  print("Attempting to turn off module...")
                  time.sleep(1)
                  if DEVMODE == False:
                    FSQP = input("Enter your password: ")
                    if FSQP == sspass:
                      print("Turned off module")
                    else:
                      print("Wrong password")
                  else:
                    print("Turned off Module.")
                else:
                  print("Okay, good thing you didn't :p")

                
            if sec == "2":
              print("Please wait...")
              if BehaviorShield == True:
                BSQ = input("Are you sure you want to turn off this module? (Behavior Shield)")
                if BSQ == "y":
                  print("Attempting to turn off module...")
                  time.sleep(1)
                  if DEVMODE == False:
                    BSQP = input("Enter your password: ")
                    if BSQP == sspass:
                      print("Turned off module")
                    else:
                      print("Wrong password")
                  else:
                    print("Turned off Module.")
                else:
                  print("Okay, good thing you didn't :p")
            if sec == "3":
              print("Please wait...")
              if WebShield == True:
                WSQ = input("Are you sure you want to turn off this module? (Web Shield)")
                if WSQ == "y":
                  print("Attempting to turn off module...")
                  time.sleep(1)
                  if DEVMODE == False:
                    WSQP = input("Enter your password: ")
                    if WSQP == sspass:
                      print("Turned off module")
                    else:
                      print("Wrong password")
                  else:
                    print("Turned off Module.")
                else:
                  print("Okay, good thing you didn't :p")
            if sec == "4":
              print("Please wait...")
              if MailShield == True:
                MSQ = input("Are you sure you want to turn off this module? (Mail Shield)")
                if MSQ == "y":
                  print("Attempting to turn off module...")
                  time.sleep(1)
                  if DEVMODE == False:
                    MSQP = input("Enter your password: ")
                    if MSQP == sspass:
                      print("Turned off module")
                    else:
                      print("Wrong password")
                  else:
                    print("Turned off Module.")
                else:
                  print("Okay, good thing you didn't :p")
            if sec == "1a":
              print("Preparing to run a quick scan...")
              time.sleep(2)
              QSM = random.randint(0,1)
              print("Scanning BOOTDISK \n")
              UBar()
              print("Checking AccountProcess.txt ...")
              time.sleep(1)
              print("Checking ChatterData...")
              print("Checking CodeEval.txt")
              print("Checking PCProcessLOGS.txt ")
              time.sleep(1)
              print("Checking SetupLogs.txt")
              print("Checking Encode Drive...")
              time.sleep(5)
              if QSM == 1:
                print("Threats found!")
                time.sleep(1)
                print("Collecting Data...")
                time.sleep(1)
                print("Trojan Found at: ")
                print("C:/bootdisk/rootuser/datalogs/files/rtxa.exe")
                cleanupQ =input("Would you like to fix this?")
                if cleanupQ == "y":
                  print("Fixing threat...")
                  time.sleep(2)
                  print("Threat moved to virus chest")
                  time.sleep(3)
                else:
                  print("Leaving threat...")
                  time.sleep(2)
              else:
                print("No threats found...")

            elif sec == "2a":
              print("Preparing to run a full scan...")
              print("Scanning BOOTDISK \n")
              UBar()
              print("Checking AccountProcess.txt ...")
              time.sleep(1)
              print("Checking ChatterData...")
              print("Checking CodeEval.txt")
              print("Checking PCProcessLOGS.txt ")
              time.sleep(1)
              print("Checking SetupLogs.txt")
              print("Checking Encode Drive...")
              FSM = random.randint(0,1)
              if FSM == 1:
                print("Threats found!")
                time.sleep(1)
                print("Collecting Data...")
                time.sleep(1)
                print("Trojan Found at: ")
                print("C:/bootdisk/rootuser/datalogs/files/rtxa.exe")
                cleanupF =input("Would you like to fix this?")
                if cleanupF == "y":
                  print("Fixing threat...")
                  time.sleep(2)
                  print("Threat moved to virus chest")
                  time.sleep(3)
                else:
                  print("Leaving threat...")
                  time.sleep(2)
              else:
                print("No threats found...")

          
              

