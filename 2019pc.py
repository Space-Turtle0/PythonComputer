import time, webbrowser, os, warnings
time.sleep(3)
print("Booting...")
psword =input("Please enter your password ")
if psword ==("Bluecore"):
    print("Logging in...")
    time.sleep(2)
    print("Welcome to the Home Screen. This computer is not built for real life useage..")
    print("This computer is soley for the use of testing.")
    time.sleep(2)

    des = "y"
    while des == "y":
        appchoice =input("What would you like to use today? (Calculator,Browser, Logout, Settings.)")
        if appchoice ==("Settings"):
            print("Loading...")
            time.sleep(2)
            print("Connecting to document...")
            Logs = open(r"Logs.txt", "r")
            print(Logs.readlines())
            Logs.close()

        if appchoice ==("Browser"):
            website=input("What would you like to search? Format: python.org ")
            print("Opening "+ "www."+website)
            time.sleep(1)
            print("Requesting www."+website, "with chrome")
            time.sleep(1)
            webbrowser.open("www."+ website,new=0, autoraise=True)
            Logsweb = open(r"Logs.txt", "a")
            Logsweb.write("Visited: www."+ website + "\n")
            Logsweb.close()
        if appchoice ==("Calculator"):
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

        des = input("Do you want to proceed home/destination? (y/n)")

        if appchoice ==("RMGame"):
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
            print("This game is undergoing high improvements.So please be mindful of the game..")
            print("Checking status of the game...")
            print("Starting connection...")
            time.sleep(3)
            webbrowser.open('www.roblox.com/games/1466995005/Ragdoll-Mayhem?refPageId=d99e069d-944a-4f48-b55c-34352d088da1, new=0, autoraise=True')
            time.sleep(2)
        if appchoice == "Console":
            print("Launching a instance")
            warnings.warn('Launching instance requires credentials!')
            time.sleep(2)
            username1 =input("Username: ")
            if username1 == "BlueCore":
                password1 =input("Password: ")
                if password1 == "RedApple":
                    warnings.warn("Attempting to start...")
                    instancename =input("Instance Name:")
                    SSH = input("Instance name: ")
                    os.system('start "SSH":')


        if appchoice == "Settings":
            os.system('start ms-settings:')
        if appchoice == "Prime":
            num =int(input("Number to test: "))
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

