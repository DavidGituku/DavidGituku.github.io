command=""
started=False
while True:#while command != "quit":
    command=input(">").lower()
    if command=="start" :
        if started:
            print("Car is already started")
        else:
            started=True
            print("car started")
    elif command=="stop":
        if not started:
            print("Car already stopped")
        else:
            started=False
            print("Car is stopped")
    elif command=="help":
        print("""
Press Start to start the car
Press Stop to stop the car
Press Help for Help
Press Quit to Exit the game
              """)
    elif command=="quit":
        save_Query=input("Do you want to save you progress?   Y/N ").upper()
        if save_Query=="Y":
            print("Progress saved, You will pick up from where you left")
            break
        elif save_Query=='N':
            print("You might lose your progress, press ok to continue or cancel to cancel")
            prompt=input("Enter ok/cancel  ").lower()
            if prompt=="ok":
              break
    else:
        print("This command is unrecognised, press the help button for help")

    