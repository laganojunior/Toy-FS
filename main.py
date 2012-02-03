from Filesystem import Filesystem

def print_goto_help():
    print "'help' for command list"

def print_help():
    print "quit - quit program"
    print "help - print command list"
    print "mkdir <directory_name> - make a new subdirectory"
    print "ls - list directory contents"

# Create the filesystem
fs = Filesystem()

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
    elif command == "mkdir":
        if len(parts) < 2:
            print "mkdir needs more arguments"
            print "usage: mkdir <directory_name>"
        else:
            fs.create_directory(parts[1])
    elif command == "ls":
        (subdirs, files) = fs.list_contents()

        for name in subdirs:
            print "%s/" % name

        for name in files:
            print name

    else:
        print "Unknown command:", command
        print_goto_help()
