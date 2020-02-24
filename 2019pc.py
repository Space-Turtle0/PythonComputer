import time, webbrowser, os, warnings, random, math, datetime
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
currentDT = datetime.datetime.now()
PCProcessLOGS = open("PCProcessLOGS","a")
PCProcessLOGS.write("Setting up services... \n")
PCProcessLOGS.write(str(currentDT) + "\n")
PCProcessLOGS.write("------------------\n")
PCProcessLOGS.close
currentDT = datetime.datetime.now()
print(str(currentDT))
print("Reseting Services...")
time.sleep(2)
print("Creating processes")
print("No account file found... [Error Code 5] ")
PCLOGS =open("SetupLogs.txt")
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
PCLOGS.write("Proceeding as OSTURTLESTRSPPER 3.6.8 \n")
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
filetf = False
Register = False
print("Booting...")
time.sleep(2)
print("No Domain Found...")

#Loading..................

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
        if appchoice == "Open":
            PCProcessLOGS = open("PCProcessLOGS","a")
            PCProcessLOGS.write("Setting up "+ appchoice + "\n")
            PCProcessLOGS.write(str(currentDT) + "\n")
            PCProcessLOGS.write("------------------\n")
            PCProcessLOGS.close
            print("Opening!")
            if "filetf" == True:
                print("Accessing file...")
                open(save1)
            else:
                print("Error: You have no save!")
                print("Please go to Config to save a file!")

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

        
