from Directory import Directory
from File import File
from FSException import FSException

class Filesystem:
    """
    An implementation of a toy in-memory filesystem
    """

    def __init__(self):
        # Initalize the root directory
        self.root = Directory("", None)

        # Initialize the directory cursor to the root directory
        self.curr = self.root

    def create_directory(self, name):
        """
        Create a new subdirectory under the current directory
        """
        self.curr.create_subdirectory(name)

    def list_contents(self):
        """
        Returns a tuple of (list of subdirectories, list of files)
        under the current directory
        """
        return (self.curr.get_subdirectory_names(), self.curr.get_file_names())

    def write_to_file(self, name, offset, data):
        """
        Writes data to a file in the current directory. If the file does not
        exist, then it will be created.
        """
        if not self.curr.file_exists(name):
            self.curr.create_file(name)

        f = self.curr.get_file(name)
        f.write(offset, data)

    def read_from_file(self, name, offset, length):
        """
        Reads from data from a file starting from the desired offset. If the
        file does not exist, this throws a FSException
        """
        if not self.curr.file_exists(name):
            raise FSException("File %s doesn't exist" % name)
        else:
            return self.curr.get_file(name).read(offset, length)

    def rename_file(self, name, newname):
        """
        Renames a file.
        """
        self.curr.rename_file(name, newname)

    def rename_dir(self, name, newname):
        """
        Renames a directory.
        """
        self.curr.rename_subdirectory(name, newname)

    def resolve_path(self, path):
        """
        Returns the directory corresponding to the path string relative to the
        current directory. Raises an FSException on an error.
        """
        if path == "":
            return self.curr

        # check if the path starts with /, then it is absolute and should start
        # root
        cursor = self.curr
        if path[0] == "/":
            cursor = self.root
            path = path[1:]

        dirs = path.split("/")

        for dirname in dirs:
            if dirname == "":
                continue

            if dirname == "..": # Parent
                p = cursor.get_parent()
                if p is not None:
                    # If the node has no parent,
                    # then it is the root. Otherwise,
                    # go up one level
                    cursor = p
                continue

            if not cursor.subdirectory_exists(dirname):
                raise FSException("Directory %s doesn't exist" % dirname)

            cursor = cursor.get_subdirectory(dirname)

        return cursor

    def change_curr(self, path):
        """
        Changes the current directory
        """
        self.curr = self.resolve_path(path)

    def get_working_path(self):
        """
        Returns the current working path
        """
        return self.curr.pwd()

    def move_file(self, name, path, delete=True):
        """
        Moves a file
        """
        # Check the file exists
        if not self.curr.file_exists(name):
            raise FSException("File %s doesn't exist" % name)

        target = self.resolve_path(path)

        if target.file_exists(name):
            raise FSException("File %s already exists in target location" % name)

        # Move the file by deleting it and recreating it
        f = self.curr.get_file(name)
        if delete:
            self.curr.delete_file(name)
        target.add_file(name, f)

    def move_directory(self, name, path, delete=True):
        """
        Moves a directory
        """
        # Check the directory exists
        if not self.curr.subdirectory_exists(name):
            raise FSException("Directory %s doesn't exist" % name)

        target = self.resolve_path(path)

        if target.subdirectory_exists(name):
            raise FSException("Directory %s already exists in target location" % name)

        # Move the directory by deleting it and recreating it
        d = self.curr.get_subdirectory(name)
        if delete:
            self.curr.delete_subdirectory(name)
        target.add_subdirectory(name, d)

    def delete_file(self, name):
        """
        Delete a file
        """
        self.curr.delete_file(name)

    def delete_directory(self, name):
        """
        Delete a subdirectory
        """
        self.curr.delete_subdirectory(name)

    def copy_file(self, name, path):
        """
        Copies a file
        """
        # Perform the move without the delete
        self.move_file(name, path, False)

    def copy_directory(self, name, path):
        """
        Copies a directory
        """
        # Perform the move with the delete
        self.move_directory(name, path, False)
