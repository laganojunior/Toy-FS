def print_goto_help():
    print "'help' for command list"

def print_help():
    print "quit - quit program"
    print "help - print command list"

# Run the shell loop
while True:
    print "$",

    # Get next command
    input_str = raw_input()
    parts = input_str.split()

    if len(parts) == 0:
        print_goto_help()
        continue

    command = parts[0]

    if command == "quit":
        break
    elif command == "help":
        print_help()
    else:
        print "Unknown command:", command
        print_goto_help()

