import time
Pass = input("Enter your Password ")
if Pass == "password":
    print("Logging in")
    time.wait(3)
    print("Welcome to Home Screen")
    time.wait(2)
    Choice = input("What would you like to do?")
    if Choice == ("Internet"):
        print("Connecting...")
        time.sleep(3)
        print("Unable to Connect to the server")
        print("Please check your connection and try again")


else:
    print("Invalid Credentials")