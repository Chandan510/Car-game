command = ""
started = False
stopped = False
while command != "quit":
    command = input(">".upper())
    if command == "start":
        if started:
            print("Car already started")

        else:

            started = True
            print("Car Started")

    elif command == "stop":
        if stopped:
            print("Car already stopped")
        else:
            stoped = True
            print("Car stopped")


    elif command == "help":
        print("""
        Start - To start car
        Stop - To stop a car
        quit - To exit game
        """)
    elif command == "quit".lower():
        break
    else:
        print("Sorry, I can't understand ")












