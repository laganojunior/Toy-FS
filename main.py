from Filesystem import Filesystem
from FSException import FSException

def print_goto_help():
    print "'help' for command list"

def print_help():
    print "quit - quit program"
    print "help - print command list"
    print "cd <path> - changes the current directory"
    print "cp <file> <path> - Copies a file"
    print "cpdir <directory> <path>- Copies a subdirectory"
    print "ls - list directory contents"
    print "mkdir <directory_name> - make a new subdirectory"
    print "mv <file> <path> - Moves a file to a new directory"
    print "mvdir <directory> <path> - Moves a directory to a new directory"
    print "read <file_name> <offset> <length> - Read data from a file starting from some offset up to a desired length"
    print "rename <file_name> <new_filename> - Rename a file"
    print "renamedir <directory_name> <new_directory_name> - Rename a directory"
    print "rm <file> - Deletes a file"
    print "rmdir <directory> - Deletes a subdirectory"
    print "write <file_name> <offset> <data> - Write data to a file starting from some offset."

# Create the filesystem
fs = Filesystem()

# Run the shell loop
while True:
    print "[" + fs.get_working_path() + "] $",

    # Get next command
    input_str = raw_input()
    parts = input_str.split()

    if len(parts) == 0:
        print_goto_help()
        continue

    command = parts[0]

    try:
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
        elif command == "write":
            if len(parts) != 4:
                print "write expects exactly 3 arguments"

                print "usage: write <file_name> <offset> <data>"
                continue

            if not parts[2].isdigit():
                print "offset must be numeric"
                print "usage: write <file_name> <offset> <data>"
                continue

            fs.write_to_file(parts[1], int(parts[2]), parts[3])
        elif command == "read":
            if len(parts) != 4:
                print "read expects exactly 3 arguments"

                print "usage: read <file_name> <offset> <length>"
                continue

            if not parts[2].isdigit() or not parts[3].isdigit():
                print "offset and length must be numeric"
                print "usage: read <file_name> <offset> <length>"
                continue

            print fs.read_from_file(parts[1], int(parts[2]), int(parts[3]))
        elif command == "rename":
            if len(parts) != 3:
                print "rename expects exactly 2 arguments"
                print "usage: rename <filename> <new_filename>"
            else:
                fs.rename_file(parts[1], parts[2])
        elif command == "renamedir":
            if len(parts) != 3:
                print "renamedir expects exactly 2 arguments"
                print "usage: renamedir <directory_name> <new_directory_name>"
            else:
                fs.rename_dir(parts[1], parts[2])
        elif command == "cd":
            if len(parts) != 2:
                print "cd expects exactly 1 argument"
                print "usage: cd <path>"
            else:
                fs.change_curr(parts[1])
        elif command == "mv":
            if len(parts) != 3:
                print "mv expects exactly 2 arguments"
                print "usage: mv <file> <path>"
            else:
                fs.move_file(parts[1], parts[2])
        elif command == "mvdir":
            if len(parts) != 3:
                print "mvdir expects exactly 2 arguments"
                print "usage: mvdir <directory> <path>"
            else:
                fs.move_directory(parts[1], parts[2])
        elif command == "rm":
            if len(parts) != 2:
                print "rm expects exactly 1 argument"
                print "usage: rm <file>"
            else:
                fs.delete_file(parts[1])
        elif command == "rmdir":
            if len(parts) != 2:
                print "rmdir expects exactly 1 argument"
                print "usage: rmdir <directory>"
            else:
                fs.delete_directory(parts[1])
        elif command == "cp":
            if len(parts) != 3:
                print "cp expects exactly 2 argument"
                print "usage: cp <file> <path>"
            else:
                fs.copy_file(parts[1], parts[2])
        elif command == "cpdir":
            if len(parts) != 3:
                print "cpdir expects exactly 2 argument"
                print "usage: cpdir <directory> <path>"
            else:
                fs.copy_directory(parts[1], parts[2])
        else:
            print "Unknown command:", command
            print_goto_help()
    except FSException as e:
        print "Error:", e
