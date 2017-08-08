from subprocess import call

def leave():
    print("Goodbye")
    quit()

while 42:
    # generic shell for python based administration
    command = raw_input("gridshell > ")
    if (command == "leave"):
        leave()
    else:
        print(command + " is not a valid command.")
