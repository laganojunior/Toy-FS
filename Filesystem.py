from Directory import Directory
from File import File
from FSException import FSException

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

