from Directory import Directory
from File import File

class Filesystem:
    """
    An implementation of a toy in-memory filesystem
    """

    def __init__(self):
        # Initalize the root directory
        self.root = Directory(None)

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
        file does not exist, this returns None
        """
        if not self.curr.file_exists(name):
            return None
        else:
            return self.curr.get_file(name).read(offset, length)
