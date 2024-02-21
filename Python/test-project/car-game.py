isStarted = False
quit = False
print("""Type:
start - to start the car
stop - to stop the car
quit - to exit
""")
while(not quit):
    command = str(input(">")).lower()
    if(command == "start"):
        if(isStarted):
            print("Car is already started.")
        else:
            print("Car started...Ready to go!")
            isStarted = True
    elif(command == "stop"):
        if(isStarted):
            print("Car stopped.")
            isStarted = False
        else:
            print("Car is already stopped.")
    elif(command == "quit"):
        print("Quitting...")
        quit = True
    else:
        print("I don't understand that...")